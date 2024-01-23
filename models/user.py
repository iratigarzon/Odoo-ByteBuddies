from odoo import models, fields, api, exceptions


class User(models.Model):
    _name = "bytebuddies.user"

    email = fields.Char()
    name = fields.Char()
    surname = fields.Char()
    password = fields.Char(string="Password", groups="your_module.group_admin")

    @api.constrains('name')
    def _check_valid_name(self):
        for user in self:
            if user.name and not user.name.isalpha():
                raise exceptions.ValidationError("El nombre solo puede contener letras.")

    @api.constrains('surname')
    def _check_valid_surname(self):
        for user in self:
            if user.surname and not user.surname.isalpha():
                raise exceptions.ValidationError("El apellido solo puede contener letras.")


