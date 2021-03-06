# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, fields, models, _

class sale_order(models.Model):
    _inherit = 'sale.order'
    
    #@api.multi    
    #def _prepare_order_line_move(self, order, line, picking_id, date_planned):
    #    res = super(sale_order, self)._prepare_order_line_move(order, line, picking_id, date_planned)
    #    res.update({
    #        'special_info': line.special_info
    #    })
    #    return res
    
    @api.model
    def _prepare_order_line_procurement(self, order, line, group_id=False):
        vals = super(sale_order, self)._prepare_order_line_procurement(order, line, group_id=group_id)
        vals.update({'special_info': line.special_info})
        return vals
          
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: