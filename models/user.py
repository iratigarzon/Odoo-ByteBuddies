from odoo import models, fields


class User(models.Model):
    _name = "bytebuddies.user"
    
    email = fields.Char()
    name = fields.Char()
    surname = fields.Char()
    password = fields.Char()
    dateInit = fields.Date(string="dateInit")
    userType = fields.Selection(string="userType", selection=[("TEACHER", "Teacher"), ("STUDENT", "Student")])



