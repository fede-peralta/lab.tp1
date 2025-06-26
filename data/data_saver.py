import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from decouple import config


class DataSaver:
    def __init__(self):
    
        try:
            user = config('DB_USER')
            password = config('DB_PASSWORD')
            host = config('DB_HOST')
            port = config('DB_PORT')
            database = config('DB_NAME')
        
            url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
            self.engine = create_engine(url)
            print("Conexion a la base creada satisfactoriamente")
        except KeyError as e:
            print(f"variables de entorno faltantes: {e}")
        except Exception as e:
            print(f"Error al crar conexion de datos: {e}")
        
    def guardar_dataframe(self, df , nombre_tabla):
        if df is None:
            print(f"No se puede guardar: datos vacios para {nombre_tabla}")
            return
        
        if not isinstance(df, pd.DataFrame):
            print(f"tipo invalido: se esperaba un DataFrame, se recibio {type(df)}.")
            return
        
        if df.empty:
            print(f"DataFrame vacio: no se guardo la tabla {nombre_tabla}")
            return
        
        try:  
            df.to_sql(nombre_tabla, con=self.engine, if_exists='replace', index=False)
            print(f"datos guardados en tabla: {nombre_tabla}")
        
        except SQLAlchemyError as e:
            print(f"Error guardando datos: {e}")  
            
        except OperationalError as e:
            print(f"Error operacional: {e}")
        
        except Exception as e :
            print(f"Error inesparado guardado en base de datos: {e}")
            
            
