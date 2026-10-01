def interrupcion_rec(a: int,b: int) -> int:
    if a == 0:
        return f"No hubo interrupciones"
    else:
        return interrupcion_rec(a*b, b) + f"Bart interrumpio {a} veces a Marge"

print(interrupcion_rec(3,5))