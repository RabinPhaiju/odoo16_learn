# -*- coding: utf-8 -*-
{

'name': "School Management",
'summary': """School Management Software""",
'description':"""
    Treating Schools
    """,
'author': 'Rabin Phaiju',
'website': 'http://www.rabinphaiju15@gmail.com',
'category': 'Tools',
'version': '16.0.1.0.0',
'depends':['base','contacts','hr','account'],
'data': [
    'views/school.xml',
    'security/ir.model.access.csv',
],
'demo':[],
'images':['static/description/icon.png'],
'installable': True,
'application': True,
'auto_install': False
}