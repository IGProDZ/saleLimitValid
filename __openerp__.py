# -*- coding: utf-8 -*-
{
    'name': "Date de validité de commande",

    'summary': """
        Ajoute une date de fin de validité aux bons de commande""",

    'description': """
        Ajoute un champs date au modèle sale.order permettant de
        de spécifier la date de fin de validité de clui-ci et l'affiche
        sur les rapports imprimés
    """,

    'author': "Nacim ABOURA",
    'website': "http://www.igpro-online.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "sale"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views.xml',
        'templates.xml',
        'reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}