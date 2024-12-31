#Perfil personal actividad 3 club de programación 3

#Inputs
nombre = input("\nIngresa tu nombre completo: ")
nombre_sin_espacios = nombre.replace(" ","")
#Loop while verifica si es un numero y si es menor a 100
while True:
    edad = input("\nIngresa tu edad: ")
    try:
        edad = int(edad)
        if edad < 100:
            break
        else:
            print("Nmms no tienes mas de 100 años no seas mentiros@")
    except ValueError:
        print("Caracter incorrecto")

residencia = input("\nIngresa tu lugar de residencia: ")
pasatiempos = input("\nIngresa tus pasatiempos favoritos: ").lower()
pasatiempos_separados = list(pasatiempos.split())

#Outputs
print("\n","*"*45,"\n")
print("Resumen de la información del usuario\n")
print(f"Nombre completo en mayusculas: {nombre.upper()}")
print(f"Longitud del nombre: {len(nombre_sin_espacios)}")
print(f"Edad: {edad}")
print(f"Ciudad de residencia (capitalizada): {residencia.title()}")

#Verifica que "leer esté o no en los pasatiempos para agregarlo"
if "leer" not in pasatiempos:
    pasatiempos_separados.insert(1,"Leer")
elif "leer" in pasatiempos_separados[:]:
    pasatiempos_separados.remove("leer")
    pasatiempos_separados.insert(1,"Leer")

contador = 0
print("Tus pasatiempos favoritos:")
for i in pasatiempos_separados:
    contador += 1
    print(contador,i.capitalize())
print("\n","*"*45,"\n")