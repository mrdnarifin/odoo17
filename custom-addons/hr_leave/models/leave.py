from odoo import models, fields, api


class HolidaysRequest(models.Model):
    _inherit = ["hr.leave"]

    facility = fields.Selection(
        string="Facility",
        required=False,
        selection=[
            ["TIKET PESAWAT & TRAVEL", "TIKET PESAWAT & TRAVEL"],
            ["TIKET PESAWAT", "TIKET PESAWAT"],
            ["TRAVEL", "TRAVEL"],
        ],
    )
