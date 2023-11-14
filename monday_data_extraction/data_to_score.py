import requests
import monday
import pandas as pd
import json

apiKey = monday.apiKey
apiUrl = monday.apiUrl
headers = monday.headers

#QUESTE FUNZIONI SERVONO AD ESTRARRE I DATI NUMERICI DEI PREVENTIVI
def get_items(board_ids: list, column_values_ids: list, group_ids: list = None, limit: int = 500,
              query_params_str: str = None, cursor: str = None):
    all_items = []

    if group_ids is None:
        group_ids_str = ""
        group_ids_closing = ""
    else:
        my_group_ids_str = "$my_group_ids: [String!]"
        group_ids_str = "{groups(ids:$my_group_ids)"
        group_ids_closing = "}"

    if query_params_str is None:
        query_params_str = ""
    else:
        query_params_str = f", query_params: {query_params_str}"

    while True:
        if cursor is None:
            cursor_str = ""
        else:
            cursor_str = f', cursor: "{cursor}"'
            # print(cursor_str)
            query_params_str = ""

        # Define the initial query to fetch the first set of data
        query = 'query ($my_board_id: [ID!]!, $my_colummn_values_ids: [String!], $my_limit: Int!' + my_group_ids_str + ') { boards(ids:$my_board_id)' + group_ids_str + ' { items_page(limit:$my_limit' + query_params_str + cursor_str + ') { cursor items { id name column_values(ids:$my_colummn_values_ids){id text value ... on MirrorValue { display_value }} } } }}' + group_ids_closing
        # print(query)
        vars = {
            'my_limit': limit,
            'my_board_id': board_ids,
            'my_query_params': query_params_str,
            'my_colummn_values_ids': column_values_ids,
            'my_group_ids': group_ids
        }

        data = {'query': query, 'variables': vars}

        # Make a request to the GraphQL endpoint
        r = requests.post(url=apiUrl, json=data, headers=headers)
        response_data = r.json()
        print(response_data)

        if group_ids is None:
            items = response_data['data']['boards'][0]['items_page']['items']
            cursor = response_data['data']['boards'][0]['items_page']['cursor']
        else:
            cursor = response_data['data']['boards'][0]['groups'][0]['items_page']['cursor']

            for n, id in enumerate(group_ids):
                items = response_data['data']['boards'][0]['groups'][n]['items_page']['items']
                all_items.extend(items)

        # Append items to the accumulated list
        all_items.extend(items)

        if limit != 500:
            break

        if cursor is None:
            break

    return (all_items)







def n_tot_prev_accettati_anno():
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
    query = '{ boards(ids: 2286362496) { groups(ids: ["nuovo_gruppo10114" "nuovo_gruppo89357"]) { items_page( limit: 500 ) { items { id name column_values(ids: ["dup__of_importo_offerta" "anno"]) { text value id} } } } } }'
    data = {'query': query}
    # FACCIAMO UNA RICHIESTA JSON
    r = requests.post(url=apiUrl, json=data, headers=headers)

    total_sum = 0.0

    # DEFINIAMO IL NOSTRO JSON CON LA VARIABILE response_data
    response_data = r.json()

    # Iterate through the items and calculate the sum
    for group in response_data["data"]["boards"][0]["groups"]:
        for item in group["items_page"]["items"]:
            for column in item["column_values"]:
                if column["id"] == "anno" and column["text"] == "2023":
                    for col in item["column_values"]:
                        if col["id"] == "dup__of_importo_offerta":
                            total_sum += float(col["text"])

    rounded_total_sum = round(total_sum, 2)

    return rounded_total_sum

#BISOGNA AGGIUNGERE LA SOMMA DELLA COLONNA DATA EMISSIONE
def fatturato_prev_2023():
    total_sum = 0  # Initialize a variable to store the total sum

    # make the queries
    date4_items = get_items(board_ids=[2430432761],
                            query_params_str='{rules: [{column_id: "date4", compare_value: ["2023-01-01", "2023-12-31"], operator: between}]}',
                            column_values_ids=["numeri"]
                            )

    dup__of_data_prevista_items = get_items(board_ids=[2430432761],
                                            query_params_str='{rules: [{column_id: "dup__of_data_prevista", compare_value: ["2023-01-01", "2023-12-31"], operator: between}]}',
                                            column_values_ids=["numeri"]
                                            )

    # Merge the two lists based on 'id'
    merged_json = {item['id']: item for item in date4_items + dup__of_data_prevista_items}.values()

    # calculate the total sum
    for item in merged_json:
        numeri_value = item['column_values'][0].get('value')  # Assuming 'value' is the key for the numeri field
        try:
            numeri_value = numeri_value.strip('"')  # Remove double quotes
            total_sum += float(numeri_value)
        except (ValueError, TypeError):
            print("Warning: Could not convert '{0}' to float. Skipping this value.".format(numeri_value))

    rounded_total_sum = round(total_sum, 2)
    print("Total Sum until cursor is None:", rounded_total_sum)

    return rounded_total_sum


fatturato_prev_2023()



#ANCHE QUI BISOGNA AGGIUNGERE LA SOMMA DELLA COLONNA DATA EMISSIONE
def fatturato_ad_oggi():
    query = ' { boards(ids: 2430432761) { groups(ids: "group_title") { id items_page( limit: 500 query_params: {rules: [{column_id: "date4", compare_value: ["2023-01-01", "2023-12-31"], operator: between}]} ) { cursor items { id name column_values(ids: "numeri") { value text } } } } } }'
    total_sum = 0
    processed_items = set()

    while True:
        response = requests.post(url=apiUrl, headers=headers, json={'query': query})
        data = response.json()

        for group in data['data']['boards'][0]['groups']:
            for item in group['items_page']['items']:
                item_id = item['id']
                if item_id not in processed_items:
                    text_value = item['column_values'][0]['text']
                    if text_value is not None:
                        value = float(text_value)
                        total_sum += value
                        processed_items.add(item_id)

        cursor = data['data']['boards'][0]['groups'][-1]['items_page']['cursor']
        if cursor is None:
            break

        query = query.replace(f'"{cursor}"', 'null')



    rounded_total_sum = round(total_sum, 2)
    print('Total Sum:', rounded_total_sum)






    return rounded_total_sum


fatturato_ad_oggi()


#funzionante, vanno settati i gruppi come variabili globali
def fatturato_da_emettere():

    query = ' { boards(ids: 2430432761) { groups( ids: ["topics", "nuovo_gruppo", "nuovo_gruppo74022", "duplicate_of_0__fatture_in_def"] ) { id items_page( limit: 500 ) { cursor items { id name column_values(ids: "numeri") { value text } } } } } } '
    total_sum = 0
    processed_items = set()


    while True:
        response = requests.post(url=apiUrl, headers=headers, json={'query': query})
        data = response.json()

        for group in data['data']['boards'][0]['groups']:
            for item in group['items_page']['items']:
                item_id = item['id']
                if item_id not in processed_items:
                    text_value = item['column_values'][0]['text']
                    if text_value is not None:
                        value = float(text_value)
                        total_sum += value
                        processed_items.add(item_id)

        cursor = data['data']['boards'][0]['groups'][-1]['items_page']['cursor']
        if cursor is None:
            break

        query = query.replace(f'"{cursor}"', 'null')

    rounded_total_sum = round(total_sum, 2)

    return rounded_total_sum



