from datetime import date

from odoo import fields, models, api, _


class PaintHouse(models.Model):
    _name = 'paint.house'
    name = fields.Char()
    house_Owner = fields.Many2one('res.partner')
    ref = fields.Char('House Sequence', readonly=True, required=True, default=lambda self: _('New'), store=True)

    @api.model
    def create(self, vals_list):
        if vals_list.get('ref', _('New')) == _('New'):
            owner_id = vals_list.get('house_Owner')
            owner_name = self.env['res.partner'].browse(owner_id).name
            vals_list['ref'] = str(date.today().year)
            vals_list['ref'] += '/'
            vals_list['ref'] += owner_name
            vals_list['ref'] += '/'
            vals_list['ref'] += self.env['ir.sequence'].next_by_code('house.seq') or _('New')
        result = super(PaintHouse, self).create(vals_list)
        return result
