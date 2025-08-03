import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
GIT_URL = os.getenv("GIT_URL")

ID_KEY = 9708180507
PARENT_ITEM_ID = 9732279664
API_URL = "https://api.monday.com/v2/"

COLUMS_ID = {
    "edad": "numeric_mktb8zbj",
    "fecha": "date4",
    "nombre": "name",
    "telefono": "phone_mktbpkth",
    "correo": "email_mktb8jqh",
    "github": "link_mktbykh5"
}
