from odoo import fields, models, api


class Driver(models.Model):
    _inherit = 'hr.employee'
    _name = 'x_driver'
    _description = 'Vehicle Driver'

    x_license_type = fields.Char(string='License type')
    x_license_exp = fields.Date(string='License expiration date')

    # to be able to use name attribute
    category_ids = fields.Many2many(
        'hr.employee.category', 'driver_category_rel', 'driver_id', 'category_id', string='Tags')
