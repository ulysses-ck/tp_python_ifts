from peewee import *

def create_unique_values(table, property, value):
	try:
		table[property] = value
	except IntegrityError as e:
		print(f"error: {e}")
