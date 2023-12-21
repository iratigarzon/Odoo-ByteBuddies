from odoo import models, fields

class User(models.Model):
    _inherit = 'res.users'
    _name = "bytebuddies.user"

    date_init = fields.Date(string="Date Init")
    user_type = fields.Selection(
        string="User Type",
        selection=[("TEACHER", "Teacher"), ("STUDENT", "Student")]
    )

