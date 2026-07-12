from odoo import models, fields

class ESGBadge(models.Model):
    _name = 'esg.badge'
    _description = 'ESG Achievement Badge'

    name = fields.Char(string="Badge Name", required=True)
    description = fields.Text(string="Description")
    unlock_rule = fields.Selection([
        ('xp_count', 'Total XP Reached'),
        ('challenge_count', 'Challenges Completed')
    ], string="Unlock Rule", required=True)
    rule_value = fields.Integer(string="Target Value Required") 
    icon = fields.Binary(string="Badge Icon")

class ESGReward(models.Model):
    _name = 'esg.reward'
    _description = 'ESG Redeemable Reward'

    name = fields.Char(string="Reward Name", required=True)
    description = fields.Text(string="Description")
    points_required = fields.Integer(string="Points Required", default=0)
    stock_status = fields.Selection([
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock')
    ], string="Stock Status", default='in_stock')