# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Administration Fleet Management',
    'version': '1.0.0',
    'summary': 'Manage your fleet and track missions costs',
    'sequence': -100,
    'description': """ Manage your fleet and track missions costs """,
    'category': 'Fleet',
    'depends': ['purchase', 'hr', 'fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/city.xml',
        'views/lessor.xml',
        'views/driver.xml',
        'views/vehicle.xml',
        'views/driver_log.xml',
        'views/mission.xml',
        'views/contract.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}
