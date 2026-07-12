from odoo import models, fields, api


class EsgComplianceIssue(models.Model):
    _name = 'esg.compliance.issue'
    _description = 'ESG Compliance Issue'

    name = fields.Char(string='Issue Title', required=True)
    department_id = fields.Many2one('esg.department', string='Department', required=True)
    severity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Severity', default='medium', required=True)
    status = fields.Selection([
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ], string='Status', default='open', required=True)
    date_reported = fields.Date(string='Date Reported', default=fields.Date.context_today)
    resolved_by = fields.Char(string='Resolved By')
    description = fields.Text(string='Description')

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records.department_id._compute_esg_scores()
        return records

    def write(self, vals):
        result = super().write(vals)
        self.department_id._compute_esg_scores()
        return result