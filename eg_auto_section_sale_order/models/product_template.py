from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    section_id = fields.Many2one('sale.order.section', string='Sale Order Section')
