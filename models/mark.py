from odoo import fields, models, api


class Mark(models.Model):
    _name = "bytebuddies.mark"

    # Id
    value = fields.Float(string = "Value")
    type = fields.Selection(string = "CallType", selection=[('FIRST', 'First'), ('SECOND', 'Second'), ('THIRD', 'Third'), ('FOURTH', 'Fourth'), ('FIFTH', 'Fifth')])
    # exam = fields.Exam()
    # student = fields.Student()
    solutionFilePath = fields.Char(string = "Solution file path")
    comment = fields.Char(string = "Comment")
