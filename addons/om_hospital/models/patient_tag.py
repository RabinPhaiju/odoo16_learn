from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="Name" , required=True )
    active = fields.Boolean(string="Active" ,default=True )
    color = fields.Integer(string="Color")
    color2 = fields.Char(string="Color2")