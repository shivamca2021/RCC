# -*- coding: utf-8 -*-
##############################################################################
{
    'name' : 'Palette Tracking',
    'version' : '14.0',
    'summary': 'Palette Tracking Process',
    'category': 'base',
    'author': 'Shiva Singh',
    'depends' : ['sale', 'sale_management', 'base', 'stock', 'sale_stock', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/palette_tracking_view.xml',
        'views/res_partner_view.xml',
        'views/res_config_settings_view.xml',
    ],
    'qweb': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}
