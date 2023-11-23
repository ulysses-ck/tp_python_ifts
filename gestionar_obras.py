import pandas as pd
from utils import create_new_record

from peewee import *
from abc import ABCMeta
from modelo_orm import *
from typing import Optional

class GestionarObras(metaclass=ABCMeta):
	df_obras_publicas: pd.DataFrame = None
	sqlite_db_obras: Optional[SqliteDatabase] = None

	@classmethod
	def extraer_datos(cls):
		try:
			df = pd.read_csv("./observatorio-de-obras-urbanas.csv")
			return df
		except FileNotFoundError as e:
			print("El archivo no existe o la ubicación del mismo es incorrecta", e)
			return None

	@classmethod
	def conectar_db(cls):
		db_obras = SqliteDatabase("./obras_urbanas.db")
		try:
			db_obras.connect()
			return db_obras
		except OperationalError as e:
			print("Se ha generado un error en la conexión a la BD.", e)
			exit()

	@classmethod
	def mapear_orm(cls):
		cls.sqlite_db_obras.create_tables([TipoEntorno, TipoEtapa, TipoObra, TipoAreaResponsable, TipoContratacion, Empresa, Fechas, LicitacionOfertaEmpresa, TipoComuna, TipoBarrio, Obra])

	@classmethod
	def limpiar_datos(cls):
		cls.df_obras_publicas.dropna(subset=["entorno", "nombre", "etapa", "tipo", "area_responsable", "monto_contrato", "comuna", "barrio", "fecha_inicio", "licitacion_oferta_empresa", "contratacion_tipo", "nro_contratacion", "cuit_contratista"], axis=0, inplace=True)

	@classmethod
	def cargar_datos(cls):
		# TODO cargar los datos del csv a la tabla
		#lista donde pongo las columnas a traer para convertir en tablas unicas
		tablas_a_traer = [
			{ "name_column": "area_responsable",
				"table": TipoAreaResponsable,
				"property": "nombre"
				},
			{ "name_column": "contratacion_tipo",
				"table": TipoContratacion,
				"property": "tipo_contratacion"
				},
			{ "name_column": "comuna",
				"table": TipoComuna,
				"property":"numero"
				},
			{ "name_column": "entorno",
				"table": TipoEntorno,
				"property":"numero"
				},
			{ "name_column": "etapa",
				"table": TipoEtapa,
				"property":"nombre"
				},
			{ "name_column": "tipo",
				"table": TipoObra,
				"property": "nombre"
				},

			]
		#ciclo para buscar cada columna de la bd que coincida con el criterio de la lista y ponerlos
		#en una lista anidada
		for tabs in tablas_a_traer:
			datos_unicos_columna = list(cls.df_obras_publicas[tabs["name_column"]].unique())
			for dato in datos_unicos_columna:
				print(f"agregando {dato} de {tabs['name_column']} en {tabs['table']}")
				create_new_record(property=tabs["property"], table=tabs["table"], value=dato)


	@classmethod
	def nueva_obra(cls):
		# TODO crear nueva obra utilizando el modelo orm
		print("nueva obra")

	@classmethod
	def obtener_identificadores(cls):
		# TODO obtener indicadores segun corresponda
		# a. Listado de todas las áreas responsables.
		for registro in TipoAreaResponsable.select():
			print(registro)
		# b. Listado de todos los tipos de obra.
		for registro in TipoObra.select():
			print(registro)
		# c. Cantidad de obras que se encuentran en cada etapa.
		# hacer un join de Obra con TipoEtapa
		# Finalizada cuantos hay
		# Rescindida cuantos hay

		# d. Cantidad de obras y monto total de inversión (atributo financiamiento) por tipo de obra.


		# e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3.
		# f. Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1. (atributo financiamiento)
		# g. Cantidad de obras finalizadas en un plazo menor o igual a 24 meses.
		# h. Porcentaje total de obras finalizadas. (atributo etapa)
		# i. Cantidad total de mano de obra empleada.
		# j. Monto total de inversión. (atributo financiamiento)
		print("obtener indicadores")


gestionador_de_obras = GestionarObras()
gestionador_de_obras.extraer_datos()

GestionarObras.extraer_datos()
