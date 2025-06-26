'''clase base. '''
from abc import ABC, abstractmethod
import pandas as pd


# definimos la estructura
class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    @property
    
    def datos(self):
        return self.__datos
   
    @datos.setter 
    def datos( self, value):
        self.__datos = value
        
    @property
    def fuente(self):
        return self.__fuente
        

    @abstractmethod  # --> este meftodo obliga a python a que las subclases implenten este metodo
    def cargar_datos(self):
        pass

    def validar_datos(self):
        if self.datos is None:
            raise ValueError("No hay datos")
        
        if self.datos.isnull().sum().sum() > 0:
            print("faltante de datos")
        
        if self.datos.duplicated().sum() > 0:
            print("datos duplicado")
        
        if self.datos.empty:
            raise ValueError("DF vacio ")
            
        return True

    def transformar_datos(self):
        try:
            
            if self.datos is not None:
            # estandarizacon de columanas. Mismo tamano de texto
            
                self.__datos.columns = self.datos.columns.str.lower().str.replace(" " , "_")
            
            #eliminamos datos duplicados
                self.__datos = self.datos.drop_duplicates()
            
            #convertir objeto a texto plano"
                for col in self.datos.select_dtypes(include="object").columns:
                    self.__datos[col] = self.datos[col].astype(str).str.strip()
                print("Modificacion exitosa")
            
            else:
                print('No existe datos para su modicicacion/')
                
        except AttributeError as e:
            print(f"Error: el objeto 'datos' no tiene el formato. {e}")
            
        except TypeError as e:
            print(f"Error de tipo: probablemente hay un dato mal formateado. {e}")
        
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
            
                
            
            
    def mostrar_resumen(self):
        return print(self.datos.describe(include='all') if self.datos is not None else "No hay datos")