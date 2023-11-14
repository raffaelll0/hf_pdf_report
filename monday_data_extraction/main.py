import pdf_gen, data_to_score, data_to_chart, monday


def genera_report_hf():

    # prendiamo i dati
    # data_progetti = monday.get_items(board="21354315",
    #                               item_ids="[32193821]",
    #                               query_filter="{eqweq[21321]}")
    # data_attivita = monday.get_items(board="21354315",
    #                               item_ids="[32193821]",
    #                               query_filter="{eqweq[21321]}")
    # data_preventivi = monday.get_items(board="21354315",
    #                               item_ids="[32193821]",
    #                               query_filter="{eqweq[21321]}")
    #
    # # diamo i dati in pasto alle funzioni per generare Scores e Charts
    #
    # fatturato_annuo = data_to_score.fatturato_annuo(data_progetti)
    # fatturato_mensile = data_to_score.fatturato_mensile(data_progetti)
    # numero_dipendenti = data_to_score.numero_dipendenti(data_attivita)
    #
    # importo_progetti_inprogress_per_anno = data_to_chart.importo_progetti_inprogress_per_anno(data_preventivi)
    # importo_progetti_inprogress_per_mese = data_to_chart.importo_progetti_inprogress_per_mese(data_preventivi)


    # DATI data_to_score

    prev_evasi_mes = data_to_score.n_tot_prev_evasi_mese()
    prev_acc_mes = data_to_score.n_tot_prev_accettati_mese()
    prev_acc_consuntivo = data_to_score.prev_acc_consuntivo()
    prev_acc_anno = data_to_score.n_tot_prev_accettati_anno()
    importo_tot_prev_evasi = data_to_score.importo_tot_prev_evasi()
    importo_tot_prev_accettati = data_to_score.importo_tot_prev_accettati()
    fatturato_prev_2023 = data_to_score.fatturato_prev_2023()
    fatturato_ad_oggi = data_to_score.fatturato_ad_oggi()
    fatturato_da_emettere = data_to_score.fatturato_da_emettere()

    # DATI data_to_chart

    chart_progetti_in_progress_su_pm = data_to_chart.n_progetti_in_progress_su_pm()



    pdf = pdf_gen.generate_pdf(prev_evasi_mes,
                               prev_acc_mes,
                               prev_acc_consuntivo,
                               importo_tot_prev_evasi,
                               prev_acc_anno,
                               importo_tot_prev_accettati,
                               fatturato_prev_2023,
                               fatturato_ad_oggi,
                               fatturato_da_emettere,
                               chart_progetti_in_progress_su_pm
                               )

    return(pdf)

genera_report_hf()

def invia_mail(pdf):
    """

    :param pdf:
    :return:
    """

    #funzione_per_inviare_mail




# pdf = genera_report_hf()
# invia_mail(pdf)
