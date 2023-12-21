from odoo import models, api, fields

class Student(models.Model):
    _name = "bytebuddies.student"
   # _inherit = 'bytebuddies.user'

    level_type = fields.Selection(
        string="Level Type",
        selection=[
            ("BEGINNER", "Beginner"),
            ("MEDIUM", "Medium"),
            ("EXPERIENCED", "Experienced")
        ]
    )