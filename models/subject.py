from odoo import models, api, fields

class Subject(models.Model):
    _name = "bytebuddies.subject"

    id = fields.Integer("id")
    name = fields.Char(string="Name", required=True, help="Name of the subject")
    hours = fields.Integer(string="hours", required=True, help="Hours of the subject")
    levelType = fields.Selection(string="levelType", selection=[("BEGGINER", "Beginner"), ("MEDIUM", "Medium"),
                                                                ("EXPERIENCED", "Experienced")])
    languageType = fields.Selection(string="languageType", selection=[("ENGLISH", "English"), ("SPANISH", "Spanish"),
                                                                ("BASQUE", "Basque")])

    dateInit = fields.date(string="dateInit")
    dateEnd = fields.date(string="dateEnd")


