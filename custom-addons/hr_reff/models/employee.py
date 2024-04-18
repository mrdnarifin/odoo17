from odoo import models, fields, api


class HrEmployeePrivate(models.Model):
    _inherit = ["hr.employee"]

    nik = fields.Char(
        string="NIK",
        required=False,
    )
    nik_ktp = fields.Char(
        string="NIK KTP",
        required=False,
    )
    family_ids = fields.Many2many("hr.family", "id")
    npwp = fields.Char(string="NPWP", required=False)
    tgl_npwp = fields.Date(string="Tgl NPWP", required=False)
    tgl_expired_npwp = fields.Date(string="Tgl Expired NPWP", required=False)
    no_bpjs = fields.Char(string="No. BPJS", required=False)
    no_bpjstk = fields.Char(string="No. BPJS TK", required=False)
    place_of_hire = fields.Char(string="Place of Hire", required=False)
    point_of_origin = fields.Char(string="Point of Origin", required=False)
    gol_darah = fields.Selection(
        string="Gol Darah",
        selection=[
            ("A", "A"),
            ("A+", "A+"),
            ("B", "B"),
            ("B+", "B+"),
            ("AB", "AB"),
            ("O", "O"),
            ("O+", "O+"),
        ],
    )
    agama = fields.Selection(
        string="Agama",
        selection=[
            ("ISLAM", "ISLAM"),
            ("KHATOLIK", "KHATOLIK"),
            ("KRISTEN", "KRISTEN"),
            ("PROTESTAN", "PROTESTAN"),
            ("HINDU", "HINDU"),
            ("TIDAK MENYEBUTKAN", "TIDAK MENYEBUTKAN"),
        ],
    )
    berat_badan = fields.Char(string="Berat Badan", required=False)
    tinggi_badan = fields.Char(string="Tinggi Badan", required=False)
    uk_baju = fields.Selection(
        string="Ukuran Baju",
        selection=[
            ("S", "S"),
            ("M", "M"),
            ("L", "L"),
            ("XL", "XL"),
            ("XXL", "XXL"),
            ("XXXL", "XXXL"),
        ],
    )

    sizes = []

    for i in range(20, 41):
        sizes.append(["{}".format(i), "{}".format(i)])

    uk_celana = fields.Selection(string="Ukuran Celana", selection=sizes)
    uk_sepatu = fields.Selection(
        string="Ukuran Sepatu",
        selection=[
            ("4.5", "4.5"),
            ("5", "5"),
            ("5.5", "5.5"),
            ("6", "6"),
            ("6.5", "6.5"),
            ("7", "7"),
            ("7.5", "7.5"),
            ("8", "8"),
            ("8.5", "8.5"),
            ("9", "9"),
            ("9.5", "9.5"),
            ("10", "10"),
            ("10.5", "10.5"),
            ("11", "11"),
            ("11.5", "11.5"),
            ("12", "12"),
            ("12.5", "12.5"),
            ("13", "13"),
        ],
    )

    no_kk = fields.Char(string="No. KK", required=False)
    tgl_terbit_kk = fields.Date(string="Tgl Terbit KK", required=False)
    tgl_terbit_ktp = fields.Date(string="Tgl Terbit KTP", required=False)
    tgl_expired_ktp = fields.Date(string="Tgl Expired KTP", required=False)
    tiktok = fields.Char(string="Tiktok", required=False)
    instagram = fields.Char(string="Instagram", required=False)
    twitter = fields.Char(string="Twitter", required=False)
    linkedin = fields.Char(string="Linkedin", required=False)
