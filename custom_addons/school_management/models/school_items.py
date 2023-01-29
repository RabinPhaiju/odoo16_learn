from odoo import models,fields,api

class SchoolItems(models.Model):
    _name = 'school.items'
    _rec_name = "class_id"


    student_ids = fields.Many2many('school.student',string='Students')
    class_id = fields.Integer(string="Class")
    division = fields.Char(string="Division",related="student_ids.division")
    admission_date = fields.Date(string="Admission Date",related="student_ids.admission_date")

    @api.onchange('class_id')
    def change_class(self):
        students = self.env['school.student'].search([('class_id','=',self.class_id)])
        self.student_ids = students

        # val = self.env['school.student'].browse(self.class_id)
        # print('va',val)