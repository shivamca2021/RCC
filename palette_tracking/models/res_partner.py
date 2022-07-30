##############################################################################
from odoo import fields, models ,api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = 'res.partner'

    def count_palatte_records(self):
        for res in self:
            palette_ids = self.env['palette.tracking'].search([('partner_id', '=', res.id)])
            if palette_ids:
                res.palette_tracking_count = len(palette_ids.ids)
            else:
                res.palette_tracking_count = 0

    palette_tracking_count = fields.Integer(compute='count_palatte_records' ,string="Palette")

    def open_palette_tracking(self):
        ctx = self.env.context.copy()
        palette_ids = self.env['palette.tracking'].search([('partner_id', '=', self.id)])
        return {
            'name': _('Palette Tracking'),
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'palette.tracking',
            'domain': [('partner_id', '=', self.id), ('id', 'in', palette_ids.ids)],
            'type': 'ir.actions.act_window',
            'target' : 'current'
        }
