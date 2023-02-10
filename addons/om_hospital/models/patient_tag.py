from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="Name" , required=True )
    active = fields.Boolean(string="Active" ,default=True,copy=False)
    sequence = fields.Integer(string="Sequence")
    color = fields.Integer(string="Color")
    color2 = fields.Char(string="Color2")

    @api.returns('self',lambda value:value.id)
    def copy(self,default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _('%s (Copy)',self.name)
            default['sequence'] = self.sequence+1
        return super (PatientTag,self).copy(default)

    _sql_constraints = [('unique_name','unique(name)',"Tag name must be unique!")]
    _sql_constraints = [('check_sequence','check(sequence > 0)',"Sequence must be greater than 0!")]
