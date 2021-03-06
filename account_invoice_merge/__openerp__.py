# -*- encoding: utf-8 -*-
#################################################################################
#    Autor: Mikel Martin (mikel@zhenit.com)
#    Copyright (C) 2012 ZhenIT Software (<http://ZhenIT.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#################################################################################
{
    'name': 'Invoice Merge',
    'version': '1.0',
    'category': 'Accounting Modules',
    'description': '''
        Merge draft invoices from the same partner
    ''',
    'author': 'Mikel Martin (http://ZhenIT.com)',
    'depends': ['base', 'account', 'picking_invoice_relation'],
    'data': [
        'wizard/invoice_merge_view.xml',
        'invoice_merge.xml',
    ],
    'installable': True,
    'application': True,
}
