# -*- coding: utf-8 -*-

from odoo import models, fields


class EmployeeType(models.Model):
    _name = "hr.employee_type"
    _description = "Employee Status"

    seq = fields.Char(string="Sequence")
    name = fields.Char()
    description = fields.Text()
