from odoo import api,fields,models,_
from odoo.exceptions import ValidationError,UserError,AccessError, MissingError

class PartnerDob(models.Model):
    _inherit = 'res.partner'

    # adding age filed in res.partner
    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string="Is Child?",default=False)

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
           if not vals.get('age'):
                raise ValidationError(_('Age field cannot be empty.'))
        return super(PartnerDob,self).create(vals_list)