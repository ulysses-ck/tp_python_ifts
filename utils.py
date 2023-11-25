from peewee import *
from modelo_orm import *
import pandas as pd
from datetime import datetime


# funcion para crear dinamicamente registros unicos utilizando unpacking operator
def create_new_record(table, property, value):

	dict_content = {
		property: value
	}

	try:
		table.get_or_create(**dict_content)

	except IntegrityError as e:
		print("Error insertando comuna", e)

def crear_tablas_con_valores_unicos(df_obras_publicas):
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
				datos_unicos_columna = list(df_obras_publicas[tabs["name_column"]].unique())
				print(f"cargando {tabs['name_column']}")
				for dato in datos_unicos_columna:
					print(f"agregando {dato} de {tabs['name_column']} en {tabs['table']}")
					create_new_record(property=tabs["property"], table=tabs["table"], value=dato)

def rellenar_tablas_barrios(df_obras_publicas):
	# cargando TipoBarrio
	# obtener un dataframe resultante de solo dos columnas
	df_comunas_barrios = df_obras_publicas[["barrio", "comuna"]].drop_duplicates()
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


def rellenar_tablas_empresas(df_obras_publicas):
	# obtener un dataframe resultante de solo dos columnas
	df_licitaciones_empresas = df_obras_publicas[["licitacion_oferta_empresa", "cuit_contratista"]].drop_duplicates()
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

def rellenar_tablas_licitaciones_empresas(registro_completo):

	# primary key de licitaciones_oferta_empresa
	rg_nro_contratacion = registro_completo[24]

	try:
		LicitacionOfertaEmpresa.get_by_id(rg_nro_contratacion)
		return None
	except DoesNotExist as e:

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
		licitacion_anio_atr = registro_completo[22]
		if not pd.isna(licitacion_anio_atr) and licitacion_anio_atr.isdigit():
			licitacion_anio_atr = int(licitacion_anio_atr)
		else:
			licitacion_anio_atr= 0
		print(f"Anio licitacion: {licitacion_anio_atr}")

		mano_obra_atr = registro_completo[27]
		if not pd.isna(mano_obra_atr) and mano_obra_atr.isdigit():
			mano_obra_atr = int(mano_obra_atr)
		else:
			mano_obra_atr = 0
		print(f"mano_obra: {mano_obra_atr}")

		beneficiarios_atr = registro_completo[26]
		if not pd.isna(beneficiarios_atr) and beneficiarios_atr.isdigit():
			beneficiarios_atr = int(beneficiarios_atr)
		else:
			beneficiarios_atr = 0
		print(f"beneficiarios_atr: {beneficiarios_atr}")

		monto_contrato_atr = registro_completo[7]
		if not pd.isna(monto_contrato_atr):
			monto_contrato_atr = monto_contrato_atr.replace(".", "").replace(",", ".").replace("$", "")
			try:
				# Convert to an IntegerField
				monto_contrato_atr = float(monto_contrato_atr)
			except ValueError as e:
				print(f"error converting: {e}")
		else:
			print(0)
		print(f"monto_contrato_atr: {monto_contrato_atr}")

		financiamiento_atr = registro_completo[35] if isinstance(registro_completo[35], str) else "Sin especificar"
		print(f"financiamiento_atr: {financiamiento_atr}")
		expediente_numero_atr = registro_completo[33] if isinstance(registro_completo[33], str) else "Sin especificar"
		print(f"expediente_numero_atr: {expediente_numero_atr}")
		if rg_area_responsable and rg_contratacion_atr and rg_empresa_atr:
			print("agregando datos")
			nueva_empresa_creada = LicitacionOfertaEmpresa.get_or_create(nro_contratacion=rg_nro_contratacion,id_area_responsable=rg_area_responsable, id_contratacion=rg_contratacion_atr, id_empresa=rg_empresa_atr, licitacion_anio=licitacion_anio_atr, mano_obra=mano_obra_atr, beneficiarios=beneficiarios_atr, monto_contrato=monto_contrato_atr, financiamiento=financiamiento_atr, expediente_numero=expediente_numero_atr)
			return nueva_empresa_creada
		else:
			print("El registro no posee todas sus valores")

def rellenar_tablas_fechas(registro_completo):
	fecha_inicio = registro_completo[13]
	fecha_fin_inicial = registro_completo[14]
	plazo_meses = registro_completo[15]
	if not pd.isna(fecha_inicio) and not pd.isna(fecha_fin_inicial) and not pd.isna(plazo_meses):
		fecha_inicio = datetime.strptime(fecha_inicio, "%m/%d/%Y")
		# try:
		plazo_meses = int(plazo_meses)
	else:
		fecha_inicio = None
		fecha_fin_inicial = None
		plazo_meses = None

	# creando datos
	print(f"fecha_inicio: {fecha_inicio}")
	print(f"fecha_fin_inicial: {fecha_fin_inicial}")
	print(f"plazo_meses: {plazo_meses}")
	return Fechas.create(fecha_inicio=fecha_inicio, fecha_fin_inicial=fecha_fin_inicial, plazo_meses=plazo_meses)
