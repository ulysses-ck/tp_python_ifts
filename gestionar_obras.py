import pandas as pd
from peewee import *


class GestionarObras (Model):
	def __init__(self) -> None:
		self.__df_obras_publicas = self.extraer_datos()

	@property
	def df_obras_publicas(self):
		return self.__df_obras_publicas

	@df_obras_publicas.setter
	def df_obras_publicas(self, new_df):
		self.__df_obras_publicas = new_df

	def extraer_datos(self):
		try:
			df = pd.read_csv("./observatorio-de-obras-urbanas.csv")
			return df
		except FileNotFoundError as e:
			print("El archivo no existe o la ubicación del mismo es incorrecta", e)
			return None

	def conectar_db(self):
		sqlite_db_obras = SqliteDatabase("./obras_urbanas.db")
		try:
			sqlite_db_obras.connect()
			return sqlite_db_obras
		except OperationalError as e:
			print("Se ha generado un error en la conexión a la BD.", e)
			exit()

	def mapear_orm(self):
		pass

	def limpiar_datos(self):
		self.df_obras_publicas.dropna(subset=["entorno", "nombre", "etapa", "tipo", "area_responsable", "monto_contrato", "comuna", "barrio", "direccion", "fecha_inicio", "porcenta_avance", "licitacion_oferta_empresa", "licitacion_anio", "contratacion_tipo", "nro_contratacion", "cuit_contratista", "mano_obra"], axis=0, inplace=True)

	def cargar_datos(self):
		pass

	def nueva_obra(self):
		pass
