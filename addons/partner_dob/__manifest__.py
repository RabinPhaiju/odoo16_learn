# -*- coding: utf-8 -*-
{

'name': "Partner Dob",
'version': '1.0',
'category': 'CRMT',
'summary': 'A module for partner dob test.',
'description': '''
        This module provides functionality for managing partner dob.
    ''',
'author': 'Rabin Phaiju',
'website': 'http://www.rabinphaiju15@gmail.com',
'category': 'Tools',
'depends':['base','contacts','hr','account','mail'],
'data': [
    'security/ir.model.access.csv',
    'views/res_partner_views.xml',
],
'demo':[],
'images':['static/description/icon.png'],
'installable': True,
'application': True,
'auto_install': False
}