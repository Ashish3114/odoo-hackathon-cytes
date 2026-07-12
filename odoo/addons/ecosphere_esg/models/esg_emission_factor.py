from odoo import models, fields

class ESGEmissionFactor(models.Model):
    _name = 'esg.emission.factor'
    _description = 'ESG Emission Factor'

    name = fields.Char(string="Activity/Source Name", required=True) # e.g., "Diesel Fleet Delivery"
    factor_value = fields.Float(string="Carbon Factor Value", required=True) # Co2 per unit
    unit = fields.Selection([
        ('km', 'Kilometers'),
        ('kwh', 'Kilowatt Hours'),
        ('liters', 'Liters'),
    ], string="Unit of Measure", required=True)
    active = fields.Boolean(default=True)