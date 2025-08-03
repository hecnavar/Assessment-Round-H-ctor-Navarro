import requests
import json

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

    headers = {
    "Content-Type": "application/json",
    "Authorization": api_key
    }

    new_data = {"query": new_query}

    print("Sending Data ......")
    response = requests.post(url=api_url, headers=headers, json=new_data)

    return response.json()
