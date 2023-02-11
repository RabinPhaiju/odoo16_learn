from odoo import api,fields, models
import re


class OdooQuery(models.Model):
    _name = 'odoo.query'
    _description = 'Odoo Query'

    query = fields.Text(string="Type a query to execute")
    output_type = fields.Selection([('formatted',"Formatted"),('raw','Raw')],string="Output Format")

    result = fields.Text(string="Result")

    def action_execute(self):
        try:
            query = self.query
            self.env.cr.execute(query)
            if 'select' not in query:
                match = re.search(r'id=(\d+)', query)
                if match:
                    id = match.group(1)
                    self.result = id
            elif 'select' in query:
                self.result = self.env.cr.fetchall()
        except Exception as e:
            self.result = str(e)

    def action_clear(self):
        for rec in self:
            if rec.query:
                rec.query = ""