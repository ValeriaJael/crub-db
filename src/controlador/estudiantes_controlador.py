from servicio.estudiantes_servicio import EstudianteServicio

class EstudiantesControlador():

    def crear ( id, nombre,dni, email ,telefono, fecha_nacimiento, curso_id):
        return EstudianteServicio.crear_Estudiantes(id, nombre,dni, email ,telefono, fecha_nacimiento, curso_id)
    
    def mostrar():
        return EstudianteServicio.mostrar_estudiantes()