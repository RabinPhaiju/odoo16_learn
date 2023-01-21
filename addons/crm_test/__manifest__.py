# -*- coding: utf-8 -*-
{

'name': "Customer Relationship Management Test",
'version': '1.0',
'category': 'CRMT',
'summary': 'A module for managing customer relationship.',
'description': '''
        This module provides functionality for managing customer relationship.
    ''',
'author': 'Rabin Phaiju',
'website': 'http://www.rabinphaiju15@gmail.com',
'category': 'Tools',
'depends':['base','contacts','hr','account','mail','crm'],
'data': [
    'security/ir.model.access.csv',
    'views/menu.xml',
    'views/lead.xml',
],
'demo':[],
'images':['static/description/icon.png'],
'installable': True,
'application': True,
'auto_install': False
}