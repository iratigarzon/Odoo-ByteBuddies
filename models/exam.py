from odoo import fields, models, api


class Exam(models.Model):
    _name = "bytebuddies.exam"

    description = fields.Char()
    dateInit = fields.Date(string="dateInit")
    duration = fields.Integer()
    filePath = fields.Char()
    subject_id = fields.Many2one('bytebuddies.subject', string="Subject")
    mark = fields.One2many(comodel_name='bytebuddies.mark', inverse_name='exam_id', ondelete='cascade', string="Mark")

