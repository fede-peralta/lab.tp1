from os import path
from domanin.dataset_csv import DatasetCSV
from domanin.dataset_excel import DatasetExcel
from domanin.dataset_api import DatasetAPI
from data.data_saver import DataSaver


# ruta cvs
csv_path =  path.join(path.dirname(__file__),"files/Exportaciones_litio_csv")
excel_path =  path.join(path.dirname(__file__),"files/fondos_de_riesgo_xlsx")

#                     Cargar y modificar 

csv = DatasetCSV(csv_path) # ruta de acceso
csv.cargar_datos()
csv.mostrar_resumen()


excel = DatasetExcel(excel_path) # ruta de acceso
excel.cargar_datos()
excel.mostrar_resumen()

api = DatasetAPI("https://apis.datos.gob.ar/georef/api/provincias")
api.cargar_datos()

#                        guardar base de datos

db = DataSaver()
db.guardar_dataframe(csv.datos, "Exportaciones_litio_csv")
db.guardar_dataframe(excel.datos, "fondos_de_riesgo_xlsx")
#db.guardar_dataframe(api.datos, "api_pronvia")
