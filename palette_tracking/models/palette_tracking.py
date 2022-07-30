##############################################################################
from odoo import fields, models ,api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class PaletteTracking(models.Model):
    _name = 'palette.tracking'
    _rec_name = 'picking_id'
    _description = 'Palette Tracking'

    @api.depends('palette_count_plus', 'palette_count_minus')
    def _compute_palette_balance(self):
        for res in self:
            palette_balance = 0.0
            if res.palette_count_plus and res.palette_count_minus:
                palette_balance = res.palette_count_plus - res.palette_count_minus
            res.palette_balance = palette_balance

    picking_id = fields.Many2one('stock.picking', string='Picking')
    partner_id = fields.Many2one('res.partner', string='Partner')
    license_plate = fields.Char(string='License Plate')
    picking_partner_id = fields.Many2one('res.partner', string='Picking Partner')
    picking_date_done  = fields.Datetime(string='Picking Date Done')  
    palette_count_plus = fields.Integer(string='Palette Count Plus', required=True)
    palette_count_minus = fields.Integer(string='Palette Count Minus', required=True)
    palette_balance = fields.Integer(compute='_compute_palette_balance', string='Palette Balance')


    @api.onchange('picking_id')
    def onchange_picking_id(self):
        if self.picking_id:
            self.picking_partner_id = self.picking_id.partner_id.id
            self.picking_date_done = self.picking_id.date_done