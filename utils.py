from peewee import *

# funcion para crear dinamicamente registros unicos utilizando unpacking operator
def create_new_record(table, property, value):

	dict_content = {
		property: value
	}

	try:
		table.get_or_create(**dict_content)

	except IntegrityError as e:
		print("Error insertando comuna", e)
