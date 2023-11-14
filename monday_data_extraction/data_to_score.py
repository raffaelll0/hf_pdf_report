import requests
import monday
import pandas as pd
from monday import first_and_last_day_of_year, get_first_and_last_day_of_current_month

apiKey = monday.apiKey
apiUrl = monday.apiUrl
headers = monday.headers

get_items = monday.get_items
#first_and_last_day_of_year = monday.first_and_last_day_of_year()

#QUESTE FUNZIONI SERVONO AD ESTRARRE I DATI NUMERICI DEI PREVENTIVI


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


def prev_acc_consuntivo():
    first_day, last_day = get_first_and_last_day_of_current_month()

    # make the query
    items = get_items(board_ids=[2286362496],
                      query_params_str='{rules: [{column_id: "data", compare_value: ["' + first_day + '", "' + last_day + '"], operator: between}]}',
                      column_values_ids=["anno"],
                      group_ids=["nuovo_gruppo89357"],
                      # limit=5
                      )

    data_list = []
    for item in items:
        id = item['id']
        anno = item['column_values'][0]['text']

        data_list.append({'id': id, 'anno': anno})

    df = pd.DataFrame(data_list)
    df = df.drop_duplicates().reset_index(drop=True)

    count = len(df)

    return count



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

def fatturato_prev_2023():

    first_day, last_day = first_and_last_day_of_year()
    total_sum = 0  # Initialize a variable to store the total sum

    # make the queries
    date4_items = get_items(board_ids=[2430432761],
                            query_params_str='{rules: [{column_id: "date4", compare_value: ["' + first_day + '", "' + last_day + '"], operator: between}]}',
                            column_values_ids=["numeri"]
                            )

    dup__of_data_prevista_items = get_items(board_ids=[2430432761],
                                            query_params_str='{rules: [{column_id: "dup__of_data_prevista", compare_value: ["' + first_day + '", "' + last_day + '"], operator: between}]}',
                                            column_values_ids=["numeri"]
                                            )

    # Merge the two lists based on 'id'
    merged_json = {item['id']: item for item in date4_items + dup__of_data_prevista_items}.values()

    # calculate the total sum
    for item in merged_json:
        numeri_value = item['column_values'][0].get('value')  # Assuming 'value' is the key for the numeri field
        try:
            if numeri_value:
                numeri_value = numeri_value.strip('"')  # Remove double quotes
                total_sum += float(numeri_value)
        except (ValueError, TypeError):
            print("Warning: Could not convert '{0}' to float. Skipping this value.".format(numeri_value))

    rounded_total_sum = round(total_sum, 2)
    #print("Total Sum until cursor is None:", rounded_total_sum)



    return rounded_total_sum





#ANCHE QUI BISOGNA AGGIUNGERE LA SOMMA DELLA COLONNA DATA EMISSIONE
def fatturato_ad_oggi():
    total_sum = 0  # Initialize a variable to store the total sum

    first_day, last_day = first_and_last_day_of_year()

    # make the queries
    date4_items = get_items(board_ids=[2430432761],
                            query_params_str='{rules: [{column_id: "date4", compare_value: ["' + first_day + '", "' + last_day + '"], operator: between}]}',
                            column_values_ids=["numeri"],
                            group_ids=["group_title"]

                            )

    dup__of_data_prevista_items = get_items(board_ids=[2430432761],
                                            query_params_str='{rules: [{column_id: "dup__of_data_prevista", compare_value: ["' + first_day + '", "' + last_day + '"], operator: between}]}',
                                            column_values_ids=["numeri"],
                                            group_ids=["group_title"]
                                            )

    # Merge the two lists based on 'id'
    merged_json = {item['id']: item for item in date4_items + dup__of_data_prevista_items}.values()

    # calculate the total sum
    for item in merged_json:
        numeri_value = item['column_values'][0].get('value')  # Assuming 'value' is the key for the numeri field
        try:
            if numeri_value:
                numeri_value = numeri_value.strip('"')  # Remove double quotes
                total_sum += float(numeri_value)
        except (ValueError, TypeError):
            print("Warning: Could not convert '{0}' to float. Skipping this value.".format(numeri_value))

    rounded_total_sum = round(total_sum, 2)
    print(rounded_total_sum)
    return rounded_total_sum




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



