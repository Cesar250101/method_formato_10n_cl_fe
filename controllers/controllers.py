# -*- coding: utf-8 -*-
from odoo import http

# class MethodFormato10nClFe(http.Controller):
#     @http.route('/method_formato_10n_cl_fe/method_formato_10n_cl_fe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_formato_10n_cl_fe/method_formato_10n_cl_fe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_formato_10n_cl_fe.listing', {
#             'root': '/method_formato_10n_cl_fe/method_formato_10n_cl_fe',
#             'objects': http.request.env['method_formato_10n_cl_fe.method_formato_10n_cl_fe'].search([]),
#         })

#     @http.route('/method_formato_10n_cl_fe/method_formato_10n_cl_fe/objects/<model("method_formato_10n_cl_fe.method_formato_10n_cl_fe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_formato_10n_cl_fe.object', {
#             'object': obj
#         })