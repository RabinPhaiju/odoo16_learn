from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Patient Records"

    name = fields.Char(string='Name',required=True,tracking=True)
    age = fields.Integer(string="Age",tracking=True)
    is_child = fields.Boolean(string="Is Child?",tracking=True)
    notes = fields.Text(string="Notes",tracking=True)
    gender = fields.Selection([('male',"Male"),('female','Female'),('others','Others')],string="Gender",tracking=True)
    capitalized_name = fields.Char(string='Capitalized Name',compute='_compute_capitalized_name',store=True) # becomes readonly and not stored in db by default


    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
        
    @api.depends('name')
    def _compute_capitalized_name(self):
        # runs after saving if depends is not added
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ""

    @api.constrains('is_child','age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded !"))