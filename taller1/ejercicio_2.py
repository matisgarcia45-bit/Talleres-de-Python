#solicitar el area  
area_original=int(input("ingrese el area en metros cuadrados: "))

#calcular el 20% de aumento
aumento= area_original * 0.20

#calcular el area con el aumento
area_total= area_original + aumento

#mostrar los resultados
print(f"area original: {area_original} metros cuadrados")
print(f"aumento del 20%: {aumento} metros cuadrados")
print(f"area total: {area_total} metros cuadrados")