from odoo import http
from odoo.http import request

class Hospital(http.Controller):
    @http.route('/patient_webform', type="http" , auth="user", website=True)
    def patient_webform(self,**kw):
        return http.request.render('om_hospital.create_patient',{})

    @http.route('/create/web_patient', type="http" , auth="user", website=True)
    def create_web_patient(self,**kw):
        request.env['hospital.patient'].sudo().create(kw)
        # To create in another model
        other_val = {
            'other_name':kw.get('name')
        }
        # request.env['other.model'].sudo().create(other_val)

        return request.render('om_hospital.patient_thanks',{})