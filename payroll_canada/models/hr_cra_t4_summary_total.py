# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 Savoir-faire Linux. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

from odoo import fields, models, _
import odoo.addons.decimal_precision as dp


class HrCRAT4SummaryTotal(models.Model):
    """CRA T4 Summary Amoun"""

    _name = "hr.cra.t4.summary.total"
    _description = _(__doc__)

    summary_id = fields.Many2one(
        "hr.cra.t4.summary",
        "Summary",
        required=True,
        ondelete="cascade",
    )
    box_id = fields.Many2one(
        "hr.cra.t4.summary.box",
        "Contribution / Source Deduction",
        required=True,
    )
    amount = fields.Float(
        "Amount",
        digits_compute=dp.get_precision("Payroll"),
        required=True,
    )
