from odoo import fields, models, api


class Mark(models.Model):
    _name = "bytebuddies.mark"

    exam_id = fields.Many2one('bytebuddies.exam', string="Exam")
    student_id = fields.Many2one('bytebuddies.student', string="Student")
    value = fields.Float(string="Value")
    callType = fields.Selection(string="CallType",
                                selection=[('FIRST', 'First'), ('SECOND', 'Second'), ('THIRD', 'Third'),
                                           ('FOURTH', 'Fourth'), ('FIFTH', 'Fifth')])
    solutionFilePath = fields.Char(string="Solution file path")
    comment = fields.Char(string="Comment")
