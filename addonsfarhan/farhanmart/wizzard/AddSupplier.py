from odoo import api, fields, models

class AddSupplier(models.TransientModel):
    _name = 'farhanmart.addsupplier'

    
    supplier_id = fields.Many2one(
        string='Nama Perusahaan',
        comodel_name='farhanmart.supplier',
        required='False')
    
    
    alamat = fields.Char(
        string='Alamat',
        required='True')
    
    no_telp = fields.Char(
        string='No. Telepon',
        required='True')
    
    def button_barang(self):
        pass
    
    
    
