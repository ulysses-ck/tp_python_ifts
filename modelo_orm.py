from peewee import *

sqlite_db = SqliteDatabase("obras_urbanas.db")

# esta clase hereda de Model de peewee
class BaseModel(Model):
  class Meta:
    database=sqlite_db

# aca empiezan las clases que corresponden a cada tabla existente en el diagrama
class TipoEntorno(BaseModel):
  nombre = CharField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_entorno"


class TipoEtapa(BaseModel):
  nombre = CharField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_etapa"


class TipoObra(BaseModel):
  nombre = CharField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_obra"

class TipoAreaResponsable(BaseModel):
  nombre = CharField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_area_responsable"

class TipoContratacion(BaseModel):
  tipo_contratacion = CharField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_contratacion"

class Empresa(BaseModel):
  nombre = CharField()
  cuit_contratista = IntegerField(unique=True)

  def __str__(self):
    return f"{self.nombre} {self.cuit_contratista}"

  class Meta:
    db_table = "empresas"

class Fechas(BaseModel):
  fecha_inicio = DateTimeField(null=True)
  fecha_fin_inicial = DateTimeField(null=True)
  plazo_meses = IntegerField(null=True)

class LicitacionOfertaEmpresa(BaseModel):
  nombre = CharField()
  # se utiliza la llave foranea para con sus respectivas tablas
  id_area_responsable = ForeignKeyField(TipoAreaResponsable, backref="tipos_area_responsable")
  id_contratacion = ForeignKeyField(TipoContratacion, backref="tipos_contratacion")
  fechas = ForeignKeyField(Fechas, backref="fechas")
  id_empresa = ForeignKeyField(Empresa, backref="empresas")
  licitacion_anio = IntegerField(null=True)
  mano_obra = IntegerField()
  beneficiarios = IntegerField()
  monto_contrato = DoubleField()
  financiamiento = CharField()
  expediente_numero = CharField()

  def __str__(self) -> str:
    return self.nombre

  class Meta:
    db_table = "licitacion_oferta_empresa"

class TipoComuna(BaseModel):
  numero = IntegerField(unique=True)

  def __str__(self):
    return self.numero

  class Meta:
    db_table = "tipos_comuna"

class TipoBarrio(BaseModel):
  nombre = CharField(unique=True)
  id_comuna = ForeignKeyField(TipoComuna, backref="tipos_comuna")

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_barrio"

class Obra(BaseModel):
  barrio = ForeignKeyField(TipoBarrio, backref="tipo_barrio")
  tipo_entorno = ForeignKeyField(TipoEntorno, backref="tipo_entorno")
  etapa = ForeignKeyField(TipoEtapa, backref="tipo_etapa")
  tipo_obra = ForeignKeyField(TipoObra, backref="tipos_obra")
  fechas = ForeignKeyField(Fechas, backref="fechas")
  licitacion_oferta_empresa = ForeignKeyField(LicitacionOfertaEmpresa, backref="licitacion_oferta_empresa")

  # agrego atributos
  nombre = CharField()
  descripcion = CharField(null=True)
  porcentaje_avance = FloatField()
  destacada = BooleanField()

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "obras_publicas"

  def nuevo_proyecto(self, nombre, descripcion, porcentaje_avance, destacada, id_barrio, id_entorno, id_tipo_obra, id_etapa, id_licitacion_oferta_empresa, fechas):
    try:
      etapa_proyecto = TipoEtapa.get_or_create(nombre='Proyecto')
      barrio_existente = TipoBarrio.get_or_none(id=id_barrio)
      entorno_existente = TipoEntorno.get_or_none(id=id_entorno)
      tipo_obra_existente = TipoObra.get_or_none(id=id_tipo_obra)
      if etapa_proyecto and barrio_existente and entorno_existente and tipo_obra_existente:
        self.id_barrio = barrio_existente
        self.id_entorno = entorno_existente
        self.id_etapa = id_etapa
        self.id_tipo_obra = tipo_obra_existente
        self.fechas = fechas
        self.id_licitacion_oferta_empresa = id_licitacion_oferta_empresa
        self.nombre = nombre
        self.descripcion = descripcion
        self.porcentaje_avance = porcentaje_avance
        self.destacada = destacada
        print("¡Nuevo proyecto de obra iniciado con éxito!")
      else:
        print("No se pudo iniciar el proyecto debido a valores inexistentes en la base de datos.")
    except Exception as e:
      print(f"Error al iniciar el proyecto: {str(e)}")

  def iniciar_contratacion(self, nro_contratacion, contratacion_tipo):
    print("iniciar contratacion")
    try:
      contratacion_existente = TipoContratacion.get_or_none(id=contratacion_tipo)

      if contratacion_existente:
          self.nro_contratacion = nro_contratacion
          self.contratacion_tipo = contratacion_existente
          self.save()

          print("¡Licitación/Contratación de obra iniciada con éxito!")
      else:
          print("No se pudo iniciar la contratación debido a que la Contratación no existe en la base de datos.")
    except Exception as e:
      print(f"Error al iniciar la contratación: {str(e)}")

  def adjudicar_obra(self, expediente_numero, id_empresa):
    print("adjudicar obra")
    try:
      empresa_existente = Empresa.get_or_none(id=id_empresa)

      if empresa_existente:
          self.id_empresa = empresa_existente
          self.expendiente_numero = expediente_numero
          self.save()

          print("¡Adjudicación de obra a empresa realizada con éxito!")
      else:
          print("No se pudo adjudicar la obra debido a que la Empresa no existe en la base de datos.")
    except Exception as e:
      print(f"Error al adjudicar la obra: {str(e)}")

  def iniciar_obra(self, destacada, fecha_inicio, fecha_fin_inicial, mano_obra, financiamiento):
    print("iniciar obra")
    try:
      fuente_financiamiento_existente = financiamiento.get_or_none(id=financiamiento)

      if fuente_financiamiento_existente:
          self.destacada = destacada
          self.fecha_inicio = fecha_inicio
          self.fecha_fin_inicial = fecha_fin_inicial
          self.id_fuente_financiamiento = fuente_financiamiento_existente
          self.mano_obra = mano_obra
          self.save()

          print("¡Inicio de la obra registrado con éxito!")
      else:
          print("No se pudo iniciar la obra debido a que la Fuente de Financiamiento no existe en la base de datos.")
    except Exception as e:
      print(f"Error al iniciar la obra: {str(e)}")

  def actualizar_porcentaje_avance(self, nuevo_porcentaje_avance):
    print("actualizar porcentaje avance")
    try:
      self.porcentaje_avance = nuevo_porcentaje_avance
      self.save()

      print("¡Porcentaje de avance de la obra actualizado con éxito!")
    except Exception as e:
        print(f"Error al actualizar el porcentaje de avance: {str(e)}")

  def incrementar_plazo(self, cantidad_meses):
    try:
      self.plazo_meses += cantidad_meses
      self.save()

      print("¡Plazo de la obra incrementado con éxito!")
    except Exception as e:
      print(f"Error al incrementar el plazo de la obra: {str(e)}")

  def incrementar_mano_obra(self, cantidad_mano_obra):
    try:
      self.mano_obra += cantidad_mano_obra
      self.save()

      print("¡Cantidad de mano de obra incrementada con éxito!")
    except Exception as e:
      print(f"Error al incrementar la cantidad de mano de obra: {str(e)}")

  def finalizar_obra(self):
    print("finalizar obra")
    try:
      self.etapa = "Finalizada"
      self.porcentaje_avance = 100
      self.save()

      print("¡La obra ha sido finalizada con éxito!")
    except Exception as e:
      print(f"Error al finalizar la obra: {str(e)}")

  def rescindir_obra(self):
    print("rescindir obra")
    try:
      self.etapa = "Rescindida"
      self.save()

      print("¡La obra ha sido rescindida!")
    except Exception as e:
      print(f"Error al rescindir la obra: {str(e)}")
