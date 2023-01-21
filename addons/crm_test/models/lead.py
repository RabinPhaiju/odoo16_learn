from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    # _name = "crm.lead.test"
    _inherit = 'crm.lead'
    _description = "crm lead test"

    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string="Is Child?",default=False)

    def orm_methods(self):
        leads = self.env['crm.lead'].search([])
        lead_one = self.env['crm.lead'].search(['id','=',1])

        sorted_out = leads.sorted(key='id',reverse=True)

        child_ids = leads.filtered(lambda l:l.is_child)

        lead_names = leads.mapped('name')