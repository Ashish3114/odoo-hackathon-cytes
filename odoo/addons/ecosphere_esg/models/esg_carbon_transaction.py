from odoo import models, fields

class EsgCarbonTransaction(models.Model):
    _name = 'esg.carbon.transaction'
    _description = 'ESG Carbon Transaction'

    name = fields.Char(string='Reference', required=True, default='New')
    department_id = fields.Many2one('esg.department', string='Department', required=True)
    category = fields.Selection([
        ('purchase', 'Purchase'),
        ('manufacturing', 'Manufacturing'),
        ('expense', 'Expense'),
        ('fleet', 'Fleet'),
    ], string='Category', required=True)
    date = fields.Date(string='Date', required=True)
    emission_amount = fields.Float(string='Emission Amount (kg CO2)')
    notes = fields.Text(string='Notes')