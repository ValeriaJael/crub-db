from modelo.estudiantes import Estudiantes 
from modelo.curso import Curso 

class EstudianteServicio:
    
    
    
    @staticmethod
    def mostrar_cursos():
        return list (Estudiantes.select())
    @staticmethod
    def crear_estudiante(nombre, curso_id):
        curso = curso.get(Curso.id == curso_id)
        Estudiante = Estudiante.create(nombre=nombre, curso=curso)
        return Estudiante