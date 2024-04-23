# -*- coding: utf-8 -*-

from odoo import models, fields


class Job(models.Model):

    _inherit = "hr.job"
    cost_center = fields.Many2one("hr.cost_center", "Cost Center", required=True)
    level = fields.Many2one("hr.level", "Job Level", required=True)
    classification = fields.Many2one(
        "hr.classification", "Job Classification", required=True
    )
    section = fields.Many2one("hr.section", string="Section")
    level_hcs = fields.Char(string="Level HCS")
    grade = fields.Many2one("hr.grade", string="Job Grade", required=True)


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
