from odoo import fields,models

class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    cancel_days = fields.Integer(string="Cancel Days",config_parameter='om_hospital.cancel_days')
    # adding parameter -> config_parameter -> it is stored in res.config.settings