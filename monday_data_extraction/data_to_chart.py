import requests
import monday
import altair as alt
import pandas as pd


apiKey = monday.apiKey
apiUrl = monday.apiUrl
headers = monday.headers

#QUESTE FUNZIONI SI BASANO DI ESTRARRE DATI DA MONDAY E DI CREARE 1 AD 1 I SINGOLI GRAFICI
# PER POI INSERIRLI NEL PDF GEN

def n_progetti_in_progress_su_pm():

    """
    questa funzione prenderà i dati da monday.com, essi verranno
    poi utilizzati per creare dei grafici tramite altair e la libreria pandas
    i grafici di questa funzione si troveranno nella seconda pagina del pdf

    Args:

    Returns:

    """
    query = 'query getItems{ boards (ids:[2286362570]) { items_page(limit:500 ){ cursor items{ id name column_values (ids:["person" "specchio_1"] ) { id text ... on MirrorValue { display_value } } } } } }'
    data = {'query': query}

    # FACCIAMO UNA RICHIESTA JSON
    r = requests.post(url=apiUrl, json=data, headers=headers)

    # DEFINIAMO IL NOSTRO JSON CON LA VARIABILE response_data
    response_data = r.json()

    #print(response_data)

    data = response_data['data']['boards'][0]['items_page']['items']

    # Create a list of dictionaries to store the data
    data_list = []

    # Loop through the data and count occurrences of 'person' and 'specchio_1'
    for item in data:
        person = item['column_values'][1]['text']
        specchio_1 = item['column_values'][0]['display_value']
        data_list.append({'person': person, 'specchio_1': specchio_1})

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)



    df = df.assign(specchio_1=df['specchio_1'].str.split(', ')).explode('specchio_1')
    # Remove leading/trailing whitespace and remove duplicates
    df['specchio_1'] = df['specchio_1'].str.strip()
    df = df.drop_duplicates().reset_index(drop=True)

    df = df.assign(person=df['person'].str.split(', ')).explode('person')
    # Remove leading/trailing whitespace and remove duplicates
    df['person'] = df['person'].str.strip()
    df = df.drop_duplicates().reset_index(drop=True)

    # Group by 'person' and 'specchio_1' and count occurrences
    result_df = df.groupby(['person', 'specchio_1']).size().reset_index(name='count')

    #display(result_df)

    # Create an Altair chart
    chart = alt.Chart(result_df).mark_bar().encode(
        x=alt.X('person', title='PM/SO'),
        y=alt.Y('count:Q', title='Conteggio'),
        color=alt.Color('specchio_1:N', title='BU')

    ).properties(
    width=400,  # Set your custom width
    height=250  # Set your custom height
    )

    chart_path = r'C:\Users\raffaele.loglisci\Desktop\altair_demo\monday_data_extraction\pngs_of_charts\chart.png'
    chart.save(chart_path)
    return chart_path





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


