from odoo import fields


class Mark(models.Model):
    _name = "bytebuddies.mark"

    # Id
    value = fields.Float()
    type = fields.Selection(selection_add=[('FIRST', 'First'), ('SECOND', 'Second'),
                                           ('THIRD', 'Third'), ('FOURTH', 'Fourth'), ('FIFTH', 'Fifth')])
    # exam = fields.Exam()
    # student = fields.Student()
    solutionFilePath = fields.Char()
    comment = fields.Char()
