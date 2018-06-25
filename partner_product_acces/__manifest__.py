# -*- coding: utf-8 -*-
{
    "name": "Permisos de Usuario (Cliente y Producto)",
    'author': "Falcón Solutions",
    'maintainer': 'Falcon Solutions',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    "version": "10.0.0.0.1",
    "category": "Sales Management",
    'description': """
Proporciona Permisos a Usuarios sobre la Creación y Edición de Cliente, Productos y Cuentas Analíticas
""",
    "depends": [
        "base",
        "sale",
    ],
    "data": [
        'views/res_users_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
