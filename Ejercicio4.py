eventos = ["Kermés", "Concurso de comida", "Reunión del consejo municipal"]

def organizar_eventos (eventos = [], expresion = False):
    if expresion == True:
        return eventos.sort(reverse = True)
    else:
        return eventos.sort()

print(organizar_eventos(eventos))
    