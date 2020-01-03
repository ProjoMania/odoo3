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

from . import account_report_common
from . import account_report_common_partner
from . import account_report_common_journal
from . import account_report_common_account

from . import account_automatic_reconcile
from . import account_move_line_reconcile_select
from . import account_move_line_unreconcile_select
from . import account_reconcile_partner_process
from . import account_reconcile
from . import account_unreconcile
from . import account_invoice_refund
from . import account_journal_select
from . import account_move_bank_reconcile
from . import account_subscription_generate
from . import account_report_aged_partner_balance
from . import account_report_partner_ledger
from . import account_report_partner_balance
from . import account_period_close
from . import account_fiscalyear_close
from . import account_fiscalyear_close_state
from . import account_vat
from . import account_open_closed_fiscalyear

from . import account_invoice_state
from . import account_chart
from . import account_tax_chart
from . import account_financial_report
#TODO: remove this file no moe used
# also remove related view fiel

from . import account_validate_account_move
from . import account_use_model

from . import account_state_open

from . import account_report_print_journal
from . import account_report_central_journal
from . import account_report_general_journal
from . import account_report_general_ledger
from . import account_report_account_balance

from . import account_change_currency

from . import pos_box
from . import account_statement_from_invoice
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
