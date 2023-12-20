from odoo import models, api, fields


class User(models.Model):
    _name = "bytebuddies.user"
    # _inherit = 'res.users'

    id = fields.Integer()
    email = fields.Char()
    name = fields.Char()
    surname = fields.Char()
    # password (encrypt)
    dateInit = fields.Date(string="dateInit")
    userType = fields.Selection(string="userType", selection=[("TEACHER", "Teacher"), ("STUDENT", "Student")])




