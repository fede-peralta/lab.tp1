import os
import pandas as pd
from domanin.dataset import Dataset


class DataJson(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
    
    def cargar_datos(self):
        if not os.path.exists(self.fuente):
            print(f"Archivbo no encontrado: {self.fuente}")
            return
        
        try:
            with open(self.fuente, 'r', encoding='utf-8') as archivo:
                self.datos = pd.read_json(archivo)
                print('Archivo Json cargado')
                
           
        except ValueError  as ve:
            print(f"Error de formato JSON: {ve}")
        
        except Exception as e:
            print(f"Error inesperado cargando JSON: {e}")
    
            
            
