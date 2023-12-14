from odoo import models, api, fields

class User(models.Model):
    _name = "bytebuddies.user"
    _inherit = 'res.users'

    dateInit = fields.date(string="dateInit")
    userType = fields.Selection(string="userType", selection=[("TEACHER", "Teacher"), ("STUDENT", "Student")])