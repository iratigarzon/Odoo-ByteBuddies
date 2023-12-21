# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Bytebuddies",

    'summary': """
        Module of our application Bytebuddies""",

    'description': """
        This app is able to store academic information
    """,

    'author': "",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
'data': [
    'security/byteBuddies_security.xml',
    'menu_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/content.xml',
    ],
}
