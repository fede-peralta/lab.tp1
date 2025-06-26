import pandas as pd
from domanin.dataset import Dataset


class DatasetExcel(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
        
    def cargar_datos(self):
        try:
            df = pd.read_excel(self.fuente)
            
            if df.empty:
                print(f"Archivo Excel'{self.fuente} esta vacio")
                return
            
            self.datos = df
            if self.validar_datos():
                self.transformar_datos()
            else:
                print(f"Validacion fallida '{self.fuente}")
            
        except FileNotFoundError:
            print(f"Archivo no encontrado {self.fuente}")
        except ValueError as ve:
            print(f"Error de lectura {ve}")
        except Exception as e:
            print(f"Error inesperado al cargar csv {e}")