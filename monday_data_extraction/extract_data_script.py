import requests


apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE0NTc5NTQ4MywiYWFpIjoxMSwidWlkIjoyNzk4NzQzMywiaWFkIjoiMjAyMi0wMi0xNFQwODoyOTo0NC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTExOTUwMTIsInJnbiI6InVzZTEifQ.j052k96lwfIBOtLGWng2xmZul4c_rWnguMOTduJ95DM"
apiUrl = "https://api.monday.com/v2"

#CI SONO DUE HEADERS POICHE' headers SPECIFICA L'ULTIMA VERSIONE, CHE SERVE PER DETERMINATE QUERY'
#QUESTO PROBLEMA VA RISOLTO INFATTI ANCHE LA FUNZIONE extract_prev_acc_anno() DEVE UTILIZZARE headers e non headers_old
headers = {
    'Content-Type': 'application/json',
    'Authorization': apiKey,
    'API-Version': '2023-10'

}
headers_old = {
    'Authorization': apiKey

}


#QUESTE FUNZIONI SERVONO AD ESTRARRE I DATI NUMERICI DEI PREVENTIVI

def extract_prev_acc_anno():
    """
    Questa funzione estrae i dati da una board di monday.com,
    i dati estrapolati nello specifico sono i numero di preventivi accettati in un anno,
    viene fatto un controllo tramite query, dove vengono definite due date (inizio-fine)

    la funzione deve essere revisionata poichè non sono ancora state messe le date

    una volta estrapolati i dati essi verranno usati nel file pdf_gen
    i dati più complicati (per grafici) verranno estrapolati da un'altra funzione

    Args:
        data: parsed json of the data that the webhook gives
        challenge: is in a dictionary and contains a value(int)

    Returns:
        number_of_ids
    """
    # CODICE DELLA BOARD
    id_board_commessa = '2286362496'

    query = ''' { boards(ids: 2286362496) { groups(ids: "topics") { items (limit: 20000) { id } } } } '''
    data = {'query': query}

    # FACCIAMO UNA RICHIESTA JSON
    r = requests.post(url=apiUrl, json=data, headers=headers_old)

    # DEFINIAMO IL NOSTRO JSON CON LA VARIABILE response_data
    response_data = r.json()

    #INDICA IL NUMERO DI ID NEL GRUPPO
    id_list = [item['id'] for item in response_data['data']['boards'][0]['groups'][0]['items']]

    # Count the number of 'id' entries
    number_of_ids = len(id_list)


    return number_of_ids


def extract_prev_acc_mese():
    """
        Questa funzione estrae i dati da una board di monday.com,
        i dati estrapolati nello specifico sono i numero di preventivi accettati in un mese,
        viene fatto un controllo tramite query, dove vengono definite due date (inizio mese-fine mese)

        una volta fatto ciò viene fatto un controllo per vedere quanti items sono presenti, quindi poi
        questo dato verrà salvato


        una volta estrapolati i dati essi verranno usati nel file pdf_gen
        i dati più complicati (per grafici) verranno estrapolati da un'altra funzione

        Returns:
            num_items
        """

    query = '{boards(ids: 2286362496) {items_page(query_params: {rules: [{column_id: "data", compare_value: ["2023-11-01", "2023-11-30"], operator: between}]} ) {items{id name}}}}'
    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    response = r.json()

    if 'data' in response and 'boards' in response['data']:
        items = response['data']['boards'][0]['items_page']['items']
        num_items = len(items)
    else:
        print("No data found in the response.")

    return num_items


def extract_prev_evasi_mese():
    """
            Questa funzione estrae i dati da una board di monday.com,
            i dati estrapolati nello specifico sono i numero di preventivi evasi in un mese,
            viene fatto un controllo tramite query, dove vengono definite due date (inizio mese-fine mese)
            stavolta però i dati che ci servono sono filtrati in base ad un altro tipo di colonna
            ovvero: column_id:"dup__of_data_offerta_contabilt_"


            una volta fatto ciò viene fatto un controllo per vedere quanti items sono presenti, quindi poi
            questo dato verrà salvato


            una volta estrapolati i dati essi verranno usati nel file pdf_gen
            i dati più complicati (per grafici) verranno estrapolati da un'altra funzione

            Args:
                data: parsed json of the data that the webhook gives
                challenge: is in a dictionary and contains a value(int)

            Returns:
                num_items
            """
    query = '{boards(ids: 2286362496) {items_page(query_params: {rules: [{column_id: "dup__of_data_offerta_contabilt_", compare_value: ["2023-11-01", "2023-11-30"], operator: between}]} ) {items{id name}}}}'

    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    response = r.json()

    if 'data' in response and 'boards' in response['data']:
        items = response['data']['boards'][0]['items_page']['items']
        num_items = len(items)
    else:
        print("No data found in the response.")

    return num_items


def extract_prev_acc_consuntivo():
    """
            Questa funzione estrae i dati da una board di monday.com,
            i dati estrapolati nello specifico sono i numero di preventivi accettati in consuntivo,
            viene fatto un controllo tramite query, dove vengono definite due date (inizio mese-fine mese)
            stavolta però i dati che ci servono sono filtrati in base ad un altro tipo di colonna e anche in
            un altro gruppo
            ovvero: column_id:"dup__of_data_offerta_contabilt_"
                    groups(ids: "nuovo_gruppo89357")


            una volta fatto ciò viene fatto un controllo per vedere quanti items sono presenti, quindi poi
            questo dato verrà salvato


            una volta estrapolati i dati essi verranno usati nel file pdf_gen
            i dati più complicati (per grafici) verranno estrapolati da un'altra funzione

            Args:
                data: parsed json of the data that the webhook gives
                challenge: is in a dictionary and contains a value(int)

            Returns:
                num_items
            """

    query = '{ boards(ids: 2286362496) { groups(ids: "nuovo_gruppo89357"){ items_page( query_params: {rules: [{column_id: "data", compare_value: ["2023-11-01", "2023-11-30"], operator: between}]} ) { items { id name } } } } }'

    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    response = r.json()

    if 'data' in response and 'boards' in response['data'] and 'groups' in response:
        items = response['data']['boards'][0]['groups']['items_page']['items']
        num_items = len(items)
    else:
        num_items = 0



    return num_items


def extract_prev_acc_tot():
    """
            Questa funzione estrae i dati da una board di monday.com,
            i dati estrapolati nello specifico sono il numero tot di preventivi accettati in un anno,
            viengono fatti due controlli tramite query, dove vengono definite due date (inizio anno-fine anno)
            stavolta però i dati che ci servono sono filtrati in base ad un altro tipo di colonna e anche in
            un altro gruppo
            ovvero per la prima query: column_id:"data"
                                        groups(ids: "nuovo_gruppo10114")

            ovvero per la seconda query: column_id:"data"
                                         groups(ids: "nuovo_gruppo89357")


            una volta fatto ciò viene fatto un controllo per vedere quanti items sono presenti in entrambe le query,
            essi verranno addizionati tra di loro e salvati un una variabile


            una volta estrapolati i dati essi verranno usati nel file pdf_gen
            i dati più complicati (per grafici) verranno estrapolati da un'altra funzione

            !IL CODICE DI QUESTA FUNZIONE E' DA REVISIONARE POICHE'
            !I DATI RISULTANO MAGGIORI DI QUANTO DOVREBBERO ESSERE

            Args:
                data: parsed json of the data that the webhook gives
                challenge: is in a dictionary and contains a value(int)

            Returns:
                tot
            """

    query = '{ boards(ids: 2286362496) { groups(ids: "nuovo_gruppo10114" ) { items_page(limit:500 query_params: {rules: [{column_id: "data", compare_value: ["2023-01-01", "2023-11-06"], operator: between}]} ) { items { id  } } } } }'

    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    response = r.json()

    # INDICA IL NUMERO DI ID NEL GRUPPO
    id_list = [item['id'] for item in response['data']['boards'][0]['groups'][0]['items_page']['items']]

    # Count the number of 'id' entries
    number_of_ids = len(id_list)
    print(number_of_ids)
#####################################################################
    #QUERY PER LA SCHEDA A CONSUNTIVO

    query_consuntivo = '{ boards(ids: 2286362496) { groups(ids: "nuovo_gruppo89357" ) { items_page(limit:500 query_params: {rules: [{column_id: "data", compare_value: ["2023-01-01", "2023-11-06"], operator: between}]} ) { items { id  } } } } }'

    data_consuntivo = {'query': query_consuntivo}
    r_consuntivo = requests.post(url=apiUrl, json=data_consuntivo, headers=headers)
    response_consuntivo = r_consuntivo.json()

    # INDICA IL NUMERO DI ID NEL GRUPPO
    id_list_consuntivo = [item['id'] for item in response_consuntivo['data']['boards'][0]['groups'][0]['items_page']['items']]

    # Count the number of 'id' entries
    number_of_ids_consuntivo = len(id_list_consuntivo)
    print(number_of_ids_consuntivo)


    tot = number_of_ids + number_of_ids_consuntivo
    print(tot)


    return tot
extract_prev_acc_tot()




