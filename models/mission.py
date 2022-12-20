# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Mission(models.Model):
    _name = "x_mission"
    _description = "Mission"

    x_name = fields.Char(string='Name')
    x_description = fields.Char(string='Description')

    x_start = fields.Datetime(string='Start')
    x_end = fields.Datetime(string='End')

    x_vehicles = fields.Many2many(comodel_name='x_vehicle', string='Vehicles')
    x_city_id = fields.Many2one(comodel_name='x_city', string='City')

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s' % rec.x_name))
        return result;