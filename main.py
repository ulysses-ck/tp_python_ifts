import gestionar_obras

GestionarObras.df_obras_publicas = gestionar_obras.extraer_datos()
GestionarObras.sqlite_db_obras = gestionar_obras.conectar_db()
GestionarObras.mapear_orm()
GestionarObras.limpiar_datos()
GestionarObras.cargar_datos()