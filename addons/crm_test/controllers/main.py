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

     @http.route('/crm/leads_form',type='http',auth="user",website=True)
     def leads_form(self,**kw):
          return http.request.render('crm_test.create_lead',{})


     @http.route('/create/web_lead',type='http',auth="user",website=True)
     def create_web_lead(self,**kw):
          val={
               'name':kw.get('name'),
               'age':9, #calculate
               'email':kw.get('email')}
          request.env['res.partner'].sudo().create(val)
          # res.partner ma add vayo

          # aba kasari crm.lead ma res.partner ko relation rakhne


          return request.render("crm_test.lead_thanks",{})
