import requests
import json

def send_query(api_url, api_key, query):
    """
    Helper function to send the query to the API
        
    Args: 
        api_url: Url API.
        api_key: API key for monday.
        query: Query text string
    Return:
        response: The server response in dictionary format.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": api_key
    }
    data = {"query": query}

    print("Sending Data ......")
    response = requests.post(url=api_url, headers=headers, json=data)
    
    return response.json()


def create_item(api_url, api_key, id_key, item_name, column_replace):
    """
    Funtion for create a new item on monday

    Args: 
        api_url: Url API.
        api_key: API key for monday
        column_replace: New data
        id_key: Value fot board Id
        item_name : Give a new name to the new element
    Return:
        send_query: Send the query with the parameters that were sent to you
    """

    column_replace_json = json.dumps(column_replace)

    new_query = f"""
    mutation {{
        create_item (
            board_id : {id_key},
            item_name: "{item_name}",
            column_values: {json.dumps(column_replace_json)}
        ){{
        id
        }}
    }}
    """

    return send_query(api_url, api_key, new_query)


def create_subitem(api_url, api_key, parent_item_id, item_name, column_replace):
    """
    Funtion for create a new item on monday

    Args: 
        api_url: Url API.
        api_key: API key for monday
        column_replace: New data
        id_key: Value fot board Id
        item_name : Give a new name to the new element
    Return:
        send_query: Send the query with the parameters that were sent to you
    """

    column_replace_json = json.dumps(column_replace)

    new_query = f"""
    mutation {{
        create_subitem (
            parent_item_id: {parent_item_id},
            item_name: "{item_name}",
            column_values: {json.dumps(column_replace_json)}
        ){{
            id
        }}
    }}
    """

    return send_query(api_url, api_key, new_query)
