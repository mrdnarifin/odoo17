# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrAttendance(models.Model):

    _inherit = "hr.attendance"

    overtime_fix_hours = fields.Float(
        string="OT Fix Hours",
        compute="_compute_overtime_fix_hours",
        store=True,
    )

    overtime_shift_hours = fields.Float(
        string="OT Shift Hours",
    )

    ot_total_hours = fields.Float(
        string="OT Total Hours",
        compute="_compute_ot_total_hours",
        store=True,
    )

    @api.depends("overtime_hours")
    def _compute_overtime_fix_hours(self):
        for record in self:
            print(record.check_in, "JONI")
            record.overtime_fix_hours = float(5.5)

    @api.depends("worked_hours")
    def _compute_ot_total_hours(self):
        if self.ids:
            for record in self:
                record.ot_total_hours = (
                    record.overtime_fix_hours + record.overtime_shift_hours
                )
