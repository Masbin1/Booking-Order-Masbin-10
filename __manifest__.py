# -*- coding: utf-8 -*-
{
    'name': "Booking_Order_Masbintang_10",

    'summary': """
        Booking Order""",

    'description': """
        Booking Order Mas Bintang Dengan Odoo 10
    """,

    'author': "Mas Bin",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',
    'installable': True,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_cancelled.xml',
        'views/work_order.xml',
        'views/booking_order.xml',
        'views/service_team.xml',
        'views/menu.xml',
        'report/work_order_report.xml',
        'report/report.xml',
        'data/data.xml'
        
    ],
}