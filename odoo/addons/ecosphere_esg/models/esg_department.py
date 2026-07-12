from odoo import models, fields, api

class EsgDepartment(models.Model):
    _name = 'esg.department'
    _description = 'ESG Department'

    name = fields.Char(string='Department Name', required=True)
    code = fields.Char(string='Code')
    head = fields.Char(string='Department Head')
    employee_count = fields.Integer(string='Employee Count')
    active = fields.Boolean(string='Active', default=True)

    carbon_transaction_ids = fields.One2many('esg.carbon.transaction', 'department_id', string='Carbon Transactions')
    total_emissions = fields.Float(string='Total Emissions (kg CO2)', compute='_compute_total_emissions', store=True)
    environment_score = fields.Float(string="Environment Score", compute="_compute_esg_scores", store=True)
    social_score = fields.Float(string="Social Score", compute="_compute_esg_scores", store=True)
    governance_score = fields.Float(string="Governance Score", compute="_compute_esg_scores", store=True)
    esg_score = fields.Float(string="Overall ESG Score", compute="_compute_esg_scores", store=True)

    @api.depends('carbon_transaction_ids.emission_amount')
    def _compute_total_emissions(self):
            for department in self:
                department.total_emissions = sum(department.carbon_transaction_ids.mapped('emission_amount'))

    @api.depends('total_emissions')
    def _compute_esg_scores(self):
            for dept in self:
                max_emission_baseline = 500.0
            emissions = dept.total_emissions or 0.0
            env_score = max(0.0, 100.0 - (emissions / max_emission_baseline * 100.0))

            social_score = 100.0
            if 'esg.csr.activity' in self.env:
                activities = self.env['esg.csr.activity'].search([('department_id', '=', dept.id)])
                total_hours = sum(activities.mapped('hours_contributed'))
                social_score = min(100.0, total_hours * 2)

            gov_score = 100.0
            if 'esg.compliance.issue' in self.env:
                issues = self.env['esg.compliance.issue'].search([('department_id', '=', dept.id)])
                open_issues = issues.filtered(lambda i: i.status == 'open')
                total_issues = len(issues) or 1
                gov_score = max(0.0, 100.0 - (len(open_issues) / total_issues * 100.0))

            dept.environment_score = round(env_score, 2)
            dept.social_score = round(social_score, 2)
            dept.governance_score = round(gov_score, 2)
            dept.esg_score = round((env_score + social_score + gov_score) / 3, 2)