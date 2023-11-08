from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter



from monday_data_extraction.data_to_score import *

# Create a function to generate the PDF
def generate_pdf(prev_evasi_mes, prev_acc_mes, prev_acc_consuntivo, importo_tot_prev_evasi, prev_acc_anno):
    """
    Questa funzione crea un pdf basato da griglie rettangolari con
    all' interno i dati estrapolati da varie funzioni presenti nel file extract_data_script
    (Per esempio la parte iniziale aggiunge delle descrizioni con delle box sotto)

    il file creato si chiama kpi_report.pdf e si trova all'interno della root di progetto

    Args:

    Returns:
        pdf file
    """
########################################################################################################################
#PRIMA PAGINA DEL PDF

    # CREO UN OGGETTO SimpleDocTemplate
    doc = SimpleDocTemplate("../kpi_report.pdf", pagesize=letter)


    # CREO UNA LISTA PER SALVARE INFORMAZIONI
    story = []

    # DEFINISCO IL TITOLO AD INIZIO PDF
    title = "REPORT KPI MESE 2023"
    title_style = getSampleStyleSheet()["Title"]
    title_paragraph = Paragraph(title, title_style)
    story.append(title_paragraph)

    # CREO UNA LINEA DI SPAZIO SOTTO IL TITOLO
    story.append(Spacer(1, 12))

    # AGGIUNGO I DATI DELL'AUTORE E GLI AGGIORNAMENTI
    author_info = "Autore del report: Christian Trocino<br/>Dati aggiornati al XX/XX/XXXX"
    author_style = getSampleStyleSheet()["Normal"]
    author_paragraph = Paragraph(author_info, author_style)
    story.append(author_paragraph)

    # CREO UNA LINEA DI SPAZIO SOTTO IL TITOLO
    story.append(Spacer(1, 12))


########################################################


    # AGGIUNGO IL TITOLO "PERIODO DI RIFERIMENTO MESE 2023" AL CENTRO
    period_title = "PERIODO DI RIFERIMENTO MESE 2023"
    period_title_style = getSampleStyleSheet()["Title"]
    period_title_paragraph = Paragraph(period_title, period_title_style)
    story.append(period_title_paragraph)

    # CREO UNA LINEA DI SPAZIO SOTTO IL TITOLO
    story.append(Spacer(1, 12))


    # CREO UNA DESCRIZIONE PER OGNI BOX
    description1 = "N tot prev.Evasi"
    description2 = "N tot prev.Accettati"
    description3 = "N tot prev.acc.consuntivo"
    description4 = "Importo tot prev.Evasi"



    # CREO UNA TABELLA CON 4 QUADRATI CHE CONTENGONO DATI
    data = [
        [description1, description2, description3, description4],
        [str(prev_evasi_mes), str(prev_acc_mes), str(prev_acc_consuntivo), str(importo_tot_prev_evasi)]
    ]

    table_data = [[Paragraph(cell, getSampleStyleSheet()["Normal"]) for cell in row] for row in data]
    table = Table(table_data, colWidths=100, rowHeights=50)  # Decreased row heights

    # APPLICO LO STILE DELLE TABELLE PER UNO SFONDO BIANCO E LINEE NERE
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SIZE', (0, 0), (-1, -1), 36),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    story.append(table)

    # CREO UNA LINEA DI SPAZIO SOTTO IL TITOLO
    story.append(Spacer(1, 12))


###################################################


    # AGGIUNGO IL TITOLO "PERIODO DI RIFERIMENTO ANNO 2023" AL CENTRO
    year_title = "PERIODO DI RIFERIMENTO: ANNO 2023"
    year_title_style = getSampleStyleSheet()["Title"]
    year_title_paragraph = Paragraph(year_title, year_title_style)
    story.append(year_title_paragraph)

    # CREO UNA LINEA DI SPAZIO SOTTO IL TITOLO
    story.append(Spacer(1, 12))


    # CREO UNA TABELLA CON 2 BOX CONTENTI I VALORI 1 ALLA SINISTRA E 2 ALLA DESTRA (PER ADESSO)
    data2 = [
        ["N. Tot.Prev.Accettati", "Importo Tot.Prev.Accettati"],
        [str(prev_acc_anno), "2"]
    ]

    table_data2 = [[Paragraph(cell, getSampleStyleSheet()["Normal"]) for cell in row] for row in data2]
    table2 = Table(table_data2, colWidths=100, rowHeights=50)  # Decreased row heights

    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SIZE', (0, 0), (-1, -1), 36),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))


    story.append(table2)

    # CREO UNA LINEA DI SPAZIO SOTTO IL TITOLO
    story.append(Spacer(1, 12))


################################################


    # AGGIUNGO LA DESCRIZIONE "FATTURATO AD OGGI," "FATTURATO DA EMETTERE," E "FATTURATO PREVISTO 2023"
    # SOTTO LE BOX ESISTENTI
    description_left = "FATTURATO AD OGGI"
    description_center = "FATTURATO DA EMETTERE"
    description_right = "FATTURATO PREVISTO 2023"

    # CCREO UNA TABELLA CON TRE BOX CONTENENTI VALORI E DESCRIZIONI
    data3 = [
        [description_left, description_center, description_right],
        ["1", "2", "3"]
    ]

    table_data3 = [[Paragraph(cell, getSampleStyleSheet()["Normal"]) for cell in row] for row in data3]
    table3 = Table(table_data3, colWidths=100, rowHeights=50)  # Decreased row heights

    table3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SIZE', (0, 0), (-1, -1), 36),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    story.append(table3)


########################################################################################################################
#SECONDA PAGINA DEL PDF

    # AGGIUNGO UN PAGE BREAK PER INIZIARE UNA NUOVA PAGINA
    story.append(PageBreak())

    # CREO UN TITOLO PER LA NUOVA PAGINA
    second_page_title = "ANALISI OPERATIVA PROGETTI"
    second_page_title_style = getSampleStyleSheet()["Title"]
    second_page_title_paragraph = Paragraph(second_page_title, second_page_title_style)
    story.append(second_page_title_paragraph)

    # CREO UNA LINEA DI SPAZIO SOTTO IL TITOLO
    story.append(Spacer(1, 12))

    # CREO UNA TABELLA CON UNA SINGOLA CELLA CONTENTENTE IL VALORE "4"
    data4 = [
        ["4"]
    ]

    table_data4 = [[Paragraph(cell, getSampleStyleSheet()["Normal"]) for cell in row] for row in data4]
    table4 = Table(table_data4, colWidths=500, rowHeights=100)  # AGGIUSTA colWidths E rowHeights IN BASE ALLE NECESSITA'

    table4.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SIZE', (0, 0), (-1, -1), 36),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    story.append(table4)

    # CREO UNA LINEA DI SPAZIO SOTTO IL TITOLO
    story.append(Spacer(1, 12))

    # AGGIUNGO 2 TABELLE CON I VALORI "5" E "6"
    data5 = [
        ["5"]
    ]

    table_data5 = [[Paragraph(cell, getSampleStyleSheet()["Normal"]) for cell in row] for row in data5]
    table5 = Table(table_data5, colWidths=[500], rowHeights=[150])

    table5.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SIZE', (0, 0), (-1, -1), 36),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    story.append(table5)

    # CREO UNA LINEA DI SPAZIO SOTTO IL TITOLO
    story.append(Spacer(1, 12))

    data6 = [
        ["6"]
    ]

    table_data6 = [[Paragraph(cell, getSampleStyleSheet()["Normal"]) for cell in row] for row in data6]
    table6 = Table(table_data6, colWidths=[500], rowHeights=[200])

    table6.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SIZE', (0, 0), (-1, -1), 36),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    story.append(table6)


########################################################################################################################
#TERZA PAGINA DEL PDF


    # Add a page break to start a new page
    story.append(PageBreak())

    # Create a title for the second page
    third_page_title = "CONTROLLO DI GESTIONE"
    third_page_title_style = getSampleStyleSheet()["Title"]
    third_page_title_paragraph = Paragraph(third_page_title, third_page_title_style)
    story.append(third_page_title_paragraph)

    # Add some space below the second page title
    story.append(Spacer(1, 12))

    # Add four more tables with data "5," "6," "7," and "8"
    for data_value in ["5", "6", "7", "8"]:
        data = [
            [data_value]
        ]

        table_data = [[Paragraph(cell, getSampleStyleSheet()["Normal"]) for cell in row] for row in data]
        table = Table(table_data, colWidths=[400], rowHeights=[100])

        # Add some space below the second page title
        story.append(Spacer(1, 12))

        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('SIZE', (0, 0), (-1, -1), 36),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        story.append(table)


########################################################################################################################
#QUARTA PAGINA DEL PDF


    # Add a page break to start a new page
    story.append(PageBreak())

    # Add three more tables with data "9," "10," and "11"
    for data_value in ["9", "10", "11"]:
        data = [
            [data_value]
        ]

        table_data = [[Paragraph(cell, getSampleStyleSheet()["Normal"]) for cell in row] for row in data]
        table = Table(table_data, colWidths=[400], rowHeights=[100])

        # Add some space below the second page title
        story.append(Spacer(1, 12))

        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('SIZE', (0, 0), (-1, -1), 36),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        story.append(table)


    # Add some space below the fourth page title
    story.append(Spacer(1, 12))

    # Add the "OBIETTIVI 2023" and "COMMENTI" boxes
    data_objectives_comments = [
        ["OBIETTIVI 2023", "COMMENTI"],
        ["XXX", "XXX"]
    ]

    table_data_objectives_comments = [[Paragraph(cell, getSampleStyleSheet()["Normal"]) for cell in row] for row in data_objectives_comments]
    table_objectives_comments = Table(table_data_objectives_comments, colWidths=[300, 300], rowHeights=[50, 50])

    table_objectives_comments.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SIZE', (0, 0), (-1, -1), 36),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    story.append(table_objectives_comments)


########################################################################################################################

    # Build the PDF document
    doc.build(story)



#CHIAMO LA FUNZIONE DELLA TABELLA FATTA CON ALTAIR E LA METTO NELLA CASELLA 4

#CHIAMO LA FUNZIONE DELLA TABELLA FATTA CON ALTAIR E LA METTO NELLA CASELLA 5

#CHIAMO LA FUNZIONE DELLA TABELLA FATTA CON ALTAIR E LA METTO NELLA CASELLA 6

#CHIAMO LA FUNZIONE DELLA TABELLA FATTA CON ALTAIR E LA METTO NELLA CASELLA 7

#CHIAMO LA FUNZIONE DELLA TABELLA FATTA CON ALTAIR E LA METTO NELLA CASELLA 8

#CHIAMO LA FUNZIONE DELLA TABELLA FATTA CON ALTAIR E LA METTO NELLA CASELLA 9

#CHIAMO LA FUNZIONE DELLA TABELLA FATTA CON ALTAIR E LA METTO NELLA CASELLA 10

#CHIAMO LA FUNZIONE DELLA TABELLA FATTA CON ALTAIR E LA METTO NELLA CASELLA 11

#CHIAMO LA FUNZIONE OBIETTIVI E COMMENTI E LI INSERISCO NELLE BOX

#INSERISCO FOOTER PER OGNI PAGINA(PROBABILMENTE TUTTO COME IMMAGINE, INCLUSO IL TESTO)

if __name__ == "__main__":
    generate_pdf()







