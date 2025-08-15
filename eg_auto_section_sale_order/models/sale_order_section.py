from odoo import models, fields


class SaleOrderSection(models.Model):
    _name = 'sale.order.section'

    name = fields.Char(string="Sale Order Section")
