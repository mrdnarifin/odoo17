# -*- coding: utf-8 -*-

from odoo import models, fields


class EmployeeStatus(models.Model):
    _name = "hr.employee_status"
    _description = "Employee Status"

    seq = fields.Char(string="Sequence")
    name = fields.Char()
    description = fields.Text()
