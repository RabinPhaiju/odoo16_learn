from odoo import models, fields, api
from odoo.http import request

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        result = super(ResPartner, self).create(vals)
       
        return result
