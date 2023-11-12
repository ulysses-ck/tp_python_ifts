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
