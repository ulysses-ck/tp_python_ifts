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

class TipoContratacion(BaseModel):
  tipo_contratacion = CharField(unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    db_table = "tipos_contratacion"

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
  contratacion_tipo = ForeignKeyField(TipoContratacion, backref="tipos_contratacion")
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

  def nuevo_proyecto(self, nombre, descripcion, monto_contrato, direccion, plazo_meses, beneficiarios, mano_obra, porcenta_avance):
    self.nombre = nombre
    self.descripcion = descripcion
    self.monto_contrato = monto_contrato
    self.direccion = direccion
    self.plazo_meses = plazo_meses
    self.beneficiarios = beneficiarios
    self.mano_obra = mano_obra
    self.porcentaje_avance = porcenta_avance

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
    # TODO cambiar atributo TipoEtapa a "Finalizada" segun corresponda el indice en la tabla
    print("finalizar obra")

  def rescindir_obra(self):
    # TODO cambiar atributo TipoEtapa a "Rescindida" segun corresponda el indice en la tabla
    print("rescindir obra")
