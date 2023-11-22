from typing import Optional
import pandas as pd
from peewee import *
from abc import ABCMeta
from modelo_orm import *

class GestionarObras(metaclass=ABCMeta):
	df_obras_publicas: pd.DataFrame = None
	sqlite_db_obras: Optional[SqliteDatabase] = None

	@classmethod
	def extraer_datos(cls):
		try:
			df = pd.read_csv("./observatorio-de-obras-urbanas.csv", sep=",")
			return df
		except FileNotFoundError as e:
			print("El archivo no existe o la ubicación del mismo es incorrecta", e)
			return None

	@classmethod
	def conectar_db(cls):
		sqlite_db_obras = SqliteDatabase("./obras_urbanas.db")
		try:
			sqlite_db_obras.connect()
			cls.sqlite_db_obras = sqlite_db_obras
		except OperationalError as e:
			print("Se ha generado un error en la conexión a la BD.", e)
			exit()

	@classmethod
	def mapear_orm(cls):
		cls.sqlite_db_obras.create_tables([TipoAreaResponsable, TipoContratacion, Empresa, LicitacionOfertaEmpresa, Fechas, TipoObra, TipoEtapa, TipoEntorno, TipoComuna, TipoBarrio, Obra])

	@classmethod
	def limpiar_datos(cls):
		cls.df_obras_publicas.dropna(subset=["entorno", "nombre", "etapa", "tipo", "area_responsable", "monto_contrato", "comuna", "barrio", "fecha_inicio", "licitacion_oferta_empresa", "contratacion_tipo", "nro_contratacion", "cuit_contratista"], axis=0, inplace=True)

	@classmethod
	def cargar_datos(cls):
		# TODO cargar los datos del csv a la tabla
		print("cargar datos")

	@classmethod
	def nueva_obra(cls):
		# TODO crear nueva obra utilizando el modelo orm
		print("nueva obra")

	@classmethod
	def obtener_identificadores(cls):
		# TODO obtener indicadores segun corresponda
		# a. Listado de todas las áreas responsables.
		# b. Listado de todos los tipos de obra.
		# c. Cantidad de obras que se encuentran en cada etapa.
		# d. Cantidad de obras y monto total de inversión (atributo financiamiento) por tipo de obra.
		# e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3.
		# f. Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1. (atributo financiamiento)
		# g. Cantidad de obras finalizadas en un plazo menor o igual a 24 meses.
		# h. Porcentaje total de obras finalizadas. (atributo etapa)
		# i. Cantidad total de mano de obra empleada.
		# j. Monto total de inversión. (atributo financiamiento)
		print("obtener indicadores")

