from odoo import fields, models

class Client(models.Model):
    _name = 'real.estate.customer'
    _description = 'Customer'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')


class Property(models.Model):
    _name = 'real.estate.property'
    _description = 'Property'

    name = fields.Char(string='Name')
    value = fields.Char(string='Value')
    location = fields.Char(string='Location')
    property_type = fields.Char(string='Property Type')
    price = fields.Float(string='Price')
    interested_propety = fields.Many2many('real.estate.client', string='Interested Propety')


class Agent(models.Model):
    _name = 'real.estate.agent'
    _description = 'Agent'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')



