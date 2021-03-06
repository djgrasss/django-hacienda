#!-*- coding:  utf-8 -*-
from django.shortcuts import render
import datetime
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer, Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import cm
from reportlab.lib import colors

from liquidaciones.models import Liquidacion2, Pago2


PAGE_HEIGHT = 29.7*cm
PAGE_WIDTH = 21*cm


@login_required(login_url='/login/')
def licencia_expendio_alcohol(request):
    nombre_reporte = "licencia_expendio_alcohol"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    elementos = canvas.Canvas(response)

    elementos.setFont("Helvetica", 11) # Tamaño de letra

    # Primera fila
    elementos.drawCentredString(PAGE_WIDTH-13.5*cm, PAGE_HEIGHT-5.6*cm, 'RODRIGO BRAVO')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-5.6*cm, '0034530')

    # Segunda fila
    elementos.drawCentredString(PAGE_WIDTH-18.5*cm, PAGE_HEIGHT-7.3*cm, 'J-19724-1')
    elementos.drawCentredString(PAGE_WIDTH-13*cm, PAGE_HEIGHT-7.3*cm, 'CERVECERIA POLAR C.A')
    elementos.drawCentredString(PAGE_WIDTH-6.5*cm, PAGE_HEIGHT-7.3*cm, 'V-19724')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-7.3*cm, '00004585')

    # Tercera fila
    elementos.drawCentredString(PAGE_WIDTH-14.5*cm, PAGE_HEIGHT-9.2*cm, 'Av. Fuerzas Armadas. Calle Zulia # 20')
    elementos.drawCentredString(PAGE_WIDTH-6.2*cm, PAGE_HEIGHT-9.2*cm, 'ZAMORA')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-9.2*cm, 'COJ')

    # Cuarta fila
    elementos.drawCentredString(PAGE_WIDTH-19.2*cm, PAGE_HEIGHT-12.0*cm, '17-04-2009')
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-12.0*cm, 'Municipio')
    elementos.drawCentredString(PAGE_WIDTH-12.3*cm, PAGE_HEIGHT-12.0*cm, 'Estado')
    elementos.drawCentredString(PAGE_WIDTH-9.5*cm, PAGE_HEIGHT-12.0*cm, '204515')
    elementos.drawCentredString(PAGE_WIDTH-6.3*cm, PAGE_HEIGHT-12.0*cm, '200.000')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-12.0*cm, '9000300001')

    # Quinta fila
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-14.7*cm, 'Av. Fuerzas Armadas. Calle Zulia # 20')
    elementos.drawCentredString(PAGE_WIDTH-6.5*cm, PAGE_HEIGHT-14.7*cm, '12:30pm')
    elementos.drawCentredString(PAGE_WIDTH-2.5*cm, PAGE_HEIGHT-14.7*cm, '09:00pm')

    # Primera fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-14.5*cm, PAGE_HEIGHT-24.0*cm, 'RODRIGO BRAVO')
    elementos.drawCentredString(PAGE_WIDTH-4.5*cm, PAGE_HEIGHT-24.0*cm, '09090912')

    # Segunda fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-16.5*cm, PAGE_HEIGHT-25.5*cm, 'Av. Fuerzas Armadas. Calle Zulia # 20')
    elementos.drawCentredString(PAGE_WIDTH-4.8*cm, PAGE_HEIGHT-24.7*cm, 'J-197244582-2')

    # Tercera fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-17.5*cm, PAGE_HEIGHT-26.8*cm, 'Luis Alfredo Rodriguez Almeida')
    elementos.drawCentredString(PAGE_WIDTH-11.5*cm, PAGE_HEIGHT-26.7*cm, 'V-19724452')
    elementos.drawCentredString(PAGE_WIDTH-4.5*cm, PAGE_HEIGHT-26.7*cm, '04040452')

    # Cuarta fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-17.5*cm, PAGE_HEIGHT-27.7*cm, 'Gonzalo Gonzales')
    elementos.drawCentredString(PAGE_WIDTH-11.5*cm, PAGE_HEIGHT-27.7*cm, 'V-19724452')
    elementos.drawCentredString(PAGE_WIDTH-4.5*cm, PAGE_HEIGHT-27.7*cm, '04040452')

    # Quinta fila último cuadro
    elementos.drawCentredString(PAGE_WIDTH-19.2*cm, PAGE_HEIGHT-28.7*cm, '01-02-2014')
    elementos.drawCentredString(PAGE_WIDTH-15.7*cm, PAGE_HEIGHT-28.7*cm, '12:00')
    elementos.drawCentredString(PAGE_WIDTH-4.5*cm, PAGE_HEIGHT-28.7*cm, '04-12-2014')

    elementos.showPage()
    elementos.save()
    return response


@login_required(login_url='/login/')
def vauche_imprimir(request):
    nombre_reporte = "Vauche de Pago"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    elementos = canvas.Canvas(response)

    elementos.setFont("Helvetica", 8) # Tamaño de letra

    elementos.drawCentredString(PAGE_WIDTH-8.5*cm, PAGE_HEIGHT-0.7*cm, 'x')

    # Datos del depositante
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-2.0*cm, 'Alcaldía')
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-3.3*cm, 'Luis Carlos Rodriguez Quiñones')
    elementos.drawCentredString(PAGE_WIDTH-15.5*cm, PAGE_HEIGHT-4.0*cm, '20.522.392')

    # n° de cuenta
    elementos.setFont("Helvetica", 12) # Tamaño de letra
    elementos.drawCentredString(PAGE_WIDTH-7.7*cm, PAGE_HEIGHT-1.8*cm, '0  0  0  1  2  3  4  5  6  7  8  9  1  2  3  4  5  6  7  8')

    elementos.showPage()
    elementos.save()
    return response


@login_required(login_url='/login/')
def liquidacion_report(request, liquidacion):
    liquid = Liquidacion2.objects.get(numero=liquidacion)
    pagos = Pago2.objects.filter(liquidacion=liquid.pk)

    nombre_reporte = "liquidacion"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    #Esta lista contendra todos los elementos que se dibujaran en el pdf
    elementos = []
    doc = SimpleDocTemplate(response, title=nombre_reporte, topMargin=5,
                            bottomMargin=5, rightMargin=15, leftMargin=15)

    for i in range(0, 3):
        #---> Encabezado <---
        styleSheet = getSampleStyleSheet()
        cabecera = styleSheet['Normal']
        cabecera.alignment = TA_CENTER
        cabecera.firstLineIndent = 0
        cabecera.fontSize = 7.5
        cabecera.fontName = 'Helvetica-Bold'
        cabecera.leftIndent = -370
        cabecera.leading = 7

        logo = Image(settings.STATIC_ROOT+'/reportes/escudo.jpg',
                    width=25, height=35)
        logo.hAlign = 'LEFT'
        elementos.append(logo)

        elementos.append(Spacer(1, -35))
        txtEncabezado = 'País'
        txtEncabezado += '<br />Estado'
        txtEncabezado += '<br />Alcaldía'
        txtEncabezado += '<br />Dirección de Rentas Municipales'
        txtEncabezado += '<br />RIF: x'
        encabezado = Paragraph(txtEncabezado, cabecera)
        elementos.append(encabezado)
        #---> Fin Encabezado <---

        #---> Datos Contribuyente <---
        styleSheet2 = getSampleStyleSheet()
        estilo_contrib = styleSheet2['BodyText']
        estilo_contrib.alignment = TA_CENTER
        estilo_contrib.fontSize = 7.5
        estilo_contrib.fontName = 'Times-Roman'
        estilo_contrib.leading = 6
        contrib_style = [
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ]

        elementos.append(Spacer(1, -37))

        contrib1 = Paragraph('<b>INFORMACION GENERAL DEL CONTRIBUYENTE</b>', estilo_contrib)
        contrib2 = Paragraph('%s' % liquid.contribuyente.nombre, estilo_contrib)
        contrib3 = Paragraph('<b>CI/RIF:</b> %s ' % (liquid.contribuyente.num_identificacion), estilo_contrib)
        contrib4 = Paragraph('%s' % liquid.contribuyente.direccion, estilo_contrib)

        tabla_contrib = []
        tabla_contrib.append([contrib1])
        tabla_contrib.append([contrib2])
        tabla_contrib.append([contrib3])
        tabla_contrib.append([contrib4])

        tabla_contrib = Table(tabla_contrib, colWidths=(12.0*cm))
        tabla_contrib.setStyle(TableStyle(contrib_style))
        tabla_contrib.hAlign = 'RIGHT'

        elementos.append(tabla_contrib)
        #---> Fin Datos Contrib <---

        #---> Tabla <---
        elementos.append(Spacer(1, 10))

        estilo_tabla = styleSheet['BodyText']
        estilo_tabla.alignment = TA_CENTER
        estilo_tabla.fontSize = 7.5
        estilo_tabla.leading = 7
        x = [
            ('BACKGROUND', (0, 0), (6, 0), colors.silver),
            ('BACKGROUND', (0, 2), (6, 2), colors.silver),
            ('BACKGROUND', (0, -2), (-1, -2), colors.silver),
            ('SPAN', (0, -2), (-6, -2)),
            ('SPAN', (0, -1), (-6, -1)),
            ('BOX', (0, 5), (6, 0), 0.50, colors.black),
            ('BOX', (0, 9), (6, 0), 0.50, colors.black),
            ('GRID', (0, 0), (-1, -1), 0.50, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 8),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]
        tabla = []

        # Headers de la tabla
        hdatos = Paragraph('<b>Fecha Emisión</b>', estilo_tabla)
        x.append(('SPAN', (0, 0), (1, 0))),  # Extendiendo columna
        x.append(('SPAN', (0, 1), (1, 1))),  # Extendiendo columna

        hdatos1 = Paragraph('<b>Fecha Vencimiento</b>', estilo_tabla)
        hdatos2 = Paragraph('<b>ID</b>', estilo_tabla)
        hdatos3 = Paragraph('<b>No. Liquidación</b>', estilo_tabla)

        hdatos4 = Paragraph('<b>No. Deposito</b>', estilo_tabla)
        x.append(('SPAN', (5, 0), (6, 0))),  # Extendiendo columna
        x.append(('SPAN', (5, 1), (6, 1))),  # Extendiendo columna

        hPagos = Paragraph('<b>DETALLE DE PAGO DE IMPUESTOS VARIOS</b>', estilo_tabla)
        x.append(('SPAN', (0, 2), (6, 2))),  # Extendiendo columna

        hpago= Paragraph('<b>Año</b>', estilo_tabla)
        hpago1 = Paragraph('<b>Codigo</b>', estilo_tabla)
        hpago2 = Paragraph('<b>Impuesto</b>', estilo_tabla)
        hpago3 = Paragraph('<b>Monto Impuesto o Tasa</b>', estilo_tabla)
        hpago4 = Paragraph('<b>Recargo</b>', estilo_tabla)
        hpago5 = Paragraph('<b>Intereses</b>', estilo_tabla)
        hpago6 = Paragraph('<b>Sub-Total</b>', estilo_tabla)

        hpago7 = Paragraph('<b>Credito Fiscal</b>', estilo_tabla)
        hpago8 = Paragraph('<b>Descuento</b>', estilo_tabla)
        hpago9 = Paragraph('<b>Total(Bs.)</b>', estilo_tabla)
        hpago10 = Paragraph('<b>Impuesto o Tasa</b>', estilo_tabla)
        # Fin Headers de la tabla

        tabla.append([hdatos, '', hdatos1, hdatos2, hdatos3, hdatos4, ''])
        tabla.append([liquid.emision, '', liquid.vencimiento, liquid.contribuyente.id_contrato, liquid.numero, liquid.deposito, ''])
        pos = 0
        recargo = 0
        intereses = 0
        cancelado = 0
        monto = 0
        for pago in pagos:
            if liquid.tipo=='EST':
                credito=pago.credito_fiscal
            else:
                credito=0
            if pos == 0:
                tabla.append([hPagos])
                tabla.append([hpago, hpago1, hpago2, hpago3, hpago4, hpago5, hpago6])
            tabla.append([liquid.ano, pago.impuesto.codigo, pago.impuesto.descripcion, round(pago.monto,2), round(pago.recargo,2), round(pago.intereses,2), round(pago.monto,2)])

            pos = pos + 1

            recargo = recargo + pago.recargo
            intereses = intereses + pago.intereses
            cancelado = cancelado + pago.cancelado
            monto = monto + round(pago.monto,2)

        tabla.append([hpago7, '', hpago8, hpago10, hpago4, hpago5, hpago9])
        tabla.append([credito, '', pago.descuento, pago.monto, pago.recargo, intereses, pago.cancelado])

        t = Table(tabla, colWidths=(2.0*cm, 2.0*cm, 3.5*cm, 3.5*cm, 3.5*cm, 2.0*cm, 2.2*cm))
        t.setStyle(TableStyle(x))
        elementos.append(t)
        #---> Fin Tabla <---

        #---> Notas <---
        styleSheetNota = getSampleStyleSheet()
        nota = styleSheetNota['Normal']
        nota.fontSize = 8
        nota.fontName = 'Helvetica'
        nota.alignment = TA_LEFT

        txtNota1 = Paragraph('<b>DETALLES:</b> <br /> <b>%s</b>' % liquid.observaciones, nota)
        elementos.append(txtNota1)

        elementos.append(Spacer(1, 10))
        styleSheet3 = getSampleStyleSheet()
        parrafo = styleSheet3['Normal']
        parrafo.fontSize = 7
        parrafo.rightIndent = -320
        parrafo.fontName = 'Helvetica'
        parrafo.alignment = TA_CENTER

        elementos.append(Spacer(1, -17))
        txtNota1 = Paragraph('Evite Sanciones...Cumpla con su Ciudad...!', parrafo)
        elementos.append(txtNota1)

        txtNota2 = Paragraph('Para más información dirijase a las oficinas de Rentas Municipales.'+
                             '<br />Atención: Directora x' +
                             '<br /><b>Directora</b>', parrafo)
        elementos.append(txtNota2)
        #---> Fin Notas <---

        #---> Firmas <---
        elementos.append(Spacer(1, -42))
        estilo_tabla2 = styleSheet['BodyText']
        estilo_tabla2.alignment = TA_CENTER
        estilo_tabla2.fontSize = 7
        y = [
            ('BOX', (0, 0), (-1, -1), 0.50, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ]
        hrecibi = Paragraph('VALIDACIÓN', estilo_tabla2)
        hsellos = Paragraph('SELLOS', estilo_tabla2)
        hautorizada = Paragraph('FIRMA FUNCIONARIO', estilo_tabla2)

        tabla2 = []
        tabla2.append([hrecibi, '', ''])
        tabla2.append(['', hsellos, hautorizada])

        t2 = Table(tabla2, colWidths=(3.0*cm, 3.0*cm, 4.0*cm))
        t2.setStyle(TableStyle(y))
        t2.hAlign = 'LEFT'
        elementos.append(t2)
        #---> Fin Firmas <---

        elementos.append(Spacer(1, 5))
        lineaStyle = [
            ('LINEABOVE', (0, 0), (-1, -1), 0.35, colors.black),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 2),
        ]
        linea = []
        linea.append([' '])

        l2 = Table(linea, colWidths=(20.0*cm))
        l2.setStyle(TableStyle(lineaStyle))
        elementos.append(l2)

    doc.build(elementos)
    return response


@login_required(login_url='/login/')
def boletin_liquid_definitiva(request, liquidacion):
    liquid = Liquidacion2.objects.get(numero=liquidacion)
    pagos = Pago2.objects.filter(liquidacion=liquid.pk)

    nombre_reporte = "boletin_liquidacion"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    #Esta lista contendra todos los elementos que se dibujaran en el pdf
    elementos = []
    doc = SimpleDocTemplate(response, title=nombre_reporte, topMargin=5,
                            bottomMargin=5, rightMargin=15, leftMargin=15)

    for i in range(0, 2):
        #---> Encabezado <---
        styleSheet = getSampleStyleSheet()
        cabecera = styleSheet['Normal']
        cabecera.alignment = TA_CENTER
        cabecera.firstLineIndent = 0
        cabecera.fontSize = 6
        cabecera.fontName = 'Helvetica-Bold'
        cabecera.leftIndent = -380
        cabecera.leading = 7

        logo = Image(settings.STATIC_ROOT+'/reportes/escudo.jpg',
                    width=25, height=35)
        logo.hAlign = 'LEFT'
        elementos.append(logo)

        elementos.append(Spacer(1, -35))
        txtEncabezado = 'País'
        txtEncabezado += '<br />Estado'
        txtEncabezado += '<br />Alcaldía'
        txtEncabezado += '<br />Dirección de Rentas Municipales'
        txtEncabezado += '<br />RIF: '
        encabezado = Paragraph(txtEncabezado, cabecera)
        elementos.append(encabezado)
        #---> Fin Encabezado <---

        #---> Datos Contribuyente <---
        styleSheet2 = getSampleStyleSheet()
        estilo_contrib = styleSheet2['BodyText']
        estilo_contrib.alignment = TA_CENTER
        estilo_contrib.fontSize = 7.5
        estilo_contrib.fontName = 'Times-Roman'
        estilo_contrib.leading = 6
        contrib_style = [
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ]

        elementos.append(Spacer(1, -37))

        contrib1 = Paragraph(u'<b>BOLETIN DE NOTIFICACIÓN</b>', estilo_contrib)
        contrib2 = Paragraph(u'<b>%s</b>' % pagos[0].impuesto.descripcion, estilo_contrib)
        contrib3 = Paragraph(u'<b>PERIODO IMPOSITIVO:</b> %s ' % (liquid.ano), estilo_contrib)
        contrib4 = Paragraph(u'<b>FECHA:</b> %s' % liquid.emision, estilo_contrib)

        tabla_contrib = []
        tabla_contrib.append([contrib1])
        tabla_contrib.append([contrib2])
        tabla_contrib.append([contrib3])
        tabla_contrib.append([contrib4])

        tabla_contrib = Table(tabla_contrib, colWidths=(12.0*cm))
        tabla_contrib.setStyle(TableStyle(contrib_style))
        tabla_contrib.hAlign = 'RIGHT'

        elementos.append(tabla_contrib)
        #---> Fin Datos Contrib <---

        #---> Tabla <---
        elementos.append(Spacer(1, 10))

        estilo_tabla = styleSheet['BodyText']
        estilo_tabla.alignment = TA_CENTER
        estilo_tabla.fontSize = 7.5
        estilo_tabla.leading = 7
        x = [
            ('BACKGROUND', (0, 0), (2, 0), colors.silver),
            ('BACKGROUND', (0, 2), (2, 2), colors.silver),
            ('BACKGROUND', (0, -1), (-1, -1), colors.silver),
            ('GRID', (0, 0), (-1, -1), 0.50, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 7.5),
        ]
        tabla = []

        # Headers de la tabla
        hdatos = Paragraph('<b>R.I.F.</b>', estilo_tabla)
        hdatos1 = Paragraph('<b>RAZON SOCIAL</b>', estilo_tabla)
        hdatos2 = Paragraph('<b>ID</b>', estilo_tabla)

        hdatos3 = Paragraph('<b>DOMICILIO FISCAL</b>', estilo_tabla)
        x.append(('SPAN', (0, 2), (2, 2))),  # Extendiendo columna

        hdatos4 = Paragraph('<b>PERIODO FISCAL:</b>', estilo_tabla)
        hdatos5 = Paragraph('<b>IMPUESTO TOTAL ANUAL ESTIMADO</b>', estilo_tabla)
        hdatos6 = Paragraph('<b>IMPUESTO TOTAL ANUAL DEFINITIVO</b>', estilo_tabla)
        hdatos7 = Paragraph('<b>DIFERENCIA A CANCELAR</b>', estilo_tabla)
        # Fin Headers de la tabla

        tabla.append([hdatos, hdatos1, hdatos2])
        tabla.append([liquid.contribuyente.num_identificacion, liquid.contribuyente.nombre, liquid.contribuyente.id_contrato])

        # -- Direccion
        tabla.append([hdatos3])
        direccion = Paragraph('%s' % liquid.contribuyente.direccion, estilo_tabla)
        tabla.append([direccion])
        x.append(('SPAN', (0, 3), (2, 3))),  # Extendiendo columna

        # -- Periodo Fiscal
        periodo_fiscal = Paragraph('<b>01 DE ENERO DE ## AL 31 DE DICIEMBRE DE %s</b>' % liquid.ano, estilo_tabla)
        tabla.append([hdatos4, periodo_fiscal])
        x.append(('SPAN', (1, 4), (2, 4))),  # Extendiendo columna

        t = Table(tabla, colWidths=(3.5*cm, 11.5*cm, 3.5*cm))
        t.setStyle(TableStyle(x))
        elementos.append(t)
        elementos.append(Spacer(1, 10))

        tabl2 = []
        y = [
            ('BACKGROUND', (0, 0), (2, 0), colors.silver),
            ('BOX', (0, 5), (6, 0), 0.50, colors.black),
            ('BOX', (0, 9), (6, 0), 0.50, colors.black),
            ('GRID', (0, 0), (-1, -1), 0.50, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 7.5),
        ]
        tabl2.append([hdatos5, hdatos6, hdatos7])
        montos = liquid.contribuyente.monto_set.filter(contribuyente=liquid.contribuyente, ano=liquid.ano)
        diferencia = float(montos[0].definitivo) - float(montos[0].estimado)
        tabl2.append([montos[0].estimado, montos[0].definitivo, diferencia])

        t2 = Table(tabl2, colWidths=(6.5*cm, 6.5*cm, 5.5*cm))
        t2.setStyle(TableStyle(y))
        elementos.append(t2)
        #---> Fin Tabla <---

        #---> Notas <---
        styleSheetNota = getSampleStyleSheet()
        nota = styleSheetNota['Normal']
        nota.fontSize = 7.5
        nota.fontName = 'Helvetica'
        nota.alignment = TA_JUSTIFY

        elementos.append(Spacer(1, 5))
        txtNota1 = Paragraph('<b>Ordenanza de Impuesto sobre Actividades Económicas vigente:</b><br />', nota)
        elementos.append(txtNota1)

        txtArt1 = Paragraph('"<b>ARTICULO 24.-</b> La declaración definitiva deberá presentarse en el mes de Enero de cada año y comprenderá'+\
                            ' el monto de los ingresos brutos obtenidos en el ejercicio económico entre el 1° de Enero al 31 de Diciembre'+\
                            ' del año anterior, en cada una de las actividades o ramo ejercidas por el contribuyente a que se refiere el'+\
                            ' Clasificador de Actividades Económicas y que hayan sido o no autorizados en la correspondiente Licencia'+\
                            ', la cual conformara la base imponible definitiva para la determinación, cálculo y liquidación del impuesto'+\
                            ' correspondiente a la obligación tributaria causada en el ejercicio fiscal fenecido."<br />', nota)
        elementos.append(txtArt1)

        elementos.append(Spacer(1, 5))
        txtArt2 = Paragraph('"<b>ARTICULO 66.-</b> Serán sancionados en la forma prevista en el artículo de los contribuyentes que:'+\
                            ' ..."d) No paguen, dentro de los plazos previstos en el artículo 24 de esta Ordenanza, la diferencia'+\
                            ' producto de la presentación de la declaración definitiva, con <b>multa equivalente a 10 Unidades'+\
                            ' Tributarias y cierre temporal del establecimiento</b>, hasta tanto cumpla con las obligaciones'+\
                            ' establecidas en dicho artículo."<br />', nota)
        elementos.append(txtArt2)

        elementos.append(Spacer(1, 5))
        txtNota2 = Paragraph('NOTA: La presente notificación no implica la<br />cancelación de años anteriores al %s' % liquid.ano, nota)
        elementos.append(txtNota2)

        elementos.append(Spacer(1, 10))
        styleSheet3 = getSampleStyleSheet()
        parrafo = styleSheet3['Normal']
        parrafo.fontSize = 7.5
        parrafo.fontName = 'Helvetica'
        parrafo.alignment = TA_CENTER

        elementos.append(Spacer(1, 15))
        txtNota3 = Paragraph('<b>Evite Sanciones... Cumpla con su Ciudad...!</b>', parrafo)
        elementos.append(txtNota3)

        styleSheet3 = getSampleStyleSheet()
        parrafo = styleSheet3['Normal']
        parrafo.fontSize = 7.5
        parrafo.rightIndent = -320
        parrafo.fontName = 'Helvetica'
        parrafo.alignment = TA_CENTER

        elementos.append(Spacer(1, -50))
        lineaStyle = [
            ('LINEABOVE', (0, 0), (-1, -1), 0.55, colors.black),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 2),
        ]
        linea = []
        linea.append([' '])

        l2 = Table(linea, colWidths=(8.0*cm))
        l2.setStyle(TableStyle(lineaStyle))
        l2.hAlign = 'RIGHT'
        elementos.append(l2)

        elementos.append(Spacer(1, -15))
        txtNota4 = Paragraph('<hr /><br />Directora x' +
                             '<br /><b>Directora</b>', parrafo)
        elementos.append(txtNota4)

        elementos.append(Spacer(1, 20))
        txtNota4 = Paragraph('<b>ALCALDIA</b>', parrafo)
        elementos.append(txtNota4)
        #---> Fin Notas <---

        elementos.append(Spacer(1, 10))
        linea = []
        linea.append([' '])

        l2 = Table(linea, colWidths=(20.0*cm))
        l2.setStyle(TableStyle(lineaStyle))
        elementos.append(l2)

    doc.build(elementos)
    return response


@login_required(login_url='/login/')
def boletin_liquid_estimada(request, liquidacion):
    liquid = Liquidacion2.objects.get(numero=liquidacion)
    pagos = Pago2.objects.filter(liquidacion=liquid.pk)

    nombre_reporte = "boletin_liquidacion"
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nombre_reporte+'.pdf; pagesize=letter;'

    #Esta lista contendra todos los elementos que se dibujaran en el pdf
    elementos = []
    doc = SimpleDocTemplate(response, title=nombre_reporte, topMargin=5,
                            bottomMargin=5, rightMargin=15, leftMargin=15)

    for i in range(0, 2):
        #---> Encabezado <---
        styleSheet = getSampleStyleSheet()
        cabecera = styleSheet['Normal']
        cabecera.alignment = TA_CENTER
        cabecera.firstLineIndent = 0
        cabecera.fontSize = 7
        cabecera.fontName = 'Helvetica-Bold'
        cabecera.leftIndent = -350
        cabecera.leading = 7

        logo = Image(settings.STATIC_ROOT+'/reportes/escudo.jpg',
                    width=25, height=35)
        logo.hAlign = 'LEFT'
        elementos.append(logo)

        elementos.append(Spacer(1, -35))
        txtEncabezado = 'País'
        txtEncabezado += '<br />Estado'
        txtEncabezado += '<br />Alcaldía'
        txtEncabezado += '<br />Dirección de Rentas Municipales'
        txtEncabezado += '<br />RIF: '
        encabezado = Paragraph(txtEncabezado, cabecera)
        elementos.append(encabezado)
        #---> Fin Encabezado <---

        #---> Datos Contribuyente <---
        styleSheet2 = getSampleStyleSheet()
        estilo_contrib = styleSheet2['BodyText']
        estilo_contrib.alignment = TA_CENTER
        estilo_contrib.fontSize = 7
        estilo_contrib.fontName = 'Times-Roman'
        estilo_contrib.leading = 6
        contrib_style = [
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ]

        elementos.append(Spacer(1, -37))

        contrib1 = Paragraph(u'<b>BOLETIN DE NOTIFICACIÓN</b>', estilo_contrib)
        contrib2 = Paragraph(u'<b>%s</b>' % pagos[0].impuesto.descripcion, estilo_contrib)
        contrib3 = Paragraph(u'<b>PERIODO IMPOSITIVO: %s </b>' % (liquid.ano), estilo_contrib)
        contrib4 = Paragraph(u'<b>FECHA: %s </b>' % liquid.emision, estilo_contrib)

        tabla_contrib = []
        tabla_contrib.append([contrib1])
        tabla_contrib.append([contrib2])
        tabla_contrib.append([contrib3])
        tabla_contrib.append([contrib4])

        tabla_contrib = Table(tabla_contrib, colWidths=(8.0*cm))
        tabla_contrib.setStyle(TableStyle(contrib_style))
        tabla_contrib.hAlign = 'RIGHT'

        elementos.append(tabla_contrib)
        #---> Fin Datos Contrib <---

        #---> Tabla <---
        elementos.append(Spacer(1, 5))

        estilo_tabla = styleSheet['BodyText']
        estilo_tabla.alignment = TA_CENTER
        estilo_tabla.fontSize = 6
        estilo_tabla.leading = 6
        x = [
            ('BACKGROUND', (0, 0), (2, 0), colors.silver),
            ('BACKGROUND', (0, 2), (2, 2), colors.silver),
            ('BACKGROUND', (0, -1), (-1, -1), colors.silver),
            ('GRID', (0, 0), (-1, -1), 0.50, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 6.5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
        ]
        tabla = []

        # Headers de la tabla
        hdatos = Paragraph('<b>R.I.F.</b>', estilo_tabla)
        hdatos1 = Paragraph('<b>RAZON SOCIAL</b>', estilo_tabla)
        hdatos2 = Paragraph('<b>ID</b>', estilo_tabla)

        hdatos3 = Paragraph('<b>DOMICILIO FISCAL</b>', estilo_tabla)
        x.append(('SPAN', (0, 2), (2, 2))),  # Extendiendo columna

        hdatos4 = Paragraph('<b>PERIODO FISCAL:</b>', estilo_tabla)
        hdatos5 = Paragraph('<b>INGRESOS BRUTOS ESTIMADOS</b>', estilo_tabla)
        hdatos6 = Paragraph('<b>IMPUESTO TOTAL ANUAL ESTIMADO</b>', estilo_tabla)
        # Fin Headers de la tabla

        tabla.append([hdatos, hdatos1, hdatos2])
        tabla.append([liquid.contribuyente.num_identificacion, liquid.contribuyente.nombre, liquid.contribuyente.id_contrato])

        # -- Direccion
        tabla.append([hdatos3])
        direccion = Paragraph('%s' % liquid.contribuyente.direccion, estilo_tabla)
        tabla.append([direccion])
        x.append(('SPAN', (0, 3), (2, 3))),  # Extendiendo columna

        # -- Periodo Fiscal
        periodo_fiscal = Paragraph('<b>01 DE ENERO DE %s AL 31 DE DICIEMBRE DE %s</b>' % (liquid.ano, liquid.ano), estilo_tabla)
        tabla.append([hdatos4, periodo_fiscal])
        x.append(('SPAN', (1, 4), (2, 4))),  # Extendiendo columna

        t = Table(tabla, colWidths=(3.5*cm, 11.5*cm, 3.5*cm))
        t.setStyle(TableStyle(x))
        elementos.append(t)
        elementos.append(Spacer(1, 5))

        tabl2 = [] # Tabla 2
        y = [
            ('BACKGROUND', (0, 0), (2, 0), colors.silver),
            ('BOX', (0, 5), (6, 0), 0.50, colors.black),
            ('BOX', (0, 9), (6, 0), 0.50, colors.black),
            ('GRID', (0, 0), (-1, -1), 0.50, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 6.5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
        ]
        tabl2.append([hdatos5, hdatos6])
        montos = liquid.contribuyente.monto_set.filter(contribuyente=liquid.contribuyente, ano=liquid.ano)
        monto_anual = float(montos[0].estimado) * 12
        tabl2.append([montos[0].estimado, monto_anual])

        t2 = Table(tabl2, colWidths=(9.0*cm, 9.5*cm))
        t2.setStyle(TableStyle(y))
        elementos.append(t2)
        elementos.append(Spacer(1, 5))

        tabl3 = [] # Tabla 3
        z = [
            ('BACKGROUND', (0, 0), (7, 0), colors.silver),
            ('BOX', (0, 5), (6, 0), 0.50, colors.black),
            ('BOX', (0, 9), (6, 0), 0.50, colors.black),
            ('GRID', (0, 0), (-1, -1), 0.50, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 6.5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
        ]

        titulo_tabl3 = Paragraph('<b>RESUMEN DEL IMPUESTO A PAGAR SEGUN EL MES CUANDO REALICE EL PAGO</b>', estilo_tabla)
        tDatos = Paragraph('<b>TRIMESTRE</b>', estilo_tabla)
        tDatos2 = Paragraph('<b>AÑO</b>', estilo_tabla)
        tDatos3 = Paragraph('<b>IMPUESTO TRIMESTRAL</b>', estilo_tabla)
        tDatos4 = Paragraph('<b>EXIGIBILIDAD</b>', estilo_tabla)
        tDatos5 = Paragraph('<b>RECARGO(10%)</b><br />Si Cancela en...', estilo_tabla)
        tDatos6 = Paragraph('<b>INTERESES ACUMULADOS</b><br />Si Cancela a partir de...', estilo_tabla)
        nota_especial = Paragraph('Se sumara 1% Adicional Mensual por Adelantado', estilo_tabla)

        tabl3.append([titulo_tabl3])
        z.append(('SPAN', (0, 0), (7, 0))),  # Extendiendo columna titulo_tabl3

        tabl3.append([tDatos, tDatos2, tDatos3, tDatos4, tDatos5, '', tDatos6, ''])
        z.append(('SPAN', (4, 1), (5, 1))),  # Extendiendo columna tDatos5
        z.append(('SPAN', (6, 1), (7, 1))),  # Extendiendo columna tDatos6
        z.append(('BACKGROUND', (0, 1), (7, 1), colors.silver)),

        monto_estimado = montos[0].estimado
        monto_trimestres = float(monto_estimado) / 4
        monto_recargo = float(monto_trimestres) * 0.10
        tabl3.append(['1', liquid.ano, monto_trimestres, 'ENERO', 'FEBRERO', monto_recargo, 'MARZO', nota_especial])
        tabl3.append(['2', liquid.ano, monto_trimestres, 'ABRIL', 'MAYO', monto_recargo, 'JUNIO', ''])
        tabl3.append(['3', liquid.ano, monto_trimestres, 'JULIO', 'AGOSTO', monto_recargo, 'SEPTIEMBRE', ''])
        tabl3.append(['4', liquid.ano, monto_trimestres, 'OCTUBRE', 'NOVIEMBRE', monto_recargo, 'DICIEMBRE', ''])
        z.append(('SPAN', (7, 2), (7, 5))),  # Extendiendo columna nota_especial
        z.append(('VALIGN', (7, 2), (7, 5), 'MIDDLE')),

        nota_est = Paragraph('<b>SI CANCELA TODO ANTES DEL 31 DE ENERO DEL AÑO EN CURSO TENDRA<br />UN DESCUENTO DEL 10% DEL MONTO DE SUS IMPUESTOS</b>', estilo_tabla)
        tabl3.append([nota_est])
        z.append(('SPAN', (0, 6), (7, 6))),  # Extendiendo columna nota_est
        z.append(('BACKGROUND', (0, 6), (7, 6), colors.silver)),

        t2 = Table(tabl3, colWidths=(1.9*cm, 1.7*cm, 3.7*cm, 3.5*cm, 2.0*cm, 2.0*cm, 2.0*cm, 2.0*cm))
        t2.setStyle(TableStyle(z))
        elementos.append(t2)
        #---> Fin Tabla <---

        #---> Notas <---
        styleSheetNota = getSampleStyleSheet()
        nota = styleSheetNota['Normal']
        nota.fontSize = 6
        nota.fontName = 'Helvetica'
        nota.alignment = TA_JUSTIFY

        elementos.append(Spacer(1, 5))
        txtNota1 = Paragraph('<b>Ordenanza de Impuesto sobre Actividades Económicas vigente:</b><br />', nota)
        elementos.append(txtNota1)

        txtArt1 = Paragraph('<b>ARTICULO 23.-</b> En el mes de Noviembre de cada año los sujetos pasivos obligados al pago de este impuesto'+\
                            ', presentan por ante la Dirección de Rentas Municipales o el ente que designe el Alcalde, una declaración'+\
                            ' estimada de los ingresos brutos que obtendrán en el ejercicio fiscal siguiente, que conformara la base de'+\
                            ' calculo para la determinación y liquidación del impuesto estimado correspondiente a la obligación tributaria'+\
                            ' que se causará en el transcurso del ejercicio fiscal gravable, la cual será ajustada con la declaración '+\
                            'definitiva de ingresos brutos obtenidos al cierre del ejercicio fiscal del que se trate.<br />', nota)
        elementos.append(txtArt1)

        elementos.append(Spacer(1, 5))
        txtArt2 = Paragraph('"<b>ARTICULO 66.-</b> Serán sancionados en la forma prevista en el artículo de los contribuyentes que:'+\
                            ' ..."d) No paguen, dentro de los plazos previstos en el artículo 24 de esta Ordenanza, la diferencia'+\
                            ' producto de la presentación de la declaración definitiva, con <b>multa equivalente a 10 Unidades'+\
                            ' Tributarias y cierre temporal del establecimiento</b>, hasta tanto cumpla con las obligaciones'+\
                            ' establecidas en dichos artículos."<br />', nota)
        elementos.append(txtArt2)

        elementos.append(Spacer(1, 5))
        txtNota2 = Paragraph('NOTA: La presente notificación no implica la<br />cancelación de años anteriores al %s' % liquid.ano, nota)
        elementos.append(txtNota2)

        elementos.append(Spacer(1, 10))
        styleSheet3 = getSampleStyleSheet()
        parrafo = styleSheet3['Normal']
        parrafo.fontSize = 7
        parrafo.fontName = 'Helvetica'
        parrafo.alignment = TA_CENTER

        elementos.append(Spacer(1, 5))
        txtNota3 = Paragraph('<b>Evite Sanciones... Cumpla con su Ciudad...!</b>', parrafo)
        elementos.append(txtNota3)

        styleSheet3 = getSampleStyleSheet()
        parrafo = styleSheet3['Normal']
        parrafo.fontSize = 7
        parrafo.rightIndent = -320
        parrafo.fontName = 'Helvetica'
        parrafo.alignment = TA_CENTER

        elementos.append(Spacer(1, -50))
        lineaStyle = [
            ('LINEABOVE', (0, 0), (-1, -1), 0.55, colors.black),
            ('FONT', (0, 0), (-1, -1), "Helvetica", 2),
        ]
        linea = []
        linea.append([' '])

        l2 = Table(linea, colWidths=(8.0*cm))
        l2.setStyle(TableStyle(lineaStyle))
        l2.hAlign = 'RIGHT'
        elementos.append(l2)

        elementos.append(Spacer(1, -20))
        txtNota4 = Paragraph('<hr /><br />Directora x' +
                             '<br /><b>Directora</b>', parrafo)
        elementos.append(txtNota4)

        elementos.append(Spacer(1, 15))
        txtNota4 = Paragraph('<b>ALCALDIA</b>', parrafo)
        elementos.append(txtNota4)
        #---> Fin Notas <---

        elementos.append(Spacer(1, 5))
        linea = []
        linea.append([' '])

        l2 = Table(linea, colWidths=(20.0*cm))
        l2.setStyle(TableStyle(lineaStyle))
        elementos.append(l2)

    doc.build(elementos)
    return response
