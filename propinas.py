

#Inputs en loops while

while True:
    total = input("Ingresa el total de la cuenta: $")
    try:
        valor_numerico = float(total)
        break 
    except ValueError:
        print("eso no es un numero w")

while True:
    propina = input("Ingresa el porcentaje de propina: ")
    try:
        valor_numerico = float(propina)
        break 
    except ValueError:
        print("Eso no es un numero w")

while True:
    personas = input("Ingresa la cantidad de personas a dividir la cuenta: ")
    try:
        valor_numerico = float(personas)
        break  
    except ValueError:
        print("Eso no es un numero w")

#conversiones
total = float(total)
propina = float(propina)
personas = float(personas)

#operaciones
porcentaje_propina_general = propina*total/100
costo_alimentos_personal = total/personas
propina_individual = porcentaje_propina_general/personas
pago_personal = costo_alimentos_personal+propina_individual



#output
print("\n")
print("*"*45)
print("--------------TACOS LOS PADRINOS-------------")
print("*"*45)
print("-"*45)
print(f"\nEl total de la cuenta es: ${round(total+porcentaje_propina_general)}\n")
print("-"*45)
print(f"\nEl total de propina a pagar por persona es: \n${round(propina_individual,2)} \n")
print("-"*45)
print(f"\nEl total a pagar por persona es: ${round(pago_personal,2)}\n")
print("-"*45)
print("*"*45)
print("------------GRACIAS POR SU COMPRA------------")
print("*"*45)
print("\n")
