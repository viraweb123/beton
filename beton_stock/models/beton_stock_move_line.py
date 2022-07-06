from collections import Counter, defaultdict

from odoo import _, api, fields, tools, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import OrderedSet
from odoo.tools.float_utils import float_compare, float_is_zero, float_round


class BetonStockMoveLine(models.Model):
    _inherit = ["stock.move.line"]
    
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', readonly=False, required=False, index=True)
    driver_id = fields.Many2one('res.partner', string='Driver', readonly=False, required=False, index=True)
