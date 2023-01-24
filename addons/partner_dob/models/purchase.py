from odoo import models,fields

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(selection_add=[('wait','Waiting'),])