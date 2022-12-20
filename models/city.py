# -*- coding: utf-8 -*-
from odoo import api, fields, models


class City(models.Model):
    _name = "x_city"
    _description = "City"

    x_name = fields.Char(string='Name')
    x_country_id = fields.Many2one(comodel_name='res.country', string='Country')

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s, %s' % (rec.x_name, rec.x_country_id.name)))
        return result;

