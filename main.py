from os import path
from domanin.dataset_csv import DatasetCSV
from domanin.dataset_excel import DatasetExcel
from domanin.dataset_api import DatasetAPI
from data.data_saver import DataSaver
from domanin.dataset_json import DataJson

# ruta cvs
csv_path =  path.join(path.dirname(__file__),"files/Exportaciones_litio_csv")
excel_path =  path.join(path.dirname(__file__),"files/fondos_de_riesgo_xlsx")
json_path = path.join(path.dirname(__file__), "files/personajes_json")

#                     Cargar y modificar 

csv = DatasetCSV(csv_path) # ruta de acceso
# csv.cargar_datos()
# csv.mostrar_resumen()


excel = DatasetExcel(excel_path) # ruta de acceso
# excel.cargar_datos()
# excel.mostrar_resumen()

# api = DatasetAPI("https://apis.datos.gob.ar/georef/api/provincias")
# api.cargar_datos()

json=DataJson(json_path)
json.cargar_datos()
json.mostrar_resumen()

#                        guardar base de datos

db = DataSaver()
db.guardar_dataframe(csv.datos, "Exportaciones_litio_csv")
db.guardar_dataframe(excel.datos, "fondos_de_riesgo_xlsx")
db.guardar_dataframe(json.datos, "personajes_json")
#db.guardar_dataframe(api.datos, "api_pronvia")
