from odoo import models,fields

class School(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread']
    _description = "Student Records"


    division = fields.Char(string='Division',tracking=True)
    full_name = fields.Char(string='FullName',tracking=True)

    class_id = fields.Integer(string='Class Id',tracking=True) # default=0
    number = fields.Integer(string='Value',default=0,tracking=True)

    float_no = fields.Float(string="Float",default=1.1)

    price = fields.Monetary(string="Price")

    active = fields.Boolean(string='Active',default=False)

    date = fields.Date(string="Date")

    date_time = fields.Datetime(string="DateTime")

    yes_no = fields.Selection([
            ('yes','Yes'),
            ('no',"No"),
        ])

    name = fields.Many2one('res.partner',string='Student') # one item to choose
    partner_id = fields.Many2one('res.partner',string='Partner')
    currency_id = fields.Many2one('res.currency',string='Currency')

    product_ids = fields.Many2many('product.product',string="Products") # many item to choose

    # school_line_ids = fields.One2many('school.student.line','school.id')

    document = fields.Binary(string="Document") # base64 encoded file

    image = fields.Image(string='Image') # extended of binary

    def action_accept(self):
        print('action_accept')