from peewee import *
import datetime


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
    id = IntegerField
    tipo_entorno = ForeignKeyField(TipoEntorno, backref="tipo_entorno")
    nombre = CharField
    etapa = ForeignKeyField(TipoEtapa, backref="tipo_etapa")
    tipo_tipo = ForeignKeyField(TipoTipo, backref="tipo_tipo")
    area_responsable = ForeignKeyField(
        TipoAreaResponsable, backref="tipo_area_responsable"
    )
    descripcion = CharField
    monto_contrato = FloatField
    comuna = ForeignKeyField(TipoComuna, backref="tipo_comuna")
    barrio = ForeignKeyField(TipoBarrio, backref="tipo_barrio")
    direccion = CharField
    lat = FloatField
    lng = FloatField
    fecha_inicio = DateTimeField
    fecha_fin_inicial = DateTimeField
    plazo_meses = IntegerField
    porcentaje_avance = FloatField
    imagen1 = CharField
    imagen2 = CharField
    imagen3 = CharField
    imagen4 = CharField
    licitacion_oferta_empresa = CharField
    licitacion_anio = IntegerField
    contratacion_tipo = CharField
    nro_contratacion = IntegerField
    cuit_contratista = IntegerField
    beneficiarios = CharField
    mano_obra = CharField
    compromiso = ForeignKeyField(TipoCompromiso, backref="tipo_compromiso")
    destacada = ForeignKeyField(TipoDestacada, backref="tipo_destacada")
    ba_elige = CharField
    link_interno = CharField
    pliego_descarga = CharField
    expediente_numero = IntegerField
    estudio_ambiental_descarga = CharField
    financiamiento = CharField

    def nuevo_proyecto():
        pass

    def iniciar_contratacion():
        pass

    def adjudicar_obra():
        pass

    def iniciar_obra():
        pass

    def actualizar_porcentaje_avance():
        pass

    def incrementar_plazo():
        pass

    def incrementar_mano_obra():
        pass

    def finalizar_obra():
        pass

    def rescindir_obra():
        pass

class Obras_Publicas(BaseModel):
    id=IntegerField(unique = True)
    entorno = CharField
    nombre = CharField
    etapa = CharField
    tipo = CharField
    area_responsable = CharField
    descripcion = CharField
    monto_contratos = DoubleField
    comuna = IntegerField
    barrio = CharField
    direccion = CharField
    lat = DoubleField
    lgn = DoubleField
    fecha_inicio = DateTimeField
    fecha_fin_inicial = DateTimeField
    plazo_meses = IntegerField
    porcentaje_avance = IntegerField
    imagen_1 = CharField
    imagen_2 = CharField
    imagen_3 = CharField
    imagen_4 = CharField
    licitacion_oferta_empresa = CharField
    licitacion_anio = IntegerField
    contratacion_tipo = CharField
    nro_contratacion = CharField(unique=True)
    cuit_contratista = IntegerField(unique=True)
    beneficiarios = CharField
    mano_obra = CharField
    compromiso = CharField
    destacada = BooleanField
    ba_elige = CharField
    link_interno = CharField
    pliego_descarga = CharField
    expediente_numero = IntegerField(unique=True)
    estudio_ambiental_descarga = CharField
    financiamiento = DoubleField
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = "Obras Publicas"