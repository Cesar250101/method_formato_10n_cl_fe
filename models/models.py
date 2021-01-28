# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class method_formato_10n_cl_fe(models.Model):
#     _name = 'method_formato_10n_cl_fe.method_formato_10n_cl_fe'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100