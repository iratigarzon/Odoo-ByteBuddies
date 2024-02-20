from odoo import models, fields, api, exceptions
from datetime import datetime

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
    image = fields.Binary(string='Image')
    state_subject = fields.Selection(string="Subject state",  selection=[("ACTIVE", "Active"), ("INACTIVE", "Inactive")])
    date_inactive = fields.Datetime(
        string="Date Inactive",
        readonly=True
    )

    @api.onchange('state_subject')
    def _onchange_state_subject(self):
        if self.state_subject == 'INACTIVE':
            self.update({'date_inactive': fields.Datetime.now()})
        else:
            self.update({'date_inactive': False})
    @api.constrains('name')
    def _check_unique_subject_name(self):
        for subject in self:
            if subject.name:
                existing_subjects = self.env['bytebuddies.subject'].search([('name', '=', subject.name)])
                if len(existing_subjects) > 1 or (len(existing_subjects) == 1 and existing_subjects[0] != subject):
                    raise exceptions.ValidationError("Existe una asignatura con el mismo nombre")
    @api.constrains('dateInit')
    def _constrains_dateInit(self):
        for subject in self:
            if subject.dateInit and subject.dateEnd and subject.dateInit > subject.dateEnd:
                raise exceptions.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")

    @api.constrains('name')
    def _check_valid_name(self):
        for record in self:
            if record.name and not all(char.isalpha() or char.isspace() for char in record.name):
                raise exceptions.ValidationError("El nombre solo puede contener letras y espacios.")

    @api.constrains('dateEnd')
    def _check_null_dateInit(self):
        for subject in self:
            if not subject.dateInit:
                raise exceptions.ValidationError("La fecha de inicio no puede estar vacía.")



    def copy(self, default=None):
        if default is None:
            default = {}

        default.update({
            'name': 'Copia de ' + self.name,
            'image': False,
            'date_inactive': False
        })

        result = super(Subject, self).copy(default)
        return result


