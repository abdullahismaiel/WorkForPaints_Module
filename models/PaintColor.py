from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'paint.color'
    name = fields.Char()
    unit_cost=fields.Float('Unit Cost Of One Meter Square')