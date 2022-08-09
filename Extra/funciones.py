#Funciones -> def nombre(parametro,*args,**kwargs)
## args es una lista de argumentos
## kwargs es un diccionario con claves y valores

def perimetro(*args):
    perimetro=0
    for lado in args:
        perimetro+=lado
    return perimetro

print(perimetro(1,2,3,4))


def funcion_alumnos(**kwargs):
    print(kwargs)
    for llave,valor in kwargs.items():
        print(f"Llave: {llave}, valor: {valor}")
    print(kwargs['nombre'],kwargs['apellido'])

funcion_alumnos(nombre="Hernan", apellido="Fresco")