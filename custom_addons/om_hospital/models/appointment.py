from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread']
    _description = "Patient Appointment"
    _rec_name = "ref"
    # if model has attribute name, we dont need _rec_name else define _rec_name as any attribute field
    # if _rec_name or name field is not in class, It will show model_name,id in Many2one rel

    patient_id = fields.Many2one('hospital.patient',String="Patient",tracking=True)
    appointment_time = fields.Datetime(string="Appointment Time",default=fields.Datetime.now,tracking=True)    
    booking_date = fields.Date(string="Booking Date",default=fields.Date.today,tracking=True)
    gender = fields.Selection(string="Gender",related='patient_id.gender',readonly=False)
    age = fields.Integer(string="Age",related='patient_id.age',readonly=False)
     # suggestion are ignored in related
     # changing the related value will reflect to the related_field_model_value
    ref = fields.Char(string="Reference",default=lambda self:_('New'))


    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment,self).create(vals_list)