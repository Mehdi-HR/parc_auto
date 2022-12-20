from odoo import fields, models, api


class Driver(models.Model):
    _inherit = 'fleet.vehicle'
    _name = 'x_vehicle'
    _description = 'Vehicle'

    x_driver_id = fields.Many2one(comodel_name='x_driver', string='Driver')
    x_mrouge = fields.Boolean(string='MRouge')

    # to be able to use name attribute
    tag_ids = fields.Many2many('fleet.vehicle.tag', 'vehicle_rel', 'vehicle_id', 'tag_id', string='Tags')

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s' % rec.license_plate))
        return result;