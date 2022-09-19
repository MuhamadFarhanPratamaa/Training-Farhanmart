from odoo import api, fields, models


class konsumen(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'
    
    poin = fields.Integer(string='poin')
    level = fields.Char(string='level')
    
    
     
     
     
     
     
    
