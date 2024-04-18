from odoo import fields, models, api


class Family(models.Model):
    _name = "hr.family"
    _description = "Family of an employee"

    # emp_id = fields.Many2one("hr.employee", string="Employee")
    name = fields.Char(string="Nama Lengkap", required=True)
    nik = fields.Char(string="NIK KTP", required=False)

    relation = fields.Selection(
        string="Hubungan",
        selection=[
            ["SUAMI/ISTRI", "SUAMI/ISTRI"],
            ["ANAK 1", "ANAK 1"],
            ["ANAK 2", "ANAK 2"],
            ["ANAK 3", "ANAK 3"],
            ["ANAK 4", "ANAK 4"],
            ["ANAK 5", "ANAK 5"],
            ["ANAK 6", "ANAK 6"],
            ["ANAK 7", "ANAK 7"],
            ["ANAK 8", "ANAK 8"],
            ["ANAK 9", "ANAK 9"],
            ["ANAK 10", "ANAK 10"],
            ["IBU KANDUNG", "IBU KANDUNG"],
            ["AYAH KANDUNG", "AYAH KANDUNG"],
            ["IBU MERTUA", "IBU MERTUA"],
            ["AYAH MERTUA", "AYAH MERTUA"],
            ["SAUDARA", "SAUDARA"],
        ],
    )

    address = fields.Text(string="Alamat", required=False)
    rt = fields.Char(string="RT", required=False)
    rw = fields.Char(string="RW", required=False)
    no_bpjs = fields.Char(string="No. BPJS", required=True)
    kode_faskes1 = fields.Char(string="Kode Faskes 1", required=True)
    faskes1 = fields.Char(string="Faskes 1", required=True)
    kelas_rawat = fields.Char(string="Kelas Rawat", required=True)
    kode_faskes_gigi = fields.Char(string="Kode Faskes Dokter Gigi", required=False)
    faskes_gigi = fields.Char(string="Faskes Dokter Gigi", required=False)
    country_id = fields.Many2one(
        "res.country", string="Country", groups="hr.group_hr_user"
    )
    postal_code = fields.Char(string="Postal Code", required=False)
    phone = fields.Char(string="Phone", required=False)
    birthdate = fields.Date(string="Birthdate", required=False)
    deathdate = fields.Date(string="Deathdate", required=False)
    gender = fields.Selection(
        string="Gender",
        required=False,
        selection=[
            ("L", "Laki-laki"),
            ("P", "Perempuan"),
            ("U", "Unknown"),
        ],
    )
    MARITAL_TYPE = [
        ("KAWIN", "KAWIN"),
        ("BELUM KAWIN", "BELUM KAWIN"),
        ("DUDA", "DUDA"),
        ("JANDA", "JANDA"),
    ]
    marital_status = fields.Selection(
        string="Marital Status", required=False, selection=MARITAL_TYPE
    )
    marital_date = fields.Date(string="Marital Date", required=False)
    an_employee = fields.Boolean(string="An Employee", required=True, default=False)
    unit_usaha = fields.Char(string="Unit Usaha", required=False)
    nik_emp = fields.Char(string="NIK Employee", required=False)
    active = fields.Boolean(string="Active", required=True, default=True)
