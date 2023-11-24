import random
from datetime import datetime
from peewee import *
from modelo_orm import Obra


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


def mostrar_menu(obra):
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
                monto_contrato,
                direccion,
                plazo_meses,
                beneficiarios,
                mano_obra,
                porcentaje_avance,
            ) = obtener_datos_nueva_obra()
            obra.nuevo_proyecto(
                nombre,
                descripcion,
                monto_contrato,
                direccion,
                plazo_meses,
                beneficiarios,
                mano_obra,
                porcentaje_avance,
            )
            #nueva_obra_instancia = obra.nueva_obra()
            print("Nueva instancia de obra creada:", nueva_obra_instancia)
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
    monto_contrato = float(input("Ingrese el monto del contrato: "))
    direccion = input("Ingrese la dirección del proyecto: ")
    plazo_meses = int(input("Ingrese el plazo en meses: "))
    beneficiarios = input("Ingrese los beneficiarios del proyecto: ")
    mano_obra = input("Ingrese la mano de obra: ")
    porcentaje_avance = float(input("Ingrese el porcentaje de avance: "))

    return (
        nombre,
        descripcion,
        monto_contrato,
        direccion,
        plazo_meses,
        beneficiarios,
        mano_obra,
        porcentaje_avance,
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


