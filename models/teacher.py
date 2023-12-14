from odoo import models, api, fields

class Teacher(models.Model):
    _name = "bytebuddies.teacher"
    #_inherit = 'bytebuddies.user'

    studiesType = fields.Selection(string="levelType", selection=[("HIGHER LEVEL TRAINING CYCLES", "Higher level training cycles"), ("UNIVERSITY DEGREE", "University Degree"),
                                                                ("MASTER", "Master"), ("DOCTORATE", "Doctorate"), ("OTHER", "Other")])
    qualifications = fields.Char(string="Name", required=True)
