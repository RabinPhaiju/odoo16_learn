# -*- coding: utf-8 -*-
{

'name': "Om Sales Order",
'version': '1.0',
'sequence':-98,
'summary': 'A module for managing Sales Order.',
'description': '''
        This module provides functionality for managing sales order.
    ''',
'author': 'Rabin Phaiju',
'website': 'http://www.rabinphaiju15@gmail.com',
'depends':['base','contacts','hr','sale','mail','sale_stock'],
'data': [
    'security/ir.model.access.csv',
    'views/menu.xml',
    'views/sale_order.xml',
],
'demo':[],
'images':['static/description/icon.png'],
'installable': True,
'application': True,
'auto_install': False
}