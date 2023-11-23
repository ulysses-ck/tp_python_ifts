from peewee import *

def create_new_record(table, property, value):

	dict_content = {
		property: value
	}

	try:
		table.create(**dict_content)

	except IntegrityError as e:
		print("Error insertando comuna", e)
