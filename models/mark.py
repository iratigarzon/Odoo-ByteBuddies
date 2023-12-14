from odoo import fields

class Mark:
    # Id
    value = fields.Float()
    type = fields.Selection(selection_add=[('FIRST', 'First'), ('SECOND', 'Second'),
                                           ('THIRD', 'Third'), ('FOURTH', 'Fourth'), ('FIFTH', 'Fifth')])
    # exam = fields.Exam()
    # student = fields.Student()
    solutionFilePath = fields.Char()
    comment = fields.Char()