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
'depends':['base','contacts','hr','account','mail','product'],
'data': [
    'security/ir.model.access.csv',
    'data/sequence.xml',
    'views/menu.xml',
    'views/patient.xml',
    'views/female_patient.xml',
    'views/appointment.xml',
    'views/website_form.xml',
    'views/patient_tag.xml',
],
'demo':[],
'images':['static/description/icon.png'],
'installable': True,
'application': True,
'auto_install': False,
'license':'LGPL-3'
}