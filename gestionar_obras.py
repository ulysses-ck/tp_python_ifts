import pandas as pd
from peewee import *

from abc import ABCMeta

from modelo_orm import *

class GestionarObras(metaclass=ABCMeta):
	df_obras_publicas = None
	sqlite_db_obras = None

	@classmethod
	def extraer_datos(cls):
		try:
			df = pd.read_csv("./observatorio-de-obras-urbanas.csv")
			cls.df = df
			return df
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
		cls.sqlite_db_obras.create_tables([TipoAreaResponsable, TipoBarrio, TipoCompromiso, TipoComuna, TipoDestacada, TipoEntorno, TipoEtapa, TipoTipo, Obra, TipoContratacion])

	@classmethod
	def limpiar_datos(cls, df):
		cls.df = df.dropna(subset=["entorno", "nombre", "etapa", "tipo", "area_responsable", "monto_contrato", "comuna", "barrio", "direccion", "fecha_inicio", "porcenta_avance", "licitacion_oferta_empresa", "licitacion_anio", "contratacion_tipo", "nro_contratacion", "cuit_contratista", "mano_obra"], axis=0, inplace=True)

	@classmethod
	def cargar_datos(cls):
		# TODO cargar los datos del csv a la tabla
		#lista donde pongo las columnas a traer para convertir en tablas unicas
		tablas_a_traer= ["etapa", "comuna", "barrio", "entorno", "tipo"]
		#lista donde van a ingresar dichas colunmnas en formato tabla
		tablas=[]
		#ciclo para buscar cada columna de la bd que coincida con el criterio de la lista y ponerlos
		#en una lista anidada
		for tabs in tablas_a_traer:
			tablas.append(cls.df_obras_publicas[tabs].unique())
		#ciclo para, identificando su posicion en la lista anidada, persistir los datos extraidos
		for tabs in range(len(tablas)):
			match tabs:
				case 0:
					for fila in tablas[0]:
						try:
							TipoEtapa.create(nombre=fila)
						except IntegrityError as f:
							print("Error insertando etapa", f)
				case 1:
					for fila in tablas[1]:
						try:
							TipoComuna.create(nombre=fila)
						except IntegrityError as f:
							print("Error insertando comuna", f)
				case 2:
					for fila in tablas[2]:
						try:
							TipoBarrio.create(nombre=fila)
						except IntegrityError as f:
							print("Error insertando barrio", f)
				case 3:
					for fila in tablas[3]:
						try:
							TipoEntorno.create(nombre=fila)
						except IntegrityError as f:
							print("Error insertando entorno", f)
				case 4:
					for fila in tablas[4]:
						try:
							TipoTipo.create(nombre=fila)
						except IntegrityError as f:
							print("Error insertando tipo de obra", f)
				case _:
					print("no se cargò nada")
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