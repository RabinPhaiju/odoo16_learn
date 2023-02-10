from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="Name" , required=True )
    active = fields.Boolean(string="Active" ,default=True )
    sequence = fields.Integer(string="Sequence")
    color = fields.Integer(string="Color")
    color2 = fields.Char(string="Color2")

    _sql_constraints = [('unique_name','unique(name,active)',"Tag name must be unique!")]
    _sql_constraints = [('check_sequence','check(sequence > 0)',"Sequence must be greater than 0!")]
