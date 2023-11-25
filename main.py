from gestionar_obras import GestionarObras
import pandas as pd
from peewee import *
from modelo_orm import *

GestionarObras.sqlite_db_obras = GestionarObras.conectar_db()
GestionarObras.mapear_orm()

GestionarObras.df_obras_publicas = GestionarObras.extraer_datos()

GestionarObras.limpiar_datos()
GestionarObras.cargar_datos()
GestionarObras.nueva_obra()
