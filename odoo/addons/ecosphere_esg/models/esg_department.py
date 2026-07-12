from odoo import models, fields

class EsgDepartment(models.Model):
    _name = 'esg.department'
    _description = 'ESG Department'

    name = fields.Char(string='Department Name', required=True)
    code = fields.Char(string='Code')
    head = fields.Char(string='Department Head')
    employee_count = fields.Integer(string='Employee Count')
    active = fields.Boolean(string='Active', default=True)
    