import json
from odoo.tools import json_default
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
    
    # @http.route('/appointment', type='http', auth="public", website=True)
    # def appointment_page(self):
    #     return request.render("om_hospital.appointment")

    @http.route('/hospital/task', type='json', auth='public', website=True)
    def hospital_task_data(self,**kwargs):
        tasks = request.env['hospital.task'].sudo().search([])

        task_list = [{
                    'id':task.id,
                    'title':task.title,
                    'color':task.color,
                    'isCompleted':task.isCompleted,
               }
               for task in tasks]
        
        json_data = json.dumps(task_list, default=json_default)
        return json_data  