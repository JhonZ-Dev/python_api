import requests
import pyodbc


# URL de la API
api_url = "http://localhost:8080/api"
# Realizar la solicitud GET a la API
response = requests.get(api_url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()  # Asumimos que la API devuelve un JSON
else:
    print(f"Error al acceder a la API: {response.status_code}")
    exit()

# Conexión a SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=tu_servidor;"
    "DATABASE=tu_base_de_datos;"
    "UID=tu_usuario;"
    "PWD=tu_contraseña"
)
cursor = conn.cursor()