from odoo import models, api, fields


class Student(models.Model):
    _name = 'bytebuddies.student'
    _inherit = "bytebuddies.user"

    levelType = fields.Selection(string="levelType", selection=[("BEGGINER", "Beginner"), ("MEDIUM", "Medium"),
                                                                ("EXPERIENCED", "Experienced")])
    mark = fields.One2many('bytebuddies.mark', 'student_id', ondelete='cascade', string="mark")
    subjects = fields.Many2many('bytebuddies.subject', 'student_subject_rel', 'student_id', 'subject_id',
                                string="Subjects", ondelete='cascade')

