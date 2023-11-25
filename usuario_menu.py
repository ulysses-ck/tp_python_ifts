import random
from datetime import datetime
from peewee import *
from modelo_orm import *

numeros_contratacion_utilizados = []

def generar_numero_contratacion():
    while True:
        fecha_actual = datetime.now()
        año_actual = fecha_actual.year
        numero_aleatorio = random.randint(100_000_000, 999_999_999)
        nuevo_numero_contratacion = f"{año_actual}/GCBA-{numero_aleatorio}"
        if nuevo_numero_contratacion not in numeros_contratacion_utilizados:
            numeros_contratacion_utilizados.append(nuevo_numero_contratacion)
            return nuevo_numero_contratacion


def mostrar_menu():
    while True:
        print("----- Menú de Obras -----")
        print("1. Nuevo Proyecto")
        print("2. Iniciar Contratación")
        print("3. Adjudicar Obra")
        print("4. Iniciar Obra")
        print("5. Actualizar Porcentaje de Avance")
        print("6. Incrementar Plazo")
        print("7. Incrementar Mano de Obra")
        print("8. Finalizar Obra")
        print("9. Rescindir Obra")
        print("0. Salir")

        opcion = input("Seleccione una opción (0-9): ")

        if opcion == "1":
            (
                nombre,
                descripcion,
                porcentaje_avance,
                destacada,
                barrio,
                tipo_entorno,
                etapa,
                tipo_obra,
                fechas,
                licitacion_oferta_empresa
            ) = obtener_datos_nueva_obra()

            print("Nueva obra creada")
            # Obra.create(nombre, descripcion, porcentaje_avance, destacada, barrio, tipo_entorno)

        elif opcion == "2":
            contratacion_tipo = obtener_tipo_contratacion()
            if contratacion_tipo is not None:
                nro_contratacion = generar_numero_contratacion()
                obra.iniciar_contratacion(contratacion_tipo, nro_contratacion)
            print("Contratación iniciada correctamente.")
            print(f"Número de contratación: {nro_contratacion}")
        elif opcion == "3":
            nro_expediente = input("Ingrese el número de expediente: ")
            empresa = obtener_empresa_existente()
            obra.adjudicar_obra(empresa, nro_expediente)
            print("Obra adjudicada.")
        elif opcion == "4":
            mano_obra = input("Ingrese la mano de obra: ")
            destacada = input("Ingrese destacada: ")
            fecha_inicio = input("Ingrese la fecha de inicio: ")
            fecha_fin_inicial = input("Ingrese la fecha final inicial: ")
            obra.iniciar_obra(destacada, fecha_inicio, fecha_fin_inicial, mano_obra)
            print("Obra iniciada.")
        elif opcion == "5":
            nuevo_porcentaje_avance = input("Ingrese nuevo porcentaje de avance: ")
            obra.actualizar_porcentaje_avance(nuevo_porcentaje_avance)
            print("Porcentaje de avance actualizado.")
        elif opcion == "6":
            nuevo_plazo_meses = input("Ingrese nuevo plazo en meses: ")
            obra.incrementar_plazo(nuevo_plazo_meses)
            print("Plazo incrementado.")
        elif opcion == "7":
            nueva_mano_obra = input("Ingrese nueva mano de obra: ")
            obra.incrementar_mano_obra(self, nueva_mano_obra)
            print("Mano de obra incrementada.")
        elif opcion == "8":
            obra.finalizar()
            print("Obra finalizada.")
        elif opcion == "9":
            obra.rescindir()
            print("Obra rescindida.")
        elif opcion == "0":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def obtener_datos_nueva_obra():
    nombre = input("Ingrese el nombre del proyecto: ")
    descripcion = input("Ingrese la descripción del proyecto: ")
    porcentaje_avance = input("Ingrese porcentaje de avance del proyecto: ")
    print("Es obra destacada? 1) Si; 2) No")
    try:
        while True:
            opcion = int(input("Ingrese si es destacada o no eligiendo una de las opciones numericamente: "))
            if opcion == 1:
                destacada = True
                print("Seleccion guardada")
                break
            if opcion == 2:
                destacada = False
                print("Seleccion guardada")
                break
            else:
                print("Elija una opcion valida")
                input()
    except ValueError:
        print("Elija una opcion numerica")
    try:
        while True:
            lista_opciones = extraer_Opciones(TipoBarrio)
            seleccion = int(input("Seleccione uno de los barrios disponibles digitando un numero: "))
            if seleccion in lista_opciones:
                print("barrio seleccionado")
                barrio = seleccion
                break
            else:
                print("Elija una opcion valida")
                input()
    except ValueError:
        print("Elija una opcion numerica")
    try:
        while True:
            lista_opciones = extraer_Opciones(TipoEntorno)
            seleccion = int(input("Seleccione uno de los entornos disponibles digitando un numero: "))
            if seleccion in lista_opciones:
                print("Entorno seleccionado")
                tipo_entorno = seleccion
                break
            else:
                print("Elija una opcion valida")
                input()
    except ValueError:
        print("Elija una opcion numerica")
    try:
        while True:
            lista_opciones = extraer_Opciones(TipoEtapa)
            seleccion = int(input("Seleccione uno de las etapas disponibles digitando un numero: "))
            if seleccion in lista_opciones:
                print("Etapa seleccionada")
                etapa = seleccion
                break
            else:
                print("Elija una opcion valida")
                input()
    except ValueError:
        print("Elija una opcion numerica")
    try:
        while True:
            lista_opciones = extraer_Opciones(TipoObra)
            seleccion = int(input("Seleccione uno de los tipos de obras disponibles digitando un numero: "))
            if seleccion in lista_opciones:
                print("Tipo de obra seleccionada")
                tipo_obra = seleccion
                break
            else:
                print("Elija una opcion valida")
                input()
    except ValueError:
        print("Elija una opcion numerica")
    while True:
        try:
            fecha_inicial = input("Ingrese la fecha de inicio con el siguiente formato (YYYY-MM-DD): ")
            fecha_final = input("Ingrese la fecha de cierre del proyecto con el siguiente formato (YYYY-MM-DD): ")
            try:
                plazo_meses = int(input("Ingrese el plazo en meses(solo numeros): "))
            except ValueError:
                print("Ingrese un dato numerico")
            registro = Fechas(fecha_inicial, fecha_final, plazo_meses)
            fechas= registro.id
            print(fechas)
            break
        except IntegrityError as e:
            print(f"Error {e}")
        except DataError as e:
            print(f"Error {e}")
    try:
        while True:
            lista_opciones, indices = extraer_Licitaciones(LicitacionOfertaEmpresa)
            seleccion = int(input("Seleccione uno de las licitaciones disponibles digitando un numero: "))
            if seleccion in indices:
                print("Licitacion seleccionada")
                licitacion_oferta_empresa = seleccion
                break
            else:
                print("Elija una opcion valida")
                input("porfa apruebe profe")
    except ValueError:
        print("Elija una opcion numerica")

    return (
        nombre,
        descripcion,
        porcentaje_avance,
        destacada,
        barrio,
        tipo_entorno,
        etapa,
        tipo_obra,
        fechas,
        licitacion_oferta_empresa,
    )


def obtener_tipo_contratacion():
    print("Opciones de Contratación:")
    print("0. Adicional de Mantenimiento")
    print("1. Anexo Contratación de Mantenimiento")
    print("2. Contratación Directa")
    print("3. Contratación Menor")
    print("4. Contratación de varias empresas")
    print("5. Convenio")
    print("6. Decreto N° 433/16")
    print("7. Licitación Pública")
    print("8. Licitación Privada")
    print("9. Obra de Emergencia")
    print("S. Salir")

    opciones_validas = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "S"]

    while True:
        opcion_contratacion = input("Seleccione una opción (0-9, S): ").upper()
        if opcion_contratacion in opciones_validas:
            if opcion_contratacion == "S":
                return None
            else:
                return opcion_contratacion
        else:
            print("Opción no válida. Intente nuevamente.")


def extraer_Opciones(cls):
    opciones= cls.select()
    print(opciones)
    pk_Opciones = []
    for opcion in opciones:
        print(f"{opcion.id} {opcion.nombre}")
        pk_Opciones.append(opcion.id)
    return pk_Opciones

def extraer_Licitaciones(cls):
    opciones= cls.select()
    pk_Opciones = []
    indices= []
    for indice, opcion in enumerate(opciones):
        print(f"{indice} = {opcion.nro_contratacion}")
        pk_Opciones.append(opcion.nro_contratacion)
        indices.append(indice)
    return pk_Opciones, indices
