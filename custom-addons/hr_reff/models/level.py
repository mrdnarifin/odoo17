# -*- coding: utf-8 -*-

from odoo import models, fields


class Level(models.Model):
    _name = "hr.level"
    _description = "Job Level"

    name = fields.Char()
    description = fields.Text()
