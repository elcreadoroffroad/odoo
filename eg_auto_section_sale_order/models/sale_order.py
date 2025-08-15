from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        order = super(SaleOrder, self).create(vals)
        order.create_auto_section_lines()
        return order

    @api.model
    def write(self, vals):
        result = super(SaleOrder, self).write(vals)
        self.create_auto_section_lines()
        return result

    def create_auto_section_lines(self):
        section_lst = []
        sorted_sale_line_section_ids = sorted(self.order_line, key=lambda line: line.product_id.section_id.id)
        for sale_line_section_id in sorted_sale_line_section_ids:
            section_id = sale_line_section_id.product_id.section_id
            if section_id:
                section_vals = {
                    'display_type': 'line_section',
                    'name': section_id.name,
                    'order_id': self.id,
                    'product_id': False,
                }
                if section_id not in section_lst:
                    section_lst.append(section_id)
                    self.env['sale.order.line'].create(section_vals)

            elif sale_line_section_id.display_type == 'line_section' and not sale_line_section_id.product_id:
                section_id = self.env['sale.order.section'].search([('name', '=', sale_line_section_id.name)], limit=1)
                section_lst.append(section_id)

        counter = 1
        for section_id in section_lst:
            sale_line_section_id = self.env['sale.order.line'].search(
                [('product_id', '=', False), ('name', '=', section_id.name), ('order_id', '=', self.id)], limit=1)
            if sale_line_section_id:
                sale_line_section_id.sequence = counter
                counter += 1
            section_sale_line_ids = self.order_line.filtered(lambda l: l.product_id.section_id.id == section_id.id)
            for sale_line_id in section_sale_line_ids:
                sale_line_id.sequence = counter
                counter += 1
