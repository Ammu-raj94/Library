# -*- coding: utf-8 -*-

from odoo import fields,models

class SaleOrder(models.Model):
    """Inherited Sale order for adding new field"""
    _inherit = 'sale.order'

    customer_reference = fields.Char(string='Customer Reference',
                                     help='Reference of Customer')

    def action_confirm(self):
        """Overriding the Confirm function for send Email."""
        res = super(SaleOrder, self).action_confirm()
        email_template = self.env.ref('library_management.email_template_sale_order')
        for order in self:
            email_template.send_mail(order.id, force_send=True)
        return res