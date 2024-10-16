# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Notice Board',
    'version': '17.0',
    'summary': 'A platform for sharing important information.',
    'description': """ A notice board serves as a central location for posting announcements, news, events, and 
     other information.
     It facilitates communication and ensures that everyone stays informed and up-to-date.
     """,
    'category': 'Notice',
    'author': 'Khondokar Md. Mehedi Hasan',
    'website': 'https://www.github.com/mehedi360272',
    'currency': 'EUR',
    'price': 49.99,
    'depends': [
        'base',
        'mail',
        'website',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Data
        'data/data.xml',
        # views
        'views/se_notice.xml',
        'views/notice_type.xml',
        'views/menus.xml',
        'views/template.xml',

    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
