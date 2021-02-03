# -*- coding: utf-8 -*-
{
    'name': "method_formato_10n_cl_fe",

    'summary': """
        Modifica formatos de modulo l10n_cl_fe
        """,

    'description': """
        En primera instancia se modifica el formato de dte_external_layuot
        del modulo l10n_cl_fe,
        Agregar un campo calculado que refleja el precio menos el descuento en el detalle de la factura
    """,

    'author': "Method ERP",
    'website': "http://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_cl_fe'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/formato_factura.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
