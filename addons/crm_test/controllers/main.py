from odoo import http
from odoo.http import request


class LeadData(http.Controller):
     @http.route('/crm/leads',type='http',auth="user",website=True)
     def leads_data(self,**kw):
          leads_data = request.env['crm.lead'].sudo().search([])
          values = {
               'data_records':leads_data
          }
          
          return request.render('crm_test.tmp_leads_data',values)

     @http.route('/crm/leads/create',type='http',auth="user",website=True)
     def leads_form(self,**kw):
          return http.request.render('crm_test.create_lead',{})


     @http.route('/create/crm_leads',type='http',auth="user",website=True)
     def create_crm_lead(self,**kw):
          print('----------------------------',kw)
          # request.env['crm.lead'].sudo().create(kw)
          return request.render("crm_test.leads_entry",{})