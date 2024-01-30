from odoo import models, api, fields, exceptions
from datetime import date;


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

    @api.constrains('name')
    def _check_unique_exam_name(self):
        for exam in self:
            if exam.name:
                existing_exams = self.env['bytebuddies.exam'].search([('name', '=', exam.name)])
                if len(existing_exams) > 1 or (len(existing_exams) == 1 and existing_exams[0] != exam):
                    raise exceptions.ValidationError("Ya existe un examen con ese nombre.")

    @api.constrains('description')
    def _check_null_description(self):
        for exam in self:
            if not exam.description:
                raise exceptions.ValidationError("El examen debe tener una descripción.")

    @api.constrains('subject_id')
    def _check_null_exam_subject_id(self):
        for exam in self:
            if not exam.subject_id:
                raise exceptions.ValidationError("El examen debe pertenecer a una asignatura.")

    @api.constrains('duration')
    def _check_null_exam_duration(self):
        for exam in self:
            if not exam.duration or exam.duration == 0:
                raise exceptions.ValidationError("La duración del examen debe ser mayor que 0.")

    @api.constrains('duration')
    def _check_long_exam_duration(self):
        for exam in self:
            if exam.duration > 4:
                raise exceptions.ValidationError("El examen no puede durar más de 4 horas.")

    @api.constrains('dateInit')
    def _constrains_exam_dateInit(self):
        for exam in self:
            if exam.dateInit <= date.today():
                raise exceptions.ValidationError("La fecha del examen no puede ser anterior o igual a la de hoy.")

    @api.constrains('name')
    def _check_valid_name(self):
        for user in self:
            if user.name and not user.name.isalpha():
                raise exceptions.ValidationError("El nombre solo puede contener letras.")

    @api.constrains('dateInit')
    def _check_null_exam_dateInit(self):
        for exam in self:
            if not exam.dateInit:
                raise exceptions.ValidationError("La fecha del examen no puede estar vacía.")

    @api.constrains('exam_id')
    def _check_null_exam(self):
        for mark in self:
            if not mark.exam_id:
                raise exceptions.ValidationError("La nota debe pertenecer a un examen.")

    @api.constrains('student_id')
    def _check_null_student(self):
        for mark in self:
            if not mark.student_id:
                raise exceptions.ValidationError("La nota debe pertenecer a un alumno.")

    @api.constrains('value')
    def _check_high_mark_value(self):
        for mark in self:
            if mark.value > 10.0:
                raise exceptions.ValidationError("El valor de la nota no puede ser superior a 10.")

    @api.constrains('callType')
    def _check_null_callType(self):
        for mark in self:
            if not mark.callType:
                raise exceptions.ValidationError("La nota debe pertenecer a un CallType (convocatoria).")

    def copy(self, default=None):
        if default is None:
            default = {}

        default.update({
            'name': ''
        })

        result = super(Exam, self).copy(default)
        return result