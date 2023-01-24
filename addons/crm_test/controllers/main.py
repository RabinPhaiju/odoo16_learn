from odoo import http
from odoo.http import request


class LeadData(http.Controller):
    @http.route('/crm/leads',type='http',auth="user",website=True)
    def leads_data(self,**kw):
       leads_data = request.env['crm.lead'].sudo().search([])
       values = {
            'data_records':leads_data
       }
       print(values)
       
       return request.render('crm_test.tmp_leads_data',values)
