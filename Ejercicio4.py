eventos = ["Kermés", "Concurso de comida", "Reunión del consejo municipal"]

def organizar_eventos (eventos, expresion = False):
    if expresion not in(True,False):
        raise ValueError("El valor ingresado no es válido")
    elif expresion == True:
        return sorted(eventos, reverse = True)
    elif expresion == False:
        return sorted(eventos, reverse = False)


print(organizar_eventos(eventos, True))
    