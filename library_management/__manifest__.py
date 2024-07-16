# -*- coding: utf-8 -*-

{
    'name': 'Library Management',
    'version': '16.0.1.0.0',
    'category': 'Productivity',
    'summary': """Managing Books in Library""",
    'description': """This module helps to manage Book system in a Library""",
    'author': '',
    'website': "",
    'company': '',
    'maintainer': '',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_actions_server_data.xml',
        'data/mail_template_data.xml',
        'views/book_views.xml',
        'views/sale_order_views.xml',
        'views/sale_order_report_templates.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
