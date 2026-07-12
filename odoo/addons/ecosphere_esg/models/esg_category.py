from odoo import models, fields


class ESGCategory(models.Model):
    _name = 'esg.category'
    _description = 'ESG Category'

    name = fields.Char(
        string="Category Name",
        required=True
    )

    type = fields.Selection(
        [
            ('csr', 'CSR Activity'),
            ('challenge', 'Challenge')
        ],
        string="Category Type",
        required=True
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )