from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _description = "Hospital Operation"
    _rec_name = 'operation_name'

    doctor_id = fields.Many2one('res.users',string="Doctor" , required=True )
    operation_name = fields.Char(string="Operation Name")

    @api.model
    def name_create(self,name):
        return self.create({'operation_name':name}).name_get()[0]