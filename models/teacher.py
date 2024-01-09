from odoo import models, api, fields


class Teacher(models.Model):
    _name = "bytebuddies.teacher"
    _inherit = "bytebuddies.user"

    studiesType = fields.Selection(string="Studies Type",
                                   selection=[("HIGHER LEVEL TRAINING CYCLES", "Higher level training cycles"),
                                              ("UNIVERSITY DEGREE", "University Degree"),
                                              ("MASTER", "Master"), ("DOCTORATE", "Doctorate"), ("OTHER", "Other")])
    qualifications = fields.Char(string="Qualifications")
    subjects = fields.Many2many('bytebuddies.subject', 'teacher_subject_rel', 'teacher_id', 'subject_id',
                                string="Subjects", ondelete='cascade')
