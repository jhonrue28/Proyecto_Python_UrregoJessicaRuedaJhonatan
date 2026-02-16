#Diccionario para campers
#RECUERDA QUE TODO ESTO ESTÁ SIN PERSISTENCIA.
import json
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
                with open("infoCampers.json", "r+") as f:
                    infoCampers = json.load(f)                  
                #Creacion de un nuevo camper para inscribirlo
                    nuevo= {
                    "Id": 0,
                    "nombre":0,
                    "apellidos":0,
                    "direccion":0,
                    "acudiente":0,
                    "telCel":0,
                    "TelFijo":0,
                    "Estado":0,
                    "Riesgo":0,
                    }
                with open("infoCampers.json", "r+") as f:
                    
                    print ("Bienvenido a el registro")
                    print("Recuerda que solo te debes registrar una vez")
                    print ("presiona ENTER para inicial")
                    input ("")
                #print(f"Tu ID asignado es: {id_generado}")
                    
                    nuevo["id"]=int(input("Digita tu número de documento : "))
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
                    json.dump(infoCampers,f)
                    
                    
                    print("Ya quedaste registrado :D")
                    print("Diste el primer paso, El más importante")
            if opcamper==2:
                print("")
                print("Primero queremos reconocerte :P")
                nombreBuscar=input("Nombre con el que te registraste  / solo nombre, no apellido (Recuerda escribirlo igual)")
                apellidoBuscar=input("¿Cual es tu apellido?")
                for i in range (len("infoCampers")):
                    with open("infoCampers.json", "r") as f:
                        infoCampers = json.load(f)
                        #El ciclo for lo que hace es buscar en el diccionario de infocampers uno en el cual el nombre y apellido sean el mismo
                        if infoCampers[i]["nombre"]== nombreBuscar and infoCampers[i]["apellidos"]== apellidoBuscar:
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
                                print ("tus notas son: ",infoCampers[i]["notas_modulos"])
                            if decision2==3:
                                print("¿Estás seguro de querer retirarte?")
                                print("1. Si" " 2. No")
                                confirmacion=int(input(": "))
                                if   confirmacion==1:
                                    with open("infoCampers.json", "r+") as f:
                                        infoCampers = json.load(f)
                                        #Cambia su propio estado a RETIRADO
                                        print("Esperamos te vaya super bien")
                                        print("Muchas gracias por haber estado acá")
                                        infoCampers[i]["Estado"]= "Retirado"
                                        json.dump(infoCampers, f)
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
  
    if opcion1 == 3:
           
     print("\n--- MENÚ COORDINADOR ---")
     with open("infoCampers.json", "r") as f:
        infoCampers = json.load(f)
       
        print("¿Cómo deseas buscar al Camper?")
        print("1. Por ID")
        print("2. Por Nombre y Apellido")
        
        metodo = int(input(": "))

        camper_encontrado = None

        if metodo == 1:
            id_buscar = int(input("Ingrese el ID: "))
            for c in infoCampers:
                if infoCampers[c]["id"] == id_buscar:
                    camper_encontrado = c
                    break
        elif metodo == 2:
            nom = input("Nombre: ")
            ape = input("Apellido: ")
            for c in infoCampers:
                if c.get("nombre")== nom and c.get("apellidos") == ape:
                    camper_encontrado = c
                    break

            if camper_encontrado:
                print(f"\nCamper seleccionado: {camper_encontrado['nombre']} (Estado: {camper_encontrado['Estado']})")
                print("1. Cambiar Estado (Aprobado/Expulsado/etc)")
                print("2. Asignar Ruta de Entrenamiento")
                print("3. Registrar Notas De Estudiante")
                accion = int(input(": "))

                if accion == 1:
                    print("Estados: 1.Aprobado, 2.Expulsado, 3.Retirado")
                    nuevo_est = int(input(": "))
                    mapa = {1: "Aprobado", 2: "Expulsado", 3: "Retirado"}
                    if nuevo_est in mapa:
                        camper_encontrado["Estado"] = mapa[nuevo_est]
                        print("Estado actualizado.")

                if accion == 2:
                    if camper_encontrado["Estado"] == "Aprobado":
                        print("Rutas: 1.NodeJS, 2.Java, 3.NetCore")
                        r = int(input(": "))
                        mapa_r = {1: "NodeJS", 2: "Java", 3: "NetCore"}
                        if r in mapa_r:
                            camper_encontrado["Ruta"] = mapa_r[r]
                            camper_encontrado["Estado"] = "Aprobado"
                            print(f"Asignado a {mapa_r[r]}")
                    else:
                        print("Error: El camper debe estar 'Aprobado' para asignar ruta.")

                # GUARDAR CAMBIOS: Sobrescribimos el archivo con la lista actualizada
                with open("infoCampers.json", "w") as f: 
                    json.dump(infoCampers, f, indent=4)

                if accion == 3: # Nueva opción: Registrar Notas de Módulo
                    print("\n--- REGISTRO DE NOTAS DE MÓDULO ---")
                # Solo se evalúa si está cursando una ruta
                    if camper_encontrado["Estado"] == "Aprobado":
                        try:
                            nota_teorica = float(input("Ingrese nota Teórica (30%): "))
                            nota_practica = float(input("Ingrese nota Práctica (60%): "))
                            nota_trabajos = float(input("Ingrese nota de Quices/Trabajos (10%): "))
                            
                            # Cálculo con porcentajes
                            nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_trabajos * 0.1)
                            
                            print(f"\nLa nota final obtenida es: {nota_final:.2f}")

                            # Guardamos el historial de notas en el objeto del camper
                            if "notas_modulos" not in camper_encontrado:
                                camper_encontrado["notas_modulos"] = []
                            
                            registroNotas= {
                            "teorica": nota_teorica,
                            "practica": nota_practica,
                                "trabajos": nota_trabajos,
                                "final": nota_final
                            }
                            camper_encontrado["notas_modulos"].append(registroNotas)

                            # Lógica de Rendimiento Bajo (Llamado de atención)
                            if nota_final < 60:
                                camper_encontrado["Riesgo"] = "Alto"
                                print("¡ALERTA!: Rendimiento bajo. Se ha generado un llamado de atención.")
                            else:
                                camper_encontrado["Riesgo"] = "Bajo"
                                print("Módulo aprobado satisfactoriamente.")

                        except ValueError:
                            print("Error: Ingrese solo números para las notas.")
                        else:
                            print("Error: Solo se pueden registrar notas para campers en estado 'Aprobado'.")

                    # Guardar cambios en el JSON
                    with open("infoCampers.json", "w") as f:
                        json.dump(infoCampers, f, indent=4)
            else:
                    print("No se encontró ningún camper con esos datos.")
#Cierre del sistema
    if opcion1==4:
        print("Gracias por usar nuestro sistema")
        print("Te esperamos pronto")
        print(":D")
        booleanito=False