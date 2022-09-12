from odoo import fields, models, api


class PaintWall(models.Model):
    _name = 'paint.wall'
    assigned_painter = fields.Many2one("res.users", string='Assigned Painter')
    length = fields.Float(string='Wall Length')
    width = fields.Float(string='Wall Width')
    area = fields.Float(compute='_calArea', store=True, readonly=True)
    room_id = fields.Many2one('paint.room', string='room')
    total_cost = fields.Float(string='Total Cost $', compute='_cal_total_cost',store=True,readonly=True)
    color_id = fields.Many2one('paint.color')
    unit_cost=fields.Float(related='color_id.unit_cost')

    @api.depends('length', 'width')
    def _calArea(self):
        for wall in self:
            if wall.length and wall.width:
                wall.area = wall.length * wall.width
            else:
                wall.area = 0.0

    @api.depends('area')
    def _cal_total_cost(self):
        for wall in self:
            if wall.area:
                wall.total_cost = wall.area * wall.unit_cost
            else:
                wall.total_cost = 0.0
