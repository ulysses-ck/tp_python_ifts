import pandas as pd
from peewee import *
from abc import ABCMeta
class GestionarObras(metaclass=ABCMeta):
	df_obras_publicas = None
	sqlite_db_obras = None

	@classmethod
	def extraer_datos(cls):
		try:
			df = pd.read_csv("./observatorio-de-obras-urbanas.csv")
			cls.df = df
		except FileNotFoundError as e:
			print("El archivo no existe o la ubicación del mismo es incorrecta", e)
			return None

	@classmethod
	def conectar_db(cls):
		sqlite_db_obras = SqliteDatabase("./obras_urbanas.db")
		try:
			sqlite_db_obras.connect()
			return sqlite_db_obras
		except OperationalError as e:
			print("Se ha generado un error en la conexión a la BD.", e)
			exit()

	@classmethod
	def mapear_orm(cls):
		print("mapear orm")

	@classmethod
	def limpiar_datos(cls, df):
		cls.df = df.dropna(subset=["entorno", "nombre", "etapa", "tipo", "area_responsable", "monto_contrato", "comuna", "barrio", "direccion", "fecha_inicio", "porcenta_avance", "licitacion_oferta_empresa", "licitacion_anio", "contratacion_tipo", "nro_contratacion", "cuit_contratista", "mano_obra"], axis=0, inplace=True)

	@classmethod
	def cargar_datos(cls):
		print("cargar datos")

	@classmethod
	def nueva_obra(cls):
		print("nueva obra")
