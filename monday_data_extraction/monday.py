import requests
apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE0NTc5NTQ4MywiYWFpIjoxMSwidWlkIjoyNzk4NzQzMywiaWFkIjoiMjAyMi0wMi0xNFQwODoyOTo0NC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTExOTUwMTIsInJnbiI6InVzZTEifQ.j052k96lwfIBOtLGWng2xmZul4c_rWnguMOTduJ95DM"
apiUrl = "https://api.monday.com/v2"
headers = {
    'Content-Type': 'application/json',
    'Authorization': apiKey,
    'API-Version': '2023-10'
}



def get_items (board:str,item_ids:str,query_filter:str):
    """

    :param board:
    :param item_ids:
    :param query_filter:
    :return:
    """


    # query..........
    # data = query
    #
    # return(data)