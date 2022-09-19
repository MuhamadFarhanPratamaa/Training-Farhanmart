from odoo import api, fields, models

class Barang(models.Model):
    _name = 'farhanmart.barang'
    _description = 'New Description'

    name = fields.Char(string='nama barang')
    harga_beli = fields.Integer(string='harga modal',required=True)
    harga_jual = fields.Integer(string='harga jual',required=True)
    kelompokbarang_id = fields.Many2one(comodel_name='farhanmart.kelompokbarang', 
                                            string='kelompok barang')
    supplier_id = fields.Many2many(comodel_name='farhanmart.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')
    
    
    