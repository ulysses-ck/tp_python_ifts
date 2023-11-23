from gestionar_obras import GestionarObras

GestionarObras.sqlite_db_obras = GestionarObras.conectar_db()
GestionarObras.mapear_orm()

GestionarObras.df_obras_publicas = GestionarObras.extraer_datos()
GestionarObras.limpiar_datos()
GestionarObras.cargar_datos()

