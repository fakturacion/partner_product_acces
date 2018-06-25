# -*- coding: utf-8 -*-
from odoo import api, models, fields

class ResUsersAcces(models.Model):
    _inherit = "res.users"

    partner_acces = fields.Boolean(string='Crear y Editar Clientes', help="Permiso para Crear y Editar Clientes")
    product_acces = fields.Boolean(string='Crear y Editar Productos', help="Permiso para Crear y Editar Productos")
    analytic_acces = fields.Boolean(string='Crear y Editar Cuentas Analiticas', help="Permiso para Crear Editar Cuentas Analiticas")
