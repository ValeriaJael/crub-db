from peewee import Model, AutoField, CharField, IntegerField, DateField, ForeignKeyField
from basedato.db import db
from modelo.curso import Curso

class Estudiantes (Model):
    id = AutoField
    nombre = CharField(unique= True)
    dni =  CharField()
    email = CharField()
    telefono = IntegerField()
    fecha_nacimiento= DateField()
    curso_id = ForeignKeyField(Curso)


    class Meta: #Vincula este modelo a la base de datos
        database = db
        table_name = 'estudiantes'


    