from odoo import api, fields, models


class PurchaseInh(models.Model):

    _inherit = 'purchase.order.line'
