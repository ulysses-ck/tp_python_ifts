from peewee import *

sqlite_db = SqliteDatabase("obras_urbanas.db")

class BaseModel(Model):
  class Meta:
    database=sqlite_db

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

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_barrio"

class Obra(BaseModel):
  # agrego atributos
  barrio = ForeignKeyField(TipoBarrio, backref="tipo_barrio")
  tipo_entorno = ForeignKeyField(TipoEntorno, backref="tipo_entorno")
  etapa = ForeignKeyField(TipoEtapa, backref="tipo_etapa")
  tipo_obra = ForeignKeyField(TipoObra, backref="tipos_obra")
  fechas = ForeignKeyField(Fechas, backref="fechas")
  licitacion_oferta_empresa = ForeignKeyField(LicitacionOfertaEmpresa, backref="licitacion_oferta_empresa")

  nombre = CharField()
  descripcion = CharField(null=True)
  porcentaje_avance = FloatField()
  destacada = BooleanField()

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "obras_publicas"

  def nuevo_proyecto(self, nombre, descripcion, monto_contrato, plazo_meses, beneficiarios, mano_obra, porcentaje_avance, destacada):
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

  def iniciar_contratacion(self):
    # TODO asignar tipo_contratacion: TipoContratacion y nro_contratacion
    print("iniciar contratacion")

  def adjudicar_obra(self, expediente_numero):
    # TODO asignar nueva empresa: TipoEmpresa
    print("adjudicar obra")

  def iniciar_obra(self, destacada, fecha_inicio, fecha_fin_inicial, mano_obra):
    # TODO asignar atributos correspondientes
    print("iniciar obra")

  def actualizar_porcentaje_avance(self, nuevo_porcentaje_avance):
    self.porcentaje_avance = nuevo_porcentaje_avance
    print("actualizar porcentaje avance")

  def incrementar_plazo(self, nuevo_plazo_meses):
    self.plazo_meses = nuevo_plazo_meses

  def incrementar_mano_obra(self, nueva_mano_obra):
    self.mano_obra = nueva_mano_obra

  def finalizar_obra(self):
    print("finalizar obra")

  def rescindir_obra(self):
    print("rescindir obra")
