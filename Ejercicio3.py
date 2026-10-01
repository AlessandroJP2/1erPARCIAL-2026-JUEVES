def interrupcion_rec(a,b):
    if a == 0:
        return f"No hubo interrupciones"
    else:
        return interrupcion_rec(b, a*b) + f"Hubo {a} interrupciones"

print(interrupcion_rec(0,2))