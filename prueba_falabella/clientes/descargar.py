from django.http.response import HttpResponse
from rest_framework.views import APIView
import xlwt
from .models import Cliente


class Descargar(APIView):

    def get(self, request):
        # content-type of response
        response = HttpResponse(content_type='application/ms-excel')

        # decide file name
        response['Content-Disposition'] = 'attachment; filename="clientes.xls"'

        # creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        # adding sheet
        ws = wb.add_sheet("sheet1")

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        # column header names, you can use your own headers here
        columns = ['numero documento', 'nombre', 'apellido', 'correo', 'telefono']

        # write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        # get your data, from database or from a text file...
        data = Cliente.objects.all()  # dummy method to fetch data.
        for my_row in data:
            row_num = row_num + 1
            ws.write(row_num, 0, my_row.numero_documento, font_style)
            ws.write(row_num, 1, my_row.nombre, font_style)
            ws.write(row_num, 2, my_row.apellido, font_style)
            ws.write(row_num, 3, my_row.correo, font_style)
            ws.write(row_num, 4, my_row.telefono, font_style)

        wb.save(response)
        return response

