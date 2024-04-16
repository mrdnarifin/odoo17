# -*- coding: utf-8 -*-

from odoo import models, fields


class Classification(models.Model):
    _name = "hr.classification"
    _description = "Job Classification"

    name = fields.Char()
    description = fields.Text()
