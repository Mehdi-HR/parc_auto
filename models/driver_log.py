# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DriverLog(models.Model):
    _name = "x_driver_log"
    _description = "Driver Log"

    x_start_date = fields.Date(string='Start date')
    x_end_date = fields.Date(string='End date')

    x_driver_id = fields.Many2one(comodel_name='x_driver', string='Driver')
    x_vehicle_id = fields.Many2one(comodel_name='x_vehicle', string='Vehicle')


