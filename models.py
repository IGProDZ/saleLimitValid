# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import timedelta


class addlimite(models.Model):
    _inherit = 'sale.order'

    valid_until = fields.Date(compute="_date_compute", required=True, string="Limite de validité")

    @api.depends('date_order')
    def _date_compute(self):
        for r in self:
            if not r.date_order:
                r.valid_until = r.date_order
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.date_order)
            duration = timedelta(60, seconds=-1)
            r.valid_until = start + duration
