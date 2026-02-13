infoCampers=[{
    "nombre":0,
    "apellidos":0,
    "direccion":0,
    "acudiente":0,
    "telCel":0,
    "TelFijo":0,
    "Estado":0,
    "Riesgo":0,
}]

print ("Menú principal")
print("¿Quién eres?")
print("1.Camper")
print("2.Trainer")
print("3.Coordinador")
opcion1=int(input(": "))
if opcion1==1:
    print("Bienvenido al menú de camper")
    print("¿que deseas ver?")
    print("1.Inscribirse al programa")
    print("2.Ver estado")
    opcamper=int(input(": "))
    if opcamper==1:
        nuevo={
            "nombre":0,
            "apellidos":0,
            "direccion":0,
            "acudiente":0,
            "telCel":0,
            "TelFijo":0,
            "Estado":0,
            "Riesgo":0,
        }
        print ("Bienvenido a el registro")
        print("Recuerda que solo te debes registrar una vez")
        print ("presiona ENTER para inicial")
        input ("")
        print("¿cual es tu nombre?")
        nuevo["nombre"]=input(": ")
        print ("Apellido")
        nuevo["apellidos"]=input(": ")
        print("direccion")
        nuevo["direccion"]=input(": ")
        print("Acudiente")
        nuevo["acudiente"]=input(": ")
        print("telefono celular")
        nuevo["telCel"]=input(": ")
        print("telefono fijo")
        nuevo["TelFijo"]=input(": ")
        infoCampers.append(nuevo)
        print("Ya quedaste registrado :D")
        print("Diste el primer paso, El más importante")
    if opcamper==2:
        print("")
        nombreBuscar=input("Nombre con el que te registraste (Recuerda escribirlo igual)")
        apellidoBuscar=input("¿Cual es tu apellido?")
        for i in range (len(infoCampers)):
            if infoCampers[i]["nombre"] == nombreBuscar and infoCampers[i]["apellidos"]== apellidoBuscar:
                print("Estado:",infoCampers[i]["estado"])
if opcion1==2:
    print("Eres Trainer")
if opcion1==3:
    print("Eres Administrador")
    print ("hola")