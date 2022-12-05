from odoo import models,fields

class School(models.Model):
    _name = 'school.student'

    name = fields.Many2one('res.partner',string='Student')
    full_name = fields.Char(string='FullName')
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')