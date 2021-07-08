from odoo import fields, models


class SaleInh(models.Model):

    _inherit = ['sale.order']
