from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class ResGroups(models.Model):
    _inherit = 'res.groups'

    def get_application_groups(self,domain):
        print('---------------domain',domain)
        group_id = self.env.ref('account.group_show_line_subtotals_tax_included').id
        stock_id = self.env.ref('stock.group_stock_picking_wave').id
    
        return super(ResGroups,self).get_application_groups(domain + [('id','not in',(group_id,stock_id))])