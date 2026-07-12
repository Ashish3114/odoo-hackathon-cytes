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

    @api.depends('carbon_transaction_ids.emission_amount')
    def _compute_total_emissions(self):
        for department in self:
            department.total_emissions = sum(department.carbon_transaction_ids.mapped('emission_amount'))