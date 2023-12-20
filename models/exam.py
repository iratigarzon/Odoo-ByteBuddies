from odoo import fields, models, api


class Exam(models.Model):
    _name = "bytebuddies.exam"

    id = fields.Integer()
    description = fields.Char()
    dateInit = fields.Date(string="dateInit")
    duration = fields.Integer()
    filePath = fields.Char()
    subject_id = fields.Many2one('bytebuddies.subject', string="Subject")
    mark = fields.One2many('bytebuddies.mark', 'exam_id', ondelete='cascade', string="Mark")

