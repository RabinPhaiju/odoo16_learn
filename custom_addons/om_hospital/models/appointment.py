from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread']
    _description = "Patient Appointment"

    patient_id = fields.Many2one('hospital.patient',String="Patient",tracking=True)