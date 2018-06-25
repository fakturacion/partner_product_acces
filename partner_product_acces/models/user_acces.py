# -*- coding: utf-8 -*-
from odoo import api, models, fields
from odoo.exceptions import UserError, AccessError, ValidationError

class UserPartnerAcces(models.Model):
    _inherit = "res.partner"
    
    @api.model
    def create(self, vals):
        res = super(UserPartnerAcces, self).create(vals)
        if self.env.user.partner_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Crear Clientes o Proveedores.\n Debe solicitar Permisos a un Administrador en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return res

    @api.multi
    def write(self, vals):
        if self.env.user.partner_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Editar Clientes o Proveedores.\n Debe solicitar acceso en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return super(UserPartnerAcces, self).write(vals)

    @api.multi
    def unlink(self):
        if self.env.user.partner_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Eliminar Clientes o Proveedores.\n Debe solicitar acceso en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return super(UserPartnerAcces, self).unlink()

class UserProductAcces(models.Model):
    _inherit = "product.product"
    
    @api.model
    def create(self, vals):
        res = super(UserProductAcces, self).create(vals)
        if self.env.user.product_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Crear Productos.\n Debe solicitar Permisos a un Administrador en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return res

    @api.multi
    def write(self, vals):
        if self.env.user.product_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Editar Productos.\n Debe solicitar acceso en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return super(UserProductAcces, self).write(vals)

    @api.multi
    def unlink(self):
        if self.env.user.product_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Eliminar Productos.\n Debe solicitar acceso en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return super(UserProductAcces, self).unlink()
        
class UserProductTemplateAccess(models.Model):
    _inherit = "product.template"
    
    @api.model
    def create(self, vals):
        res = super(UserProductTemplateAccess, self).create(vals)
        if self.env.user.product_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Crear Productos.\n Debe solicitar Permisos a un Administrador en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return res

    @api.multi
    def write(self, vals):
        if self.env.user.product_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Editar Productos.\n Debe solicitar acceso en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return super(UserProductTemplateAccess, self).write(vals)

    @api.multi
    def unlink(self):
        if self.env.user.product_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Eliminar Productos.\n Debe solicitar acceso en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return super(UserProductTemplateAccess, self).unlink()

class UserAnalyticAcces(models.Model):
    _inherit = "account.analytic.account"
    
    @api.model
    def create(self, vals):
        res = super(UserAnalyticAcces, self).create(vals)
        if self.env.user.analytic_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Crear o Editar Cuentas Analiticas.\n Debe solicitar Permisos a un Administrador en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return res

    @api.multi
    def write(self, vals):
        if self.env.user.analytic_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Editar Cuentas Analiticas.\n Debe solicitar acceso en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return super(UserAnalyticAcces, self).write(vals)

    @api.multi
    def unlink(self):
        if self.env.user.analytic_acces == False:
            error = self.env.user.login," Usted no tiene Permisos para Eliminar Apuntes Analiticos.\n Debe solicitar acceso en Configuración->Usuarios->Permisos Adicionales "
            raise UserError(error)
        return super(UserAnalyticLineAccess, self).unlink()
