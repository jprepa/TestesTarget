def inverter_string(s):
    resultado = ""
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado


texto = input("Informe uma string: ")
print(f"String invertida: {inverter_string(texto)}")
