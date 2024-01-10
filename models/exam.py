from odoo import models, api, fields


class Exam(models.Model):
    _name = "bytebuddies.exam"

    id = fields.Integer("id")
    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    dateInit = fields.Date(string="dateInit")
    duration = fields.Integer(string="duration")
    filePath = fields.Char(string="File")
    subject_id = fields.Many2one('bytebuddies.subject', string="Subject")
    mark = fields.One2many(comodel_name='bytebuddies.mark', inverse_name='exam_id',
                           string="Mark")  # ondelete='cascade',