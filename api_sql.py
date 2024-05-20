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


# Supongamos que los datos obtenidos son una lista de diccionarios
# y queremos insertar cada diccionario en una tabla llamada 'api_data'
insert_query = """
    INSERT INTO api_data (campo1, campo2, campo3)
    VALUES (?, ?, ?)
"""

for item in data:
    cursor.execute(insert_query, item['campo1'], item['campo2'], item['campo3'])

# Confirmar la transacción
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()
print("Datos insertados correctamente en la base de datos.")
