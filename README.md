# Trabajo Practico Final Integrador - Desarrollo de Sistemas Orientados a Objetos

## Integrantes

* Apaza, Ulises
* Amezaga, Diego
* Soto, Jamil
* Soarez Viana, Leonardo
* Calanna, Cecilia

# Objetivos
El propósito de este proyecto es diseñar y desarrollar un sistema para la gestión de obras públicas, utilizando los principios de la programación orientada a objetos para estructurarlo. Además, implementamos el ORM Peewee para facilitar la persistencia de objetos en una base de datos SQLite.

## Importación de Datasets:
Este proyecto puede importar datasets desde archivos CSV.

## Persistencia de Objetos con ORM Peewee:

ORM significa "Object-Relational Mapping", o "Mapeo Objeto-Relacional". Esta técnica de programación permite interactuar con bases de datos relacionales utilizando objetos de programación.
En este caso usamos el ORM Peewee para interactuar con la base de datos SQLite. Diseñamos modelos que representan las entidades necesarias, para la persistencia de datos.

## Get started
Create a new virtual environment with python in another directory that doesn't be the root project (optional)
```sh
python -m venv tp_python
```
Activate it with this line, for example to use it in powershell (optional)
```sh
cd tp_python
.\Scripts\Activate.ps1
```
Run this command to install dependencies
```sh
pip install -r requirements.txt
```

## ERD (Entity Relationship Diagram)
https://raw.githubusercontent.com/ulysses-ck/tp_python_ifts/main/diagram/ObrasPublicasDiagramaTablas.drawio.svg

## Contributing
### Clone repository
```sh
git clone https://github.com/ulysses-ck/tp_python_ifts.git
cd tp_python_ifts
```

### Make your changes and create a new branch 
```sh
git checkout -b dev
git add .
git commit -m "feat: [new feature]"
```
