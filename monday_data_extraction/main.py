import pdf_gen, data_to_score, data_to_chart, monday


def genera_report_hf():


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
