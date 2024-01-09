from odoo import models, api, fields

class Enrolled(models.Model):
    _name = "bytebuddies.enrolled"

    subject = fields.Many2one('bytebuddies.subject',string='Subject', required=True,ondelete='cascade')

    student = fields.Many2one('bytebuddies.student', string='Student',required=True,ondelete='cascade')