from odoo import fields, models, api,_


class PaintRoom(models.Model):
    _name = 'paint.room'
    house_id = fields.Many2one('paint.house')
    num_of_walls = fields.Integer(string='Number Of Walls')
    total_area_of_walls = fields.Float(computed='_cal_total_area', store=True)
    # walls_ids = fields.One2many('paint.wall', 'room_id', string='Walls')
    name = fields.Char()
    ref = fields.Char('House Sequence', readonly=True, required=True, default=lambda self: _('New'), store=True)
    total_cost = fields.Float(string='Total Cost Of Room', computed='_cal_total_cost')
    # if vals.get('reference', _('New')) == _('New'):
    #     # vals['reference'] = vals.get('house_ref')
    #     # print(self.env['house.house'].browse(vals.get('house_id')).reference)
    #     vals['reference'] = self.env['house.house'].browse(vals.get('house_id')).reference
    #     vals['reference'] += '.'
    #     vals['reference'] += self.env['ir.sequence'].next_by_code('room.seq') or _('New')
    #     res = super(Room, self).create(vals)
    #     return res
    @api.model
    def create(self, vals_list):
        # House Name.Number
        if vals_list.get('ref', _('New')) == _('New'):
            house_id = vals_list.get('house_id')
            house_name = self.env['paint.house'].browse(house_id).ref
            vals_list['ref'] = house_name
            vals_list['ref'] += '.'
            vals_list['ref'] += self.env['ir.sequence'].next_by_code('room.seq') or _('New')
        result = super(PaintRoom, self).create(vals_list)
        return result

    # @api.depends('walls_ids.area', 'num_of_walls')
    # def _cal_total_area(self):
    #     for room in self:
    #         if room.walls_ids and room.num_of_walls:
    #             room.total_area_of_walls = room.walls_ids * room.num_of_walls
    #         else:
    #             room.total_area_of_walls = 0.0
    #
    # @api.depends('total_area_of_walls', 'walls_ids.total_cost')
    # def _cal_total_cost(self):
    #     for room in self:
    #         if room.total_area_of_walls and room.walls_ids:
    #             room.total_cost = room.total_area_of_walls * room.walls_ids
    #         else:
    #             room.total_cost = 0.0
