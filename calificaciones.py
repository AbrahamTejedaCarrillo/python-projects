#Calculadora de calificaciones


while True:
    materia1 = input("Ingresa la calificacion de Matematicas: ")
    try:
        materia1 = float(materia1)
        if materia1 < 101:
            break
        else:    
            print ("la calificacion no puede ser mayor a 100")
    except ValueError:
        print ("Entrada invalida")

while True:
    materia2 = input("Ingresa la calificacion de Geografia: ")
    try:
        materia2 = float(materia2)
        if materia2 < 101:
            break
        else:    
            print ("la calificacion no puede ser mayor a 100")
    except ValueError:
        print ("Entrada invalida")

while True:
    materia3 = input("Ingresa la calificacion de Inglés: ")
    try:
        materia3 = float(materia3)
        if materia3 < 101:
            break
        else:    
                print ("la calificacion no puede ser mayor a 100")
    except ValueError:
        print ("Entrada invalida")

print("*"*55)

evaluacion = (materia1+materia2+materia3)/3
lista_calificaciones= [materia1,materia2,materia3]

if evaluacion > 59:
    print(f"El estudiante aprobo con una calificacion de : {round(evaluacion,1)}")
else:
    print(f"El estudiante no aprobo con una calificacion de: {round(evaluacion,1)}")

for i in lista_calificaciones:
    if i == 100:
        print ("El alumno tiene calificacion perfecta en alguna materia")
    elif i <= 60:
        print("El alumno necesita atencion especial en alguna materia")

if evaluacion > 89 and evaluacion <101:
    print("Nota cualitativa: Sobresaliente")
elif evaluacion >79 and evaluacion <90:
    print("Nota cualitativa: Muy bien!")
elif evaluacion >69 and evaluacion <80:
    print("Nota cualitativa: Bien!")
elif evaluacion >59 and evaluacion <70:
    print("Nota cualitativa: Suficiente")
elif evaluacion >0 and evaluacion <60:
    print("Nota cualitativa: Insuficiente")
print("*"*55)
