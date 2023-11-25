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
			nueva_licitacion_oferta_empresa = rellenar_tablas_licitaciones_empresas(registro_completo)

			nueva_fecha_creada = rellenar_tablas_fechas(registro_completo)

			if nueva_licitacion_oferta_empresa and nueva_fecha_creada:
				print(SEPARATOR_LINE)
				print("Intentantdo crear NUEVA_OBRA")
				print(SEPARATOR_LINE)

				barrio_registro = TipoBarrio.get_or_none(nombre=registro_completo[9])
				print("Barrio de la fila")
				print(barrio_registro)
				entorno_registro = TipoEntorno.get_or_none(nombre=registro_completo[1])
				print("Entorno de la fila")
				print(entorno_registro)
				etapa_registro = TipoEtapa.get_or_none(nombre=registro_completo[3])
				print("etapa de la fila")
				print(etapa_registro)
				tipo_obra_registro = TipoObra.get_or_none(nombre=registro_completo[4])
				print("Tipo Obra de la fila")
				print(tipo_obra_registro)


				# if barrio_registro and entorno_registro and etapa_registro and tipo_obra_registro:
				# 	print(SEPARATOR_LINE)
				# 	print("Creando NUEVA_OBRA")
				# 	print(SEPARATOR_LINE)
				# 	nombre_rg = registro_completo[2]
				# 	print("Nombre de la fila")
				# 	print(nombre_rg)
				# 	descripcion_rg = registro_completo[6]
				# 	print("descripcion de la fila")
				# 	print(descripcion_rg)
				# 	porcentaje_rg = registro_completo[16]
				# 	print("porcentaje_rg de la fila")
				# 	print(porcentaje_rg)
				# 	destacada_rg = registro_completo[29]
				# 	print("destacada_rg de la fila")
				# 	print(destacada_rg)

				# 	if(pd.isna(destacada_rg)):
				# 		destacada_rg = False
				# 	else:
				# 		destacada_rg = True
				# 		print(destacada_rg)

				# 	try:
				# 		porcentaje_rg = float(porcentaje_rg)
				# 		print(porcentaje_rg)
				# 	except ValueError as e:
				# 		print(f"Error: {e}")
				# 		porcentaje_rg = 0

				# 	Obra.create(nombre=nombre_rg, descripcion=descripcion_rg, porcentaje_avance=porcentaje_rg, destacada=destacada_rg, licitacion_oferta_empresa=nueva_licitacion_oferta_empresa, fechas=nueva_fecha_creada, barrio=barrio_registro, tipo_entorno=entorno_registro, etapa=etapa_registro, tipo_obra=tipo_obra_registro)
				# else:
				# 	print("Faltan valores para crear la Obra Publica")


	@classmethod
	def nueva_obra(cls):
		print("nueva obra")
		# llamar a obtener_datos_nueva_obraç
		mostrar_menu()




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

