from odoo import fields

class Exam(models.Model):
    _name = "bytebuddies.exam"

    id = fields.Integer()
    description = fields.Char()
    filePath = fields.Char()
    duration = fields.Integer()
    # Marks ?? collection??
    date = fields.Date()
    # subject = fields.Subject()