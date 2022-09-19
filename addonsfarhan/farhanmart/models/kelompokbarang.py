from odoo import api, fields, models


class kelompokbarang(models.Model):
    _name = 'farhanmart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection ( [
        ('makanan basah', 'Makanan Basah'),
        ('makanan kering', 'Makanan Kering'),
        ('minuman', 'Minuman')
    ], string= 'Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')

    @api.onchange('name')
    def _onchange_kode_kelompok(self) :
        if self.name == 'makanan basah' :
            self.kode_kelompok = 'MAKO1'
        elif self.name == 'makanan kering' :
            self.kode_kelompok = 'MAKO2'
        elif self.name == 'minuman' :
            self.kode_kelompok = 'MIN'

    kode_rak = fields.Char(string='kode rak')
    barang_ids = fields.One2many(comodel_name='farhanmart.barang',
                                    inverse_name='kelompokbarang_id',
                                    string='Daftar Barang')
    jml_item = fields.Char(compute = '_compute_jml_item' , string='Jml Item')

    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self :
            a = self.env['farhanmart.barang'] .search ([('kelompokbarang_id', '=', record.id)]) .mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')

    
    
    
