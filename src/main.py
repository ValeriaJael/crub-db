from basedato.db import db
from modelo.curso import Curso
from modelo.estudiantes import Estudiantes
from controlador.curso_controlador import CursoControlador

def main ():
    db.connect()
    db.create_tables([Curso, Estudiantes])

    CursoControlador.crear("Programacion II", "En este curso aaprenderas a programar", "1 de septiembre", "finaliza 20:00", "Dura 5 horas")

if __name__ == '__main__':
    main()

