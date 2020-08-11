# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.tools import float_compare, pycompat
from odoo.exceptions import ValidationError
from odoo.osv import expression

from odoo.addons import decimal_precision as dp



class Locataire_potenciel(models.Model):
    _inherit = 'res.partner'

    quartier_souhaitee = fields.Many2one('lb.quartier', string="Quartier souhaité")
    budget = fields.Float(string="Budget", default=0.0, digits=dp.get_precision('Budget'))
    #type_id = fields.Many2one('lb.type', string="Type Biens souhaitee")
    active_potenctiel = fields.Boolean('Peut étre un locataire potenciel', default=False)