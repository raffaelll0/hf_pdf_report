import requests
import monday
import pandas

apiKey = monday.apiKey
apiUrl = monday.apiUrl
headers = monday.headers


#QUESTE FUNZIONI SERVONO AD ESTRARRE I DATI NUMERICI DEI PREVENTIVI

def n_tot_prev_accettati_anno():

    #query

    # data = monday.get_items(board...)
    #
    # #calcolo conteggio
    #
    # score = len(data)
    #
    # return (score)





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
    id_board_preventivi = '2286362496'

    query = 'query { boards (ids: ' + id_board_preventivi + ') {groups(ids:  ["nuovo_gruppo10114" "nuovo_gruppo89357"] ){ items_page (limit:500) { items { id name column_values(ids: "anno") { text value } } } } } }'
    data = {'query': query}

    # FACCIAMO UNA RICHIESTA JSON
    r = requests.post(url=apiUrl, json=data, headers=headers)

    # DEFINIAMO IL NOSTRO JSON CON LA VARIABILE response_data
    response_data = r.json()

    total_items = 0

    # Iterate through the "groups" list and count the items that have "anno" equal to "2023"
    for group in response_data['data']['boards'][0]['groups']:
        for item in group['items_page']['items']:
            for column_value in item['column_values']:
                if column_value['text'] == '2023':
                    total_items += 1


    return total_items

def n_tot_prev_accettati_mese():
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


def n_tot_prev_evasi_mese():
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


def n_tot_prev_acc_consuntivo():
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

    query = '{ boards(ids: 2286362496) { groups(ids: "nuovo_gruppo89357"){ items_page( query_params: {rules: [{column_id: "data", compare_value: ["2023-04-01", "2023-04-30"], operator: between}]} ) { items { id name } } } } }'

    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    response = r.json()

    if 'data' in response and 'boards' in response['data'] and 'groups' in response:
        items = response['data']['boards'][0]['groups']['items_page']['items']
        num_items = len(items)
    else:
        num_items = 0



    return num_items



def importo_tot_prev_evasi():
    """

    :return:
    """
    query = '{ boards(ids: 2286362496) { groups(ids: "topics" ) { items_page(limit:500 query_params: {rules: [{column_id: "dup__of_data_offerta_contabilt_", compare_value: ["2023-11-01", "2023-11-30"], operator: between}]} ) { items { id name column_values(ids: "_importo_offerta_") { text value } } } } } }'
    data = {'query': query}

    # FACCIAMO UNA RICHIESTA JSON
    r = requests.post(url=apiUrl, json=data, headers=headers)

    # DEFINIAMO IL NOSTRO JSON CON LA VARIABILE response_data
    response_data = r.json()
    tot = 0

    # Iterate through the "groups" list and count the items that have "anno" equal to "2023"
    for group in response_data['data']['boards'][0]['groups']:
        for item in group['items_page']['items']:
            for column_value in item['column_values']:
                if column_value['value']:
                    val = column_value['value'].replace('"', '')
                    tot = tot + int(val)
    return tot



def importo_tot_prev_accettati():
    """

    :return:
    """
    query = '{ boards(ids: 2286362496) { groups(ids: ["nuovo_gruppo10114" "nuovo_gruppo89357"]) { items_page( limit: 500 ) { items { id name column_values(ids: ["_importo_offerta_" "anno"]) { text value id} } } } } }'
    data = {'query': query}
    # FACCIAMO UNA RICHIESTA JSON
    r = requests.post(url=apiUrl, json=data, headers=headers)

    total_items = 0
    tot = 0

    # DEFINIAMO IL NOSTRO JSON CON LA VARIABILE response_data
    response_data = r.json()

    for group in response_data['data']['boards'][0]['groups']:
        for item in group['items_page']['items']:
            for column_value in item['column_values']:
                if column_value['text'] == '2023':
                    #print(column_value['value'])
                    total_items += 1

                    if column_value["id"] == "_importo_offerta_":
                        if column_value['value']:
                            val = column_value['value'].replace('"', '')
                            print(val)
                            tot = tot + float(val)


    print("tot items: ", total_items)
    print("tot: ", tot)

#Da sistemare

#importo_tot_prev_accettati()