def donas_consumidas(a, b):
    if a <0 or b <0:
        raise ValueError("Los numeros ingresados deben ser naturales")
    elif isinstance(a, float) or isinstance(b, float):
        raise TypeError("Los numeros ingresados deben ser naturales")
    else:
        return f"Se consumieron {a*b} donas"

print(donas_consumidas(3.4,5.2))