from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, default="Unkown")
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=fields.Datetime.today())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    amount = fields.Float()
    total = fields.Float(compute="_compute_total")
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    partner_id = fields.Many2one("res.partner", string="Partner")
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    user_id = fields.Many2one(
        "res.users",
        string="Salesperson",
        index=True,
        tracking=True,
        default=lambda self: self.env.user,
    )

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    garden_orientation = fields.Selection(
        string="Type",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
    )
    state = fields.Selection(
        string="Status",
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        default="new",
    )

    @api.depends("amount")
    def _compute_total(self):
        for record in self:
            record.total = 1.8 * record.amount
