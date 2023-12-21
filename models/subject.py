from odoo import models, api, fields

class Subject(models.Model):
    _name = "bytebuddies.subject"

    id = fields.Integer("id")
    name = fields.Char(string="Name")
    hours = fields.Integer(string="hours")
    levelType = fields.Selection(string="levelType", selection=[("BEGGINER", "Beginner"), ("MEDIUM", "Medium"),
                                                                ("EXPERIENCED", "Experienced")])
    languageType = fields.Selection(string="languageType", selection=[("ENGLISH", "English"), ("SPANISH", "Spanish"),
                                                                ("BASQUE", "Basque")])

    dateInit = fields.Date(string="dateInit")
    dateEnd = fields.Date(string="dateEnd")
    teacher = fields.Many2one('bytebuddies.teacher', 'subject', string='Teacher')
    enrollments = fields.One2many('bytebuddies.enrolled', 'subject', string='Enrollments')
    exams = fields.One2many('bytebuddies.exam', 'subject', string='Exams')


