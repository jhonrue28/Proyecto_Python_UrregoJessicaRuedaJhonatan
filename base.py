#Diccionario para campers
#RECUERDA QUE TODO ESTO ESTÁ SIN PERSISTENCIA.
infoCampers=[{
    "nombre":0,
    "apellidos":0,
    "direccion":0,
    "acudiente":0,
    "telCel":0,
    "TelFijo":0,
    "Estado":0,
    "Riesgo":0,
    "notas":[0,0,0]
}]
#Diccionario información básica de trainers
trainers =[{
    "nombre" :"Edwen salas",
    "ruta": ["java", "netcore"],
    "horario": "6:00-14:00"
    },{ 
    "nombre" :"Jolver",
    "ruta": ["JAVA ","netcore"],
    "horario": "6:00-14:00"
    },{
    "nombre": "Kevin David",
    "ruta": "JAVA",
    "horario ":"6:00- 14:00"

    },{
    "nombre" :"Pedro Gomez",
    "ruta": ["JAVA ", "netcore"],
    "horario": "6:00-14:00"
    },{
    "nombre" : "Cristian ",
    "ruta": ["JAVA","nodejs"],
    "horario": "10:00-18:00"
    },{
    "nombre": "Carlos Rueda",
    "ruta": "JAVA",
    "horario": "2:00-22:00"
}] 

#Ciclo para el menú principal de asignacion de roles
booleanito=True
while booleanito==True:
    print ("Menú principal")
    print("¿Quién eres?")
    print("1.Camper")
    print("2.Trainer")
    print("3.Coordinador")
    print("4.Salir del programa")
    opcion1=int(input(": "))
    if opcion1==1:
        #Ciclo para el rol de Camper
        condcamper=True
        while condcamper==True:
            print("Bienvenido al menú de camper")
            print("¿que deseas ver?")
            print("1.Inscribirse al programa")
            print("2.Ya estoy inscrito")
            print("3.Salir del perfil de Camper")
            opcamper=int(input(": "))
            if opcamper==1:
                #Creacion de un nuevo camper para inscribirlo
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
                print("¿cual es tu nombre? OJO solo nombre, no apellidos")
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
                #El siguiente algoritmo es el cual agrega a la lista el Camper que de está inscribiendo lista.append(¿Que añades?)
                infoCampers.append(nuevo)
                print("Ya quedaste registrado :D")
                print("Diste el primer paso, El más importante")
            if opcamper==2:
                print("")
                print("Primero queremos reconocerte :P")
                nombreBuscar=input("Nombre con el que te registraste  / solo nombre, no apellido (Recuerda escribirlo igual)")
                apellidoBuscar=input("¿Cual es tu apellido?")
                for i in range (len(infoCampers)):
                    #El ciclo for lo que hace es buscar en el diccionario de infocampers uno en el cual el nombre y apellido sean el mismo
                    if infoCampers[i]["nombre"] == nombreBuscar and infoCampers[i]["apellidos"]== apellidoBuscar:
                        print("Bienvenido ",infoCampers[i]["nombre"])
                        print("tu estado actual es: ",infoCampers[i]["Estado"])
                        print("Que deseas hacer?")
                        print("1.¿Cual es mi ruta?")
                        print("2.¿Cuales son mis notas?")
                        print("3.Retirarse")
                        decision2=int(input(": "))
                        if decision2==1:
                            #Falta programar para que podamos hacer que el vea la ruta la cual le tocó, el treiner, el salón y el horario
                            print("Falta programar para poner la ruta")
                        if decision2==2:
                            print ("tus notas son: ",infoCampers[i]["notas"])
                        if decision2==3:
                            print("¿Estás seguro de querer retirarte?")
                            print("1. Si, 2. No")
                            confirmacion=int(input(": "))
                            if   confirmacion==1:
                                #Cambia su propio estado a RETIRADO
                                print("Esperamos te vaya super bien")
                                print("Muchas gracias por haber estado acá")
                                infoCampers[i]["Estado"]= "Retirado"
            if opcamper==3:
                print(" ")
                print("-_-")
                print("Te estaré vigilando")
                print("Vuelve pronto :D")
                condcamper=False
                print(" ")
    if opcion1==2:
        #Falta programar para hacer las funciones de treiner
        print("Eres Trainer")
    if opcion1==3:
        #Falta hacer el menú de administrador. pero está hecha la funcion de cambiar el estado de un camper 
        print("Eres Administrador")
        print("Cambiar Estado de estudiante")
        nombreBuscar=input("Nombre del CamperSsolo nombre, no apellido")
        apellidoBuscar=input("¿Cual es el apellido?")
        for i in range (len(infoCampers)):
            #Busca un camper con ese nombre y ese apellido y se mete en el perfil de el para modificar el estado , pero hay que agregar el resto de funciones.
            if infoCampers[i]["nombre"] == nombreBuscar and infoCampers[i]["apellidos"]== apellidoBuscar:
                print("En que estado vas a poner al Camper?")
                print("1.Aprobado")
                print("2.Expulsado")
                print("3.Retirado")
                decisionA=int(input(": "))
                if decisionA==1:
                    infoCampers[i]["Estado"]="Aprobado"
                if decisionA==2:
                    infoCampers[i]["Estado"]="Aprobado"
                if decisionA==3:
                    infoCampers[i]["Estado"]="Aprobado"
            else:
                print("No hay un estudiante registrado con ese nombre")
                print(" ")
                        
    if opcion1==4:
        #Cierre del sistema
        print("Gracias por usar nuestro sistema")
        print("Te esperamos pronto")
        print(":D")
        booleanito=False