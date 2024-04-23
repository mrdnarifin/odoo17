# -*- coding: utf-8 -*-

from odoo import models, fields


class CostCenter(models.Model):
    _name = "hr.cost_center"
    _description = "Cost Center"

    name = fields.Char()
    description = fields.Text()
