from peewee import *


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
    tipo_entorno = ForeignKeyField(TipoEntorno, backref="tipos_entorno")

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
