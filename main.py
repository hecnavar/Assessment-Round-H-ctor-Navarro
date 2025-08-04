import config
import requests
from api import create_item

def main():
    """
    Executable to add new elements
    
    """
    try:
        data = {
        "AGE": "24",
        "DATE": "2025-08-02", 
        "NAME": "Héctor Navarro",
        "PHONE" : "3342489386",
        "CORREO": "hmnm0007@gmail.com",
        "GITHUB": config.GIT_URL
        }

        column_replace = {
            config.COLUMS_ID["edad"]: str(data["AGE"]),
            config.COLUMS_ID["fecha"]: {"date":data["DATE"]},
            config.COLUMS_ID["nombre"]:data["NAME"],
            config.COLUMS_ID["telefono"]:{"phone":data["PHONE"]},
            config.COLUMS_ID["correo"]:{"email":data["CORREO"],"text": "Correo Personal"},
            config.COLUMS_ID["github"]:{"url":data["GITHUB"], "text": "Link Repo"}
        }

        result = create_item(api_url=config.API_URL, 
                            api_key=config.API_KEY,
                            id_key=config.ID_KEY,
                            item_name=data["Nombre"],
                            column_replace=column_replace)
        
        print("Waiting for connection .....")
        print(result)

        if "errors" not in result:
            print("\n New element add")
        else:
            print("Error to add element")

    except KeyError as e:
        print("Error in configuration")
        
if __name__ == "__main__":
    main()
