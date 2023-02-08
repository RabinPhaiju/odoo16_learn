from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users',string="Confirmed Users")

    def action_confirm(self):
        self.confirmed_user_id = self.env.user.id
        print('---------------- success')
        super(SaleOrder,self).action_confirm()