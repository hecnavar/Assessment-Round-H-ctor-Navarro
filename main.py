import config
import requests
from api import create_item

def main():
    """
    Executable to add new elements
    
    """
    try:
        data = {
        "Edad": "24",
        "Fecha": "2025-08-02", 
        "Nombre": "Héctor Navarro",
        "Telefono" : "3342489386",
        "Correo": "hmnm0007@gmail.com",
        "Github": config.GIT_URL
        }

        column_replace = {
            config.COLUMS_ID["edad"]: str(data["Edad"]),
            config.COLUMS_ID["fecha"]: {"date":data["Fecha"]},
            config.COLUMS_ID["nombre"]:data["Nombre"],
            config.COLUMS_ID["telefono"]:{"phone":data["Telefono"]},
            config.COLUMS_ID["correo"]:{"email":data["Correo"],"text": "Correo Personal"},
            config.COLUMS_ID["github"]:{"url":data["Github"], "text": "Link Repo"}
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
