from odoo import api,fields,models
from datetime import datetime

class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"
    # transient model

    @api.model
    def default_get(self,fields):
        # must be before field
        result = super(CancelAppointmentWizard,self).default_get(fields)
        result['date_cancel'] = datetime.now()
        # print('----------',self.env.context)
        # if self.env.context.get('active_id'):
            # result['appointment_id'] = self.env.context.get('active_id')
        # print('-----------default get execulted in cancel appointment wizard',result)
        return result

    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")
    reason = fields.Text(string="Reason")
    date_cancel = fields.Datetime(string="Cancellation Date")
    

    def action_wizard_cancel(self):
        print("🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 ~ self", self)
        return