from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread']
    _description = "Patient Appointment"

    patient_id = fields.Many2one('hospital.patient',String="Patient",tracking=True)
    appointment_time = fields.Datetime(string="Appointment Time",default=fields.Datetime.now,tracking=True)    
    booking_date = fields.Date(string="Booking Date",default=fields.Date.today,tracking=True)
    gender = fields.Selection(string="Gender",related='patient_id.gender',readonly=False)
    age = fields.Integer(string="Age",related='patient_id.age',readonly=False)
     # suggestion are ignored in related
     # changing the related value will reflect to the related_field_model_value
