# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Manage library catelog and book lending.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Vinci Coding",
    'license': "AGPL-3",
    'website': "http://www.davinci-universe.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # Display in the app list or not
    'application': True,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
