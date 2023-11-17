from peewee import *

sqlite_db = SqliteDatabase("obras_urbanas.db")
try:
  sqlite_db.connect()
except OperationalError as e:
  print("No se pudo realizar la conexion")
  exit()


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


class TipoTipo(BaseModel):
  nombre = CharField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_tipo"


class TipoAreaResponsable(BaseModel):
  nombre = CharField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_area_responsable"


class TipoComuna(BaseModel):
  nombre = IntegerField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_comuna"


class TipoBarrio(BaseModel):
  nombre = CharField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_barrio"


class TipoCompromiso(BaseModel):
  nombre = BooleanField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_compromiso"


class TipoDestacada(BaseModel):
  nombre = BooleanField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_destacada"


class Obra(BaseModel):
  # agrego atributos
  tipo_entorno = ForeignKeyField(TipoEntorno, backref="tipo_entorno")
  nombre = CharField()
  etapa = ForeignKeyField(TipoEtapa, backref="tipo_etapa")
  tipo_tipo = ForeignKeyField(TipoTipo, backref="tipo_tipo")
  area_responsable = ForeignKeyField(
      TipoAreaResponsable, backref="tipo_area_responsable"
  )
  descripcion = CharField(null=True)
  monto_contrato = DoubleField()
  comuna = ForeignKeyField(TipoComuna, backref="tipo_comuna")
  barrio = ForeignKeyField(TipoBarrio, backref="tipo_barrio")
  direccion = CharField(null=True)
  fecha_inicio = DateTimeField()
  fecha_fin_inicial = DateTimeField(null=True)
  plazo_meses = IntegerField(null=True)
  porcentaje_avance = FloatField()
  licitacion_oferta_empresa = CharField()
  licitacion_anio = IntegerField()
  contratacion_tipo = CharField()
  nro_contratacion = IntegerField(unique=True)
  cuit_contratista = IntegerField(unique=True)
  beneficiarios = CharField()
  mano_obra = CharField()
  compromiso = ForeignKeyField(TipoCompromiso, backref="tipo_compromiso")
  destacada = ForeignKeyField(TipoDestacada, backref="tipo_destacada")
  expediente_numero = IntegerField(unique=True, null=True)
  financiamiento = CharField(null=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "obras_publicas"

  def nuevo_proyecto(self):
    print("nuevo proyecto")

  def iniciar_contratacion(self):
    print("iniciar contratacion")

  def adjudicar_obra(self):
    print("adjudicar obra")

  def iniciar_obra(self):
    print("iniciar obra")

  def actualizar_porcentaje_avance(self):
    print("actualizar porcentaje avance")

  def incrementar_plazo(self):
    print("incrementar plazo")

  def incrementar_mano_obra(self):
    print("incrementar obra")

  def finalizar_obra(self):
    print("finalizar obra")

  def rescindir_obra(self):
    print("rescindir obra")

sqlite_db.create_tables([TipoAreaResponsable, TipoBarrio, TipoCompromiso, TipoComuna, TipoDestacada, TipoEntorno, TipoEtapa, TipoTipo, Obra])
