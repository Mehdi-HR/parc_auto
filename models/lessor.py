from odoo import fields, models, api


class Lessor(models.Model):
    _inherit = 'res.partner'
    _name = 'x_lessor'
    _description = 'Vehicle Lessor'

    x_city_id = fields.Many2one(comodel_name='x_city', string='City')

    #to be able to use name attribute
    channel_ids = fields.Many2many('mail.channel', 'mail_channel_profile_partner', 'partner_id', 'channel_id', copy=False)