eventos = ["Kermés", "Concurso de comida", "Reunión del consejo municipal"]

def organizar_eventos (eventos, expresion = False):
    if expresion == True:
        return sorted(eventos, reverse = True)
    else:
        return sorted(eventos, reverse = False)

print(organizar_eventos(eventos, True))
    