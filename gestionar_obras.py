import pandas as pd
from utils import *

from peewee import *
from abc import ABCMeta
from modelo_orm import *
from typing import Optional
from usuario_menu import *


SEPARATOR_LINE = "==================================="

class GestionarObras(metaclass=ABCMeta):
	df_obras_publicas: pd.DataFrame = None
	sqlite_db_obras: Optional[SqliteDatabase] = None

	@classmethod
	def extraer_datos(cls):
		try:
			print(SEPARATOR_LINE)
			print("Extrayendo csv")
			print(SEPARATOR_LINE)
			df = pd.read_csv("./observatorio-de-obras-urbanas.csv")
			return df
		except FileNotFoundError as e:
			print("El archivo no existe o la ubicación del mismo es incorrecta", e)
			return None

	@classmethod
	def conectar_db(cls):
		db_obras = SqliteDatabase("./obras_urbanas.db")
		try:
			print(SEPARATOR_LINE)
			print("Conectando Base de Datos")
			print(SEPARATOR_LINE)
			db_obras.connect()
			return db_obras
		except OperationalError as e:
			print("Se ha generado un error en la conexión a la BD.", e)
			exit()

	@classmethod
	def mapear_orm(cls):
		print(SEPARATOR_LINE)
		print("Creando Bases de Datos")
		print(SEPARATOR_LINE)
		cls.sqlite_db_obras.create_tables([TipoEntorno, TipoEtapa, TipoObra, TipoAreaResponsable, TipoContratacion, Empresa, Fechas, LicitacionOfertaEmpresa, TipoComuna, TipoBarrio, Obra])

	@classmethod
	def limpiar_datos(cls):
		print(SEPARATOR_LINE)
		print("Limpiando datos")
		print(SEPARATOR_LINE)
		cls.df_obras_publicas.dropna(subset=["entorno", "nombre", "etapa", "tipo", "area_responsable", "monto_contrato", "comuna", "barrio", "fecha_inicio", "licitacion_oferta_empresa", "contratacion_tipo", "nro_contratacion", "cuit_contratista"], axis=0, inplace=True)

	@classmethod
	def cargar_datos(cls):
		print(SEPARATOR_LINE)
		print("Cargando base de datos")
		print(SEPARATOR_LINE)

		print(SEPARATOR_LINE)
		print("cargando tablas con valores unicos")
		print(SEPARATOR_LINE)
		crear_tablas_con_valores_unicos(cls.df_obras_publicas)

		print(SEPARATOR_LINE)
		print("cargando barrios")
		print(SEPARATOR_LINE)
		rellenar_tablas_barrios(cls.df_obras_publicas)

		print(SEPARATOR_LINE)
		print("cargando Empresas")
		print(SEPARATOR_LINE)
		rellenar_tablas_empresas(cls.df_obras_publicas)

		print(SEPARATOR_LINE)
		print("cargando licitaciones y obras")
		print(SEPARATOR_LINE)
		# cargando tablas licitacion_oferta_empresa y obras_publicas

		# obteniendo los datos unicos existentes en cuit_contratista
		# datos
		for registro_completo in cls.df_obras_publicas.values:
			nueva_empresa_creada = rellenar_tablas_licitaciones_empresas(registro_completo)

			# nueva_fecha_creada = rellenar_tablas_fechas(registro_completo)

			# if nueva_empresa_creada:
			# 	barrio_registro = registro_completo[9]
			# 	entorno_registro = registro_completo[1]
			# 	etapa_registro = registro_completo[3]
			# 	tipo_obra_registro = registro_completo[4]
			# 	fecha_inicio = nueva_fecha_creada



	@classmethod
	def nueva_obra(cls):
		# TODO crear nueva obra utilizando el modelo orm
		print("nueva obra")
		# llamar a obtener_datos_nueva_obra
		# utilizar nuevo_proyecto de la clase Obra.nueva_o



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

