from odoo.exceptions import ValidationError
from odoo import api,fields,models,_
from datetime import date

class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"
    # transient model

    @api.model
    def default_get(self,fields):
        # must be before field
        result = super(CancelAppointmentWizard,self).default_get(fields)
        result['date_cancel'] = date.today()
        # print('----------',self.env.context)
        # if self.env.context.get('active_id'):
            # result['appointment_id'] = self.env.context.get('active_id')
        # print('-----------default get execulted in cancel appointment wizard',result)
        return result

    appointment_id = fields.Many2one('hospital.appointment',string="Appointment",
        # domain=['|',('status','=','draft'),('priority','in',('0','1'))]
        )
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancellation Date")
    

    def action_wizard_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_("Cannot cancel appointment in same date !"))
        self.appointment_id.status = 'cancel'
        return