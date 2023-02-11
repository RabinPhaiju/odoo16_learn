from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class AppointmentPharmacy(models.Model):
    _name = "appointment.pharmacy.lines"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product',required=True)
    price_unit = fields.Float(String="Price",related='product_id.list_price')
    qty = fields.Integer(string="Quantity",default=1)
    appointment_id = fields.Many2one('hospital.appointment',string='Appointment')

    company_currency_id = fields.Many2one('res.currency',related='appointment_id.currency_id')
    price_subtotal = fields.Monetary(string="Subtotal",currency_field="company_currency_id",compute="_compute_price_subtotal")

    @api.depends('price_unit','qty')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.price_unit * rec.qty