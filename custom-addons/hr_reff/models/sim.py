# -*- coding: utf-8 -*-

from odoo import models, fields


class Sim(models.Model):
    _name = "hr.employee.sim"
    _description = "Jenis SIM"

    employee_id = fields.Many2one("hr.employee", string="Employee", required=True)

    jenis_sim = fields.Selection(
        string="Jenis SIM",
        required=True,
        selection=[
            ("A", "A"),
            ("B1", "B1"),
            ("B2", "B2"),
            ("C", "C"),
            ("D", "D"),
            ("A Umum", "A Umum"),
            ("B1 Umum", "B1 Umum"),
            ("B2 Umum", "B2 Umum"),
        ],
    )

    no_sim = fields.Char(string="Nomor SIM", required=True)
    tgl_berlaku = fields.Date(string="Tanggal Berlaku", required=True)
    tgl_berakhir = fields.Date(string="Tanggal Berakhir", required=True)
    tempat_terbit = fields.Char(string="Di Terbitkan di?", required=False)
