import pandas as pd
from utils import create_new_record

from peewee import *
from abc import ABCMeta
from modelo_orm import *
from typing import Optional


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

		# TODO cargar los datos del csv a la tabla
		# lista donde pongo las columnas a traer para convertir en tablas unicas
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
				"property":"nombre"
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
		# ciclo para buscar cada columna de la bd que coincida con el criterio de la lista y ponerlos
		# en una lista anidada
		for tabs in tablas_a_traer:
			datos_unicos_columna = list(cls.df_obras_publicas[tabs["name_column"]].unique())
			print(SEPARATOR_LINE)
			print(f"cargando {tabs['name_column']}")
			print(SEPARATOR_LINE)
			for dato in datos_unicos_columna:
				print(f"agregando {dato} de {tabs['name_column']} en {tabs['table']}")
				create_new_record(property=tabs["property"], table=tabs["table"], value=dato)

		# cargando TipoBarrio
		print(SEPARATOR_LINE)
		print("cargando barrios")
		print(SEPARATOR_LINE)
		# obtener un dataframe resultante de solo dos columnas
		df_comunas_barrios = cls.df_obras_publicas[["barrio", "comuna"]].drop_duplicates()
		# recorrer el dataframe
		for index, row in df_comunas_barrios.iterrows():
			# obtener el barrio del csv
			barrio = row["barrio"]
			# obtener la comuna del csv
			comuna = row["comuna"]
			# REFACTOR optimizar carga de comunas con algunos registros erroneos
			print(f"{index} Barrio: {barrio}, Comuna: {comuna}")
			barrio_existente = TipoBarrio.get_or_none(nombre=barrio)
			comuna_existente = TipoComuna.get_or_none(numero=comuna)
			# verificando que comuna existe y que el barrio no ya que seria un duplicado
			if comuna_existente and not barrio_existente:
				print("Existe una comuna asociada")
				print("comuna existente:")
				print(comuna_existente)
				TipoBarrio.create(nombre=barrio, id_comuna=comuna_existente)
			else:
				print("Barrio no posee una comuna asociada o el barrio ya existe")

		print(SEPARATOR_LINE)
		print("cargando Empresas")
		print(SEPARATOR_LINE)
		# obtener un dataframe resultante de solo dos columnas
		df_licitaciones_empresas = cls.df_obras_publicas[["licitacion_oferta_empresa", "cuit_contratista"]].drop_duplicates()
		# recorrer el dataframe
		for index, row in df_licitaciones_empresas.iterrows():
			# obtener el nombre de la empresa del csv
			empresa_nombre = row["licitacion_oferta_empresa"]
			# obtener el cuit_contratista del csv
			cuit_contratista = row["cuit_contratista"]
			print(f"{index} Empresa nombre: {empresa_nombre}, Cuit_contratista: {cuit_contratista}")
			empresa_existente = Empresa.get_or_none(cuit_contratista=cuit_contratista)
			# verificando que la empresa no exista aun
			# REFACTOR optimizar algunas creaciones con datos erroneos
			if not empresa_existente:
				print("No existe la empresa")
				print("creando")
				Empresa.create(nombre=empresa_nombre, cuit_contratista=cuit_contratista)
			else:
				print("La empresa ya existe")


		# cargando tablas licitacion_oferta_empresa y obras_publicas

		# obteniendo los datos unicos existentes en cuit_contratista
		# datos

		for registro_completo in cls.df_obras_publicas.values:
			print(SEPARATOR_LINE)
			print("cargando licitaciones y obras")
			print(SEPARATOR_LINE)
			# obteniendo datos de tablas relacionadas
			rg_area_responsable = TipoAreaResponsable.get_or_none(nombre=registro_completo[5])
			print(rg_area_responsable)
			rg_contratacion_atr = TipoContratacion.get_or_none(tipo_contratacion=registro_completo[23])
			print(rg_contratacion_atr)
			rg_empresa_atr = Empresa.get_or_none(nombre=registro_completo[21])
			print(rg_empresa_atr)
			# obteniendo atributos para licitacion_oferta_empresa
			# REFACTOR optimizar tanto como utilizar una estructura de datos
			# REFACTOR o crear una nueva funcion para recorrer y evitar codigo duplicado
			licitacion_anio_atr = registro_completo[22] if pd.isnull(registro_completo[22]) else 0
			print(licitacion_anio_atr)
			mano_obra_atr = registro_completo[27] if pd.isnull(registro_completo[27]) else 0
			print(mano_obra_atr)
			beneficiarios_atr = registro_completo[26] if pd.isnull(registro_completo[26]) else 0
			print(beneficiarios_atr)
			monto_contrato_atr = registro_completo[7] if pd.isnull(registro_completo[7]) and str(monto_contrato_atr).isdigit() else 0
			print(monto_contrato_atr)
			financiamiento_atr = registro_completo[35] if isinstance(registro_completo[35], str) else "Sin especificar"
			print(financiamiento_atr)
			expediente_numero_atr = registro_completo[35] if isinstance(registro_completo[35], str) else "Sin especificar"
			print(expediente_numero_atr)
			LicitacionOfertaEmpresa.get_or_create(id_area_responsable=rg_area_responsable, id_contratacion=rg_contratacion_atr, id_empresa=rg_empresa_atr, licitacion_anio=licitacion_anio_atr, mano_obra=mano_obra_atr, beneficiarios=beneficiarios_atr, monto_contrato=monto_contrato_atr, financiamiento=financiamiento_atr, expediente_numero=expediente_numero_atr)

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
