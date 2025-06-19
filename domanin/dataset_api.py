import requests # para comunicarnos a traves de internet
import pandas as pd
from domanin.dataset import Dataset

class DatasetAPI(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
    
    def cargar_datos(self):
        
        try:
            response = requests.get(self.fuente)
            if response.status_code == 200:
                df = pd.json_normalize(response.json())
            
                #verificar si un valor es una lista
                def es_lista(x):
                    return isinstance(x,list)
            
                #c convertir columnas tipo list a string
                def lista_a_string(x):
                    if isinstance(x,list):
                        return ' , '.join(map(str, x))
            
                for col in df.columns:
                    if df[col].apply(es_lista).any():
                        df[col] = df[col].apply(lista_a_string )
                    
                self.datos = df
                print(self.datos)
                print('api cargada')
            
                if self.validar_datos():
                    self.transformar_datos()
            else:
                print('Error api cargada')
            
                
            
        except Exception as e:
            print(f'Error API.{e}')