from peewee import Model, AutoField, CharField, DateField, TimeField
from basedato.db import db

class Curso (Model):
    id = AutoField
    nombre = CharField(unique= True)
    descripcion = CharField()
    fecha_inicio = DateField()
    fecha_fin = DateField()
    horas = TimeField()

    class Meta: #Vincula este modelo a la base de datos
        database = db
        table_name = 'cursos'