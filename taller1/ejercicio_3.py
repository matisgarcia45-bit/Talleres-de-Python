#El valor del desempleo en Ibagué aumentó en el primer trimestre un 9.5% y en el segundo
#trimestre cayó en un 1.5%. Calcular el valor del desempleo actual.

valor_desempleo= float(input("ingrese valor actual de desempleo"))
primer_trimestre= valor_desempleo + 0.095
segundo_trimestre= primer_trimestre - 0.015
total= primer_trimestre + segundo_trimestre

print(f"el valor de desempleo actual en Ibagué es:{total:.2f}" )
