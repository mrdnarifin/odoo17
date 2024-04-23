# -*- coding: utf-8 -*-

from odoo import models, fields


class Grade(models.Model):
    _name = "hr.grade"
    _description = "Job Grade"

    name = fields.Char()
    description = fields.Text()
