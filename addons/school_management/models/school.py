from odoo import models,fields,api,_
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError,UserError

class School(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread']
    _description = "Student Records"


    division = fields.Char(string='Division',tracking=True)
    full_name = fields.Char(string='FullName',tracking=True)
    address = fields.Char(string='Address',tracking=True)

    class_id = fields.Integer(string='Class Id',tracking=True) # default=0
    number = fields.Integer(string='Value',default=0,tracking=True)
    age = fields.Integer(string='Age',tracking=True,compute='_compute_age',store=True) # becomes readonly and not stored in db by default

    float_no = fields.Float(string="Float",default=1.1)

    price = fields.Monetary(string="Price")

    active = fields.Boolean(string='Active',default=False)

    dob = fields.Date(string="dob")
    admission_date = fields.Date(string="Admission Date",default=fields.date.today())

    date_time = fields.Datetime(string="DateTime")

    yes_no = fields.Selection([
            ('yes','Yes'),
            ('no',"No"),
        ])

    name = fields.Many2one('res.partner',string='Student') # one item to choose
    partner_id = fields.Many2one('res.partner',string='Partner',default=lambda l:l.env.user)
    currency_id = fields.Many2one('res.currency',string='Currency')

    product_ids = fields.Many2many('product.product',string="Products") # many item to choose
    tags = fields.Many2many('account.account.tag',string="Tags") # many item to choose

    # school_line_ids = fields.One2many('school.student.line','school.id')

    document = fields.Binary(string="Document") # base64 encoded file

    image = fields.Image(string='Image') # extended of binary

    def action_accept(self):
        print('action_accept')

    
    def unlink(self):
        for student in self:
            if student.class_id >=12:
                raise UserError(_('You cannot delete a student of class 12 or higher for record purpose'))
        return super(School,self).unlink()


    @api.constrains('admission_date','class_id')
    def _validation_constrains(self):
        today = fields.date.today()
        for rec in self:
            if rec.admission_date > today:
                raise ValidationError(_('Admission date is greater than today!'))
            elif rec.class_id > 12 or rec.class_id < 1:
                # can be use diff constrains
                raise ValidationError(_('Invalid Class!'))

    @api.onchange('name')
    def _onchange_name(self):
        self.address = self.name.street

    @api.depends('dob')
    def _compute_age(self):
        # runs after saving if depends is not added
        self.age = False
        today = fields.date.today()
        for rec in self:
            if rec.dob:
                rec.age = relativedelta(today,rec.dob).years


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _name_search(self,name,args=None,operator="ilike", limit=100,name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|','|',('name',operator,name),('phone',operator,name),('email',operator,name)]
        return self._search(domain + args,limit = limit, access_rights_uid=name_get_uid)