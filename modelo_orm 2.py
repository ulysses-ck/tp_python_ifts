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
    self.nombre = nombre
    self.descripcion = descripcion
    self.porcentaje_avance = porcentaje_avance
    self.destacada = destacada

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
