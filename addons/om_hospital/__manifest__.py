# -*- coding: utf-8 -*-
{

'name': "Hospital Management System",
'version': '1.0.0',
'category': 'Hospital',
'sequence':-100,
'summary': 'A module for managing patients, appointments, and billing in a hospital.',
'description': '''
        This module provides functionality for managing patients, scheduling appointments, and handling billing in a hospital setting.
    ''',
'author': 'Rabin Phaiju',
'website': 'http://www.rabinphaiju15@gmail.com',
'depends':['base','contacts','hr','account','mail','product','website'],
'data': [
    'security/ir.model.access.csv',
    'data/sequence.xml',
    'data/patient.tag.csv',
    'data/patient_tag_data.xml',
    'data/mail_template_data.xml',
    'wizard/cancel_appointment.xml',
    'views/menu.xml',
    'views/patient.xml',
    'views/female_patient.xml',
    'views/appointment.xml',
    'views/website_form.xml',
    'views/patient_tag.xml',
    'views/odoo_playground.xml',
    'views/odoo_query.xml',
    'views/res_config_settings.xml',
    'views/operation.xml',
],
'demo':[],
'images':['static/description/icon.png'],
'installable': True,
'application': True,
'auto_install': False,
'license':'LGPL-3'
}