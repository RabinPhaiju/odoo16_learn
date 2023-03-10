from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class HospitalTask(models.Model):
    _name = "hospital.task"
    _description = "Hospital Task"
    _rec_name = 'title'

    title = fields.Char(string="Title")
    color = fields.Char(string="Color")
    isCompleted = fields.Boolean(string="isCompleted")