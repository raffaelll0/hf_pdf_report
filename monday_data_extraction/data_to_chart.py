import requests
import monday
import altair as alt
import pandas


apiKey = monday.apiKey
apiUrl = monday.apiUrl
headers = monday.headers

#QUESTE FUNZIONI SI BASANO DI ESTRARRE DATI DA MONDAY E DI CREARE 1 AD 1 I SINGOLI GRAFICI
# PER POI UTILIZZARLI NEL PDF GEN

def m_progetti_in_progress_su_pm(item_data):


    #elaboro i dati in modo da ottenere una tabella utile per altair
    #suddivisi per pm, in pila per Business Unit
    # df = item_data.groupby(params...)
    # """
    # pm|BU|n_progetti
    # Raffaele Tardi|ConsImp|6
    # Raffaele Tardi|ConsIMM|4
    # """
    #
    # #genero grafico a barre impilate su altair
    # piled_bar_chart = alt.Chart(data=df,....)
    #
    #
    # return(piled_bar_chart)




    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """

    # data = item_data[0][colonna]
    #
    # grafico = data.qualche_funzione
    #
    # return(grafico)

    #3 HF-progetti

    #QUESTO SARA' UN GRAFICO A BARRE VERTICALI
    #definisco il tipo di grafico

    #DEFINISCO L'ASSE X CON I GLI UTENTI DELLA BOARD HF PROGETTI E DEFINISCO LA TIPOLOGIA DEL PROGETTO
    #faccio una query della board e filtro gli utenti e il tipo del progetto

    #dict1 = {'a': 1, 'b': 2, 'c': 3}
    #dict2 = {'b': 3, 'c': 4, 'd': 5}
    #dict3 = {'a': 1, 'b': 5, 'c': 7, 'd': 5}
    #questo controllo si basa su due dizionari ma siccome noi abbiamo un solo json dobbiamo fare il controllo all'interno




    #DOBBIAMO QUINDI CERCARE LA PERCENTUALE SU CUI UN UTENTE HA LAVORATO SU UN PROGETTO
    #NELL'ASSE Y INSERISCO IL NUMERO DI CONTEGGI, OVVERO IL NUMERO DI VOLTE IN CUI UN UTENTE HA LAVORATO SU UN PROGETTO

def data_extractor_graph_2():
    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """

    # items = monday.get_items(board="", item_ids=)
    #
    # data = items[0][colonna]
    #
    # grafico = data.qualche_funzione
    #
    # return(grafico)


    #3 HF-progetti
    #Importo Progetti In Progress per Anno

    #QUESTO SARA' UN GRAFICO A BARRE VERTICALI
    #SI BASA SULLA BOARD HF PROGETTI

    #NELL'ASSE X ABBIAMO GLI ANNI
    #qui possiamo fare una query per avere gli anni con l' importo accettato(colonna nascosta su monday):
    #dict = {"2022":"100" "2022":"200" "2023":"100"}
    #dobbiamo fare un controllo all'interno del dizionario per avere il risultato finale:
    #dict = {"2022":"200" "2023":"100"}

    #una volta ottenuto il json finale con i dati intersecati dobbiamo renderlo in output con altair

def data_extractor_graph_3():
    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """

    #3 HF-progetti
    #Portafoglio Ordine Residuo

    #QUESTO GRAFICO E UN GRAFICO A BARRE VERTICALI SIMILE A QUELLI PRECEDENTI MA CON UNA DIFFERENZA, OVVERO:
    #L'ASSE DELLE X SI BASA SU UN GRUPPO E NON PIU' SU UN ITEM QUINDI:
    #nella query definiamo il gruppo e aggiungiamo come value l'item importo accettato(colonna nascosta su monday)
    #qui l'unica cosa da fare è addizionare tutti gli importi accettati e definirli con altair nell'asse delle y

def data_extractor_graph_4():
    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """
    #T2 HF permessi/malattie
    #Analisi Ferie-Malattia-DayHospital - Dipendenti

    #QUESTO GRAFICO E' A BARRE VERTICALI
    #la query si basa su 2 colonne di monday, possiamo quindi utilizzare la query del primo grafico per poi cambiare
    #il nome delle colonne

def data_extractor_graph_5():
    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """
    #T2 HF permessi/malattie
    #Analisi Permessi/ROL - Dipendenti

    # QUESTO GRAFICO E' A BARRE VERTICALI
    # la query si basa su 4 colonne di monday, possiamo quindi utilizzare la query del primo grafico per poi cambiare
    # il nome delle colonne


def data_extractor_graph_6():
    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """
    #T2 HF permessi/malattie
    #Analisi Assenze Liberi Professionisti

    # QUESTO GRAFICO E' A BARRE VERTICALI
    # la query si basa su 1 colonna di monday, possiamo quindi utilizzare la query del primo grafico per poi cambiare
    # il nome delle colonne

def data_extractor_graph_7():
    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """
    #T2 HF permessi/malattie
    # Analisi Giornate Smart Working

    # QUESTO GRAFICO E' A BARRE VERTICALI
    # la query si basa su 4 colonne di monday, possiamo quindi utilizzare la query del primo grafico per poi cambiare
    # il nome delle colonne


def data_extractor_graph_8():
    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """
    #scheda monday: T5 HF rapportini
    #Time-Sheet marzo
    # QUESTO GRAFICO E' A BARRE VERTICALI

    #l'asse delle x sono gli utenti
    #l'asse delle y sono le ore rendicontate
    #bisogna filtrare le ore rendicontate in base al mese, quindi va fatto un controllo nella query
    #una volta fatto ciò bisogna capire come selezionare le ore rendicontate in base alal tipologia
    #quindi le ore e gli utenti devono essere raggruppati in base ad una tipologia di progetto monday





def data_extractor_graph_9():
    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """
    #scheda monday: T5 HF rapportini
    #BU / h

    #QUESTO GRAFICO E' UN GRAFICO A TORTA
    #dobbiamo calcolare la percentuale delle tipologie di progetto e metterle nel grafico, tutto ciò deve essere filtrato
    #in base ad un mese specifico


