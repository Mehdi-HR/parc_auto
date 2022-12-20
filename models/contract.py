from odoo import fields, models, api


class Contract(models.Model):
    _inherit = 'fleet.vehicle.log.contract'
    _name = 'x_contract'
    _description = 'Vehicle Contract'

    x_lessor_id = fields.Many2one(comodel_name='x_lessor', string='Lessor')

    #to be able to use name attribute
    #channel_ids = fields.Many2many('mail.channel', 'mail_channel_profile_partner', 'partner_id', 'channel_id', copy=False)