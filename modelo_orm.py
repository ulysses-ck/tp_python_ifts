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
  lat = DoubleField(null=True)
  lng = DoubleField(null=True)
  fecha_inicio = DateTimeField()
  fecha_fin_inicial = DateTimeField(null=True)
  plazo_meses = IntegerField(null=True)
  porcentaje_avance = FloatField()
  imagen1 = CharField(null=True)
  imagen2 = CharField(null=True)
  imagen3 = CharField(null=True)
  imagen4 = CharField(null=True)
  licitacion_oferta_empresa = CharField()
  licitacion_anio = IntegerField()
  contratacion_tipo = CharField()
  nro_contratacion = IntegerField(unique=True)
  cuit_contratista = IntegerField(unique=True)
  beneficiarios = CharField()
  mano_obra = CharField()
  compromiso = ForeignKeyField(TipoCompromiso, backref="tipo_compromiso")
  destacada = ForeignKeyField(TipoDestacada, backref="tipo_destacada")
  ba_elige = CharField(null=True)
  link_interno = CharField(null=True)
  pliego_descarga = CharField(null=True)
  expediente_numero = IntegerField(unique=True, null=True)
  estudio_ambiental_descarga = CharField(null=True)
  financiamiento = CharField(null=True)

  def __str__(self):
      return self.nombre

  class Meta:
    db_table = "obras_publicas"

  def nuevo_proyecto(self):
      pass

  def iniciar_contratacion(self):
      pass

  def adjudicar_obra(self):
      pass

  def iniciar_obra(self):
      pass

  def actualizar_porcentaje_avance(self):
      pass

  def incrementar_plazo(self):
      pass

  def incrementar_mano_obra(self):
      pass

  def finalizar_obra(self):
      pass

  def rescindir_obra(self):
      pass

sqlite_db.create_tables([TipoAreaResponsable, TipoBarrio, TipoCompromiso, TipoComuna, TipoDestacada, TipoEntorno, TipoEtapa, TipoTipo, Obra])
