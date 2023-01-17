from odoo import api,fields,models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Patient Records"

    name = fields.Char(string='Name',required=True,tracking=True)
    age = fields.Integer(string="Age",tracking=True)
    is_child = fields.Boolean(string="Is Child?",tracking=True)
    notes = fields.Text(string="Notes",tracking=True)
    gender = fields.Selection([('male',"Male"),('female','Female'),('others','Others')],string="Gender",tracking=True)