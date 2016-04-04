# -*- coding: utf-8 -*-
{
    'name': "Cursos - Mi Módulo",

    'summary': """
        Este es una practica de desarrollo""",

    'description': """
        Aprendiendo Oddo 8, se utliza este modulo como ejemplo
    """,

    'author': "Freelance",
    'website': "http://codigoaox.blogspot.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'dev',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo.xml',
    #],
    
    #'installable': True,
    'application': True,

}