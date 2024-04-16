# -*- coding: utf-8 -*-

from odoo import models, fields


class Section(models.Model):
    _name = "hr.section"
    _description = "Section"
    _order = "name"

    name = fields.Char("Section Name", required=True, translate=True)
    complete_name = fields.Char(
        "Complete Name", compute="_compute_complete_name", recursive=True, store=True
    )
    active = fields.Boolean("Active", default=True)
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        index=True,
        default=lambda self: self.env.company,
    )
    parent_id = fields.Many2one(
        "hr.department", string="Parent Department", index=True, check_company=True
    )

    member_ids = fields.One2many(
        "hr.employee", "department_id", string="Members", readonly=True
    )
    total_employee = fields.Integer(
        compute="_compute_total_employee", string="Total Employee"
    )
    jobs_ids = fields.One2many("hr.job", "department_id", string="Jobs")
    plan_ids = fields.One2many("mail.activity.plan", "department_id")
    plans_count = fields.Integer(compute="_compute_plan_count")
    note = fields.Text("Note")
    color = fields.Integer("Color Index")
    parent_path = fields.Char(index=True, unaccent=False)
    master_department_id = fields.Many2one(
        "hr.department",
        "Master Department",
        compute="_compute_master_department_id",
        store=True,
    )

    def _compute_total_employee(self):
        emp_data = self.env["hr.employee"]._read_group(
            [("department_id", "in", self.ids)], ["department_id"], ["__count"]
        )
        result = {department.id: count for department, count in emp_data}
        for department in self:
            department.total_employee = result.get(department.id, 0)
