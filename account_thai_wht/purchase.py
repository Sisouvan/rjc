
from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp

class purchase_order(models.Model):
    _inherit = 'purchase.order'
    
    @api.one
    def _amount_line_tax_ex(self, line, add_disc=0.0):
        val = 0.0
        tax_obj = self.env['account.tax']
        for c in line.taxes_id.compute_all(line.price_unit * (1 - (line.discount or 0.0) / 100.0) * (1 - (add_disc or 0.0) / 100.0), line.product_qty, line.product_id, line.order_id.partner_id)['taxes']:
            if not tax_obj.browse(c['id']).is_wht:
                val += c.get('amount', 0.0)
        return val
    
    # Overwrite
    @api.one
    @api.depends('order_line', 'order_line.price_subtotal')
    def _amount_all(self):
        val = val1 = 0.0
        cur = self.pricelist_id.currency_id
        for line in self.order_line:
            val1 += line.price_subtotal
            val += self._amount_line_tax_ex(line, self.fields_get(['add_disc']) and self.add_disc or 0.0)[0]  # Call new method.
        self.amount_tax = cur.round(val)
        self.amount_untaxed = cur.round(val1)
        self.amount_total = self.amount_untaxed + self.amount_tax
    
    # Overwrite
    amount_untaxed = fields.Float(compute='_amount_all', digits_compute=dp.get_precision('Account'), string='Untaxed Amount', store=True, help="The amount without tax")
    amount_tax = fields.Float(compute='_amount_all', 
                              digits_compute=dp.get_precision('Account'), string='Taxes', store=True, multi="sums", help="The tax amount")
    amount_total = fields.Float(compute='_amount_all', digits_compute=dp.get_precision('Account'), string='Total', store=True, help="The total amount")
    amount_untaxed = fields.Float(compute='_amount_all', digits_compute=dp.get_precision('Account'),
                                  string='Untaxed Amount', store=True, help="The amount without tax", track_visibility='always')
    amount_tax = fields.Float(compute='_amount_all', digits_compute=dp.get_precision('Account'), string='Taxes', store=True, help="The tax amount")
    amount_total = fields.Float(compute='_amount_all', digits_compute=dp.get_precision('Account'), string='Total', store=True, help="The total amount")
    