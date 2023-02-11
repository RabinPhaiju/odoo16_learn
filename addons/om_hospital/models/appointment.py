from odoo import api,fields,models,_
from odoo.exceptions import ValidationError,UserError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Patient Appointment"
    _rec_name = "ref"
    # if model has attribute name, we dont need _rec_name else define _rec_name as any attribute field
    # if _rec_name or name field is not in class, It will show model_name,id in Many2one rel
    _order = 'id desc, appointment_time asc'

    doctor_id = fields.Many2one('res.users',String="Doctor",tracking=1)
    operation_id = fields.Many2one('res.users',String="Operation",tracking=20)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines','appointment_id',string="Pharmacy Lines")
    patient_id = fields.Many2one('hospital.patient',String="Patient",tracking=3,ondelete="restrict") 
    # ondelete="cascade"
    # restrict with prevent from deleting record with is used in another model
    # cascade with delete the related records from another model as it is deleted.

    appointment_time = fields.Datetime(string="Appointment Time",default=fields.Datetime.now,tracking=4)    
    booking_date = fields.Date(string="Booking Date",default=fields.Date.today,tracking=5)
    duration = fields.Float(string="Duration",tracking=2)

    company_id = fields.Many2one('res.company',string="Company",default=lambda self:self.env.company)
    currency_id = fields.Many2one('res.currency',related='company_id.currency_id')

    gender = fields.Selection(string="Gender",related='patient_id.gender',readonly=False)
    age = fields.Integer(string="Age",related='patient_id.age',readonly=False)
     # suggestion are ignored in related
     # changing the related value will reflect to the related_field_model_value
    ref = fields.Char(string="Reference",default=lambda self:_('New'),help="Reference of the appointment")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very Hight'),],string="Priority",default='0')
    state = fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In Consultation'),
        ('done','Done'),
        ('cancel','Cancel'),],string="State",default='draft')

    hide_sales_price = fields.Boolean(String="Hide Sales Price")
    progress = fields.Integer(string="Progress",compute="_compute_progress")


    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment,self).create(vals_list)

    @api.depends('state')
    def _compute_progress(self):
        for rec in self:
            progress = 0
            if rec.state == 'draft':
                progress = 25
            elif rec.state == 'in_consultation':
                progress = 50
            elif rec.state == 'done':
                progress = 100
            rec.progress = progress

    def unlink(self):
        for appointment in self:
            if appointment.state == 'done':
                raise UserError(_('You cannot delete a appointment with DONE state'))
        return super(HospitalAppointment,self).unlink()

    def action_object_test(self):
        return {
            'type':'ir.actions.act_url',
            'target':'self',
            'url': '/patient_webform'
        }

    def action_in_consultation(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = "in_consultation"   
    
    def action_done(self):
        for rec in self:
            rec.state = "done"  
        return {
            'effect':{
                'fadeout':'slow',
                'message':"Done",
                'type':'rainbow_man'
            }
        } 
            
    def action_cancel(self):
        action = self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        return action
        # for rec in self:
            # rec.state = "cancel"
    
    def action_send_mail(self):
        if self.patient_id.email:
            template = self.env.ref('om_hospital.hospital_appointment_email')
            for rec in self:
                # pass object.id
                template.send_mail(rec.id)
    
    def action_share_whatsapp(self):
        if not self.patient_id.phone:
            raise ValidationError(_("Missing phone number in patient record"))
        
        message = 'Hi *%s*, your appointment number is: %s, Thank you' % (self.patient_id.name,self.ref)
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' %(self.patient_id.phone,message)
        
        self.message_post(body=message,subject="Whatsapp")

        return {
            'type':'ir.actions.act_url',
            'target':'new',
            'url':whatsapp_api_url
        }
    
    def action_notificaiton(self):
        action = self.env.ref('om_hospital.action_hospital_patient')
        # 'next' will redirect to next window after display notification
        return {
            'type':'ir.actions.client',
            'tag':'display_notification',
            'params':{
                'title': ('Click to open the patient record'),
                'message':'%s',
                'links':[{
                    'label':self.patient_id.name,
                    'url':f'#action={action.id}&id={self.patient_id.id}&model=hospital.patient'
                }],
                'type':'success',
                'sticky':'False',
                'next':{
                    'type':'ir.actions.act_window',
                    'res_model':'hospital.patient',
                    'res_id':self.patient_id.id,
                    'views':[(False,'form')]
                }
            }
        }