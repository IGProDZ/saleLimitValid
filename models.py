# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import timedelta
from datetime import date

class addlimite(models.Model):
    _inherit = 'sale.order'

    valid_until = fields.Date(compute="_date_compute", required=True, string="Limite de validité")
    valid_duration = fields.Integer(string="Durée de Validité")
    today = fields.Date(compute="_date_expiration")

    # , cr, uid, context=None

    def _cancel_expired_quotation(self, cr, uid, context=None):
        context = dict(context or {})
        print"====================================================================="
        print "I AMMMMM INNNNNN"
        print"====================================================================="
        today = date.today().strftime('%Y-%m-%d')
        for r in self:
            if r.valid_until > today:
                r.states="cancel"

    def _date_expiration(self):
        self.today =  date.today().strftime('%Y-%m-%d')

    @api.onchange('today')
    def _write_changes(self):

        if self.valid_until > self.today:
            return {'warning':{'title':'Attention', 'message':'devis expiré'}}

    @api.depends('date_order')
    def _date_compute(self):
        for r in self:
            if not r.date_order:
                r.valid_until = r.date_order
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.date_order)
            duration = timedelta(self.valid_duration, seconds=-1)
            r.valid_until = start + duration

class addlimite(models.TransientModel):
    # _name = 'My.setting_sale_config'
    _inherit = 'sale.config.settings'

    default_valid_duration = fields.Integer(string="Durée de Validité des devis (Jours) ", help="""Cette valeur définit la durée de validitié d'un devis client, elle sera utilisé comme valeur par défault """,  default_model='sale.order')
