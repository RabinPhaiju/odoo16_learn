from odoo import api,fields,models,_
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import date

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Patient Records"
    _rec_name = "ref" # patient in dropdown shows ref as name

    name = fields.Char(string='Name',required=True,tracking=True)
    dob = fields.Date(string="DOB",tracking=True,default=fields.date.today())
    age = fields.Integer(string="Age",compute='_compute_age',inverse='_inverse_compute_age',store=True)
    is_child = fields.Boolean(string="Is Child?",tracking=True)
    notes = fields.Text(string="Notes",tracking=True)
    gender = fields.Selection([('male',"Male"),('female','Female'),('others','Others')],string="Gender",tracking=True)
    capitalized_name = fields.Char(string='Capitalized Name',compute='_compute_capitalized_name',store=True) # becomes readonly and not stored in db by default
    ref = fields.Char(string="Reference",default=lambda self:_('New'))
    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count",store=True)
    appointment_ids = fields.One2many('hospital.appointment','patient_id',string="Appointments")
    is_birthday = fields.Boolean(string="Birthday",compute="_compute_is_birthday")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    website= fields.Char(string="Website")

    parent = fields.Char(string="Parent")
    marital_status = fields.Selection([
        ('married','Married'),
        ('single','Single'),
    ],string="Marital Status",tracking=True)
    partner_name = fields.Char(string="Partner Name")

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
        return [(rec.id,"[%s] %s" % (rec.ref , rec.name)) for rec in self]

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
    
    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            if rec.age:
                rec.dob = today - relativedelta(years=rec.age)

    @api.ondelete(at_uninstall=False)
    def _check_appointments(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(_("You cannot delete patient with appointment.!"))

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        # for rec in self:
            # rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id','=',rec.id)])
        # using group method
        appointment_group = self.env['hospital.appointment'].read_group(domain=[],fields=['patient_id'],groupby=['patient_id'])
        for appointment in appointment_group:
            patient_id = appointment.get('patient_id')[0]
            patient_rec = self.browse(patient_id)
            patient_rec.appointment_count = appointment['patient_id_count']
            self -= patient_rec
        self.appointment_count = 0
    
    @api.depends('dob')
    def _compute_is_birthday(self):
        today = date.today()
        is_birthday = False
        for rec in self:
            if rec.dob:
                if today.day == rec.dob.day and today.month == rec.dob.month:
                    is_birthday = True
        rec.is_birthday = is_birthday


    @api.constrains('is_child','age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded !"))
    
    @api.constrains('dob')
    def _check_dob(self):
        for rec in self:
            if rec.dob and rec.dob > fields.Date.today():
                raise ValidationError(_("DOB should not greater than today !"))

    def action_group_test(self):
        print('------------action_group_test')
    
    def action_view_appointment(self):
        return {
            'name':_('Appointment'),
            'res_model':'hospital.appointment',
            'view_mode':'list,form,calendar,activity',
            'context':{'default_patient_id':self.id},
            'domain':[('patient_id','=',self.id)],
            'target':'current',
            'type':'ir.actions.act_window'
        }
                

    _sql_constraints = [('unique_ref','unique(ref)',"This ref is already used!")]
    _sql_constraints = [('check_age','check(age > 0)',"Age cannot be less than 0!")]