from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.farhanmart.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Daftar Penjualan')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'No. Nota')
        sheet.write(1, 1, 'Nama Pembeli')
        sheet.write(1, 2, str('Tgl.Transaksi'))
        sheet.write(1, 3, str('Total Pembayaran'))
        row = 2
        col = 0
        for obj in penjualan:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pembeli)
            sheet.write(row, col+2, str(obj.tgl_penjualan))
            sheet.write(row, col+3, str(obj.total_bayar))
            for xxx in obj.detailpenjualan_ids:
                sheet.write(row, col+4, xxx.barang_id.name)
                col += 1
            row += 1