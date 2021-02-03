# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class DetalleFactura(models.Model):
#     _inherit = 'account.invoice.line'
    
#     precio_sdscto = fields.Integer(compute='precio_sdscto', string='Precio Con Descuento', store=True)

    
#     @api.depends('quantity','precio_unit','discount')
#     def precio_sdscto(self):
#         self.precio_sdscto=round(self.price_subtotal/self.quantity)

    