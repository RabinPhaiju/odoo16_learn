from odoo import api,fields,models,_
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Patient Records"
    _rec_name = "ref" # patient in dropdown shows ref as name

    name = fields.Char(string='Name',required=True,tracking=True)
    dob = fields.Date(string="DOB",tracking=True,default=fields.date.today())
    age = fields.Integer(string="Age",compute='_compute_age',store=True)
    is_child = fields.Boolean(string="Is Child?",tracking=True)
    notes = fields.Text(string="Notes",tracking=True)
    gender = fields.Selection([('male',"Male"),('female','Female'),('others','Others')],string="Gender",tracking=True)
    capitalized_name = fields.Char(string='Capitalized Name',compute='_compute_capitalized_name',store=True) # becomes readonly and not stored in db by default
    ref = fields.Char(string="Reference",default=lambda self:_('New'))

    active = fields.Boolean(string="Active",default=True) # for archive and un_archive
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag',string="Tags")

    @api.model_create_multi
    def create(self,vals_list): # inherit create method
        # we can edit the datas to be stored
        print('-------------------------',vals_list)
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
            # vals['gender'] = 'female'
        return super(HospitalPatient,self).create(vals_list)

    def write(self,vals):
        print('write (update) method inherit',vals)
        return super(HospitalPatient,self).write(vals)

    def name_get(self):
        # name_get function -> _rec_name
        return [(rec.id,rec.ref +" "+ rec.name) for rec in self]

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
        
    @api.depends('name')
    def _compute_capitalized_name(self):
        # runs after saving if depends is not added
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ""

    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        today = fields.date.today()
        for rec in self:
            if rec.dob:
                rec.age = relativedelta(today,rec.dob).years
            else:
                rec.age = 0

    @api.constrains('is_child','age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded !"))

    _sql_constraints = [('unique_ref','unique(ref)',"This ref is already used!")]