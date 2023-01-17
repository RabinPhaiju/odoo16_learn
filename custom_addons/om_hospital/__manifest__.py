# -*- coding: utf-8 -*-
{

'name': "Hospital Management System",
'version': '1.0',
'category': 'Healthcare',
'summary': 'A module for managing patients, appointments, and billing in a hospital.',
'description': '''
        This module provides functionality for managing patients, scheduling appointments, and handling billing in a hospital setting.
    ''',
'author': 'Rabin Phaiju',
'website': 'http://www.rabinphaiju15@gmail.com',
'category': 'Tools',
'depends':['base','contacts','hr','account','mail'],
'data': [
    'security/ir.model.access.csv',
    'data/sequence.xml',
    'views/menu.xml',
    'views/patient.xml',
],
'demo':[],
'images':['static/description/icon.png'],
'installable': True,
'application': True,
'auto_install': False
}