from odoo import models, fields, api, exceptions

class Subject(models.Model):
    _name = "bytebuddies.subject"

    name = fields.Char(string="Name")
    hours = fields.Integer(string="Hours")
    levelType = fields.Selection(string="Level Type", selection=[("BEGINNER", "Beginner"), ("MEDIUM", "Medium"),
                                                                ("EXPERIENCED", "Experienced")])
    languageType = fields.Selection(string="Language Type", selection=[("ENGLISH", "English"), ("SPANISH", "Spanish"),
                                                                      ("BASQUE", "Basque")])

    dateInit = fields.Date(string="Date Init")
    dateEnd = fields.Date(string="Date End")
    teachers = fields.Many2many('bytebuddies.teacher', string='Teachers')
    students = fields.Many2many('bytebuddies.student', string='Students')
    exams = fields.One2many('bytebuddies.exam', 'subject_id', string='Exams')

    @api.constrains('name')
    def _check_unique_subject_name(self):
        for subject in self:
            if subject.name:
                existing_subjects = self.env['bytebuddies.subject'].search([('name', '=', subject.name)])
                if len(existing_subjects) > 1 or (len(existing_subjects) == 1 and existing_subjects[0] != subject):
                    raise exceptions.ValidationError("Subject with the same name already exists.")
    @api.constrains('dateInit')
    def _constrains_dateInit(self):
        for subject in self:
            if subject.dateInit and subject.dateEnd and subject.dateInit > subject.dateEnd:
                raise exceptions.ValidationError("Date Init cannot be greater than Date End.")

    @api.constrains('dateEnd')
    def _constrains_dateEnd(self):
        for subject in self:
            if subject.dateInit and subject.dateEnd and subject.dateEnd < subject.dateInit:
                raise exceptions.ValidationError("Date End cannot be smaller than Date Init.")

    def copy(self, default=None):
        if default is None:
            default = {}

        default.update({
            'name': ''
        })

        result = super(Subject, self).copy(default)
        return result