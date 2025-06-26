import pandas as pd
from domanin.dataset import Dataset

class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
        
    def cargar_datos(self):
        try:
            df = pd.read_csv(self.fuente)
            
            if df.empty:
                print(f"El archivo csv {self.fuente} esta vacio" )
            
            
            self.datos = df
            print("Datos CSV cargado")
            
            if self.validar_datos():
                print("datos validos")
                self.transformar_datos()
            
            else:
                print(f"la validacion de csv fallo.")
                
        except FileNotFoundError:
            print(f"Archivo no encontrado {self.fuente}")
        except pd.errors.EmptyDataError:
            print(f"El archivo cvs {self.fuente} esta vacio o mal")
        except Exception as e:
            print(f"Error inesperado al cargar csv {e}")
            
            