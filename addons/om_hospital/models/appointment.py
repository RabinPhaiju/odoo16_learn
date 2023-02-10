from odoo import api,fields,models,_
from odoo.exceptions import ValidationError,UserError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Patient Appointment"
    _rec_name = "ref"
    # if model has attribute name, we dont need _rec_name else define _rec_name as any attribute field
    # if _rec_name or name field is not in class, It will show model_name,id in Many2one rel

    doctor_id = fields.Many2one('res.users',String="Doctor",tracking=True)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines','appointment_id',string="Pharmacy Lines")
    patient_id = fields.Many2one('hospital.patient',String="Patient",tracking=True)
    appointment_time = fields.Datetime(string="Appointment Time",default=fields.Datetime.now,tracking=True)    
    booking_date = fields.Date(string="Booking Date",default=fields.Date.today,tracking=True)
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
    status = fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In Consultation'),
        ('done','Done'),
        ('cancel','Cancel'),],string="Status",default='draft')

    hide_sales_price = fields.Boolean(String="Hide Sales Price")


    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment,self).create(vals_list)

    def unlink(self):
        for appointment in self:
            if appointment.status == 'done':
                raise UserError(_('You cannot delete a appointment with DONE status'))
        return super(HospitalAppointment,self).unlink()

    def action_test(self):
        return {
            'effect':{
                'fadeout':'slow',
                'message':"Click successfull",
                'type':'rainbow_man'
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.status = "in_consultation"   
    
    def action_done(self):
        for rec in self:
            rec.status = "done"   
            
    def action_cancel(self):
        action = self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        return action
        # for rec in self:
            # rec.status = "cancel"