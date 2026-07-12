from odoo import models, fields, api


class EsgCsrActivity(models.Model):
    _name = 'esg.csr.activity'
    _description = 'ESG CSR Activity'

    name = fields.Char(string='Activity Name', required=True)
    department_id = fields.Many2one('esg.department', string='Department', required=True)
    category = fields.Selection([
        ('plantation', 'Plantation'),
        ('education', 'Education'),
        ('health', 'Health'),
        ('community', 'Community Service'),
        ('other', 'Other'),
    ], string='Category', default='other', required=True)
    activity_date = fields.Date(string='Activity Date', default=fields.Date.context_today)
    participants = fields.Integer(string='Number of Participants', default=1)
    hours_contributed = fields.Float(string='Hours Contributed')
    description = fields.Text(string='Description')