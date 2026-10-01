eventos = ["Kermés", "Concurso de comida", "Reunión del consejo municipal"]

def organizar_eventos (eventos = [], expresion = False):
    eventos = eventos.copy()
    if expresion == True:
        eventos = eventos.sort(reverse = True)
    else:
        eventos = eventos.sort()
    return eventos

print(organizar_eventos(eventos))
    