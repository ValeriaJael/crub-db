from modelo.curso import Curso 

class CursoServicio:
    
    @staticmethod
    def crear_curso(nombre):
        curso = Curso.create(nombre= nombre)
    
    @staticmethod
    def mostrar_cursos():
        return list (Curso.select())