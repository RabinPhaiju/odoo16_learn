from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class AppointmentPharmacy(models.Model):
    _name = "appointment.pharmacy.lines"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product')
    price_unit = fields.Float(String="Price")
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment',string='Appointment')