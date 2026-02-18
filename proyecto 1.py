import json

#Diccionario para campers
def lecturaInfocampers():
    with open('./infoCampers.json', "r") as f:
        infoCampers = json.load(f)
        return infoCampers

trainers = [
    {"nombre": "Edwen salas", "ruta": ["java", "netcore"], "horario": "6:00-14:00"},
    {"nombre": "Jolver", "ruta": ["java", "netcore"], "horario": "6:00-14:00"},
    {"nombre": "Kevin David", "ruta": ["java"], "horario": "6:00-14:00"},
    {"nombre": "Pedro Gomez", "ruta": ["java", "netcore"], "horario": "6:00-14:00"},
    {"nombre": "Cristian", "ruta": ["java", "nodejs"], "horario": "10:00-18:00"},
    {"nombre": "Carlos Rueda", "ruta": ["java"], "horario": "2:00-22:00"}
]

# PRIMER PASO: cargar o crear rutas.json
try: #evita que se rompa el codigo si hay un error
    with open("rutas.json", "r") as f:
        rutas = json.load(f)
except FileNotFoundError:
    modulos = [
        "Fundamentos de programación",
        "Programación Web",
        "Programación formal",
        "Bases de datos",
        "Backend"
    ]
    salones = {"NodeJS": "A1", "Java": "B1", "NetCore": "C1"}
    capacidad_salon = 35

    rutas = {}
    for ruta in ["NodeJS", "Java", "NetCore"]:
        ruta_lower = ruta.lower() # lowe convertir texto a minusculas
        disponibles = [t["nombre"] for t in trainers if ruta_lower in [r.lower() for r in t["ruta"]]] #t itinera
        principal = disponibles[0] if disponibles else ""
        rutas[ruta] = {
            "capacidad_salon": capacidad_salon,
            "campers": [],
            "trainer": principal,
            "trainers_disponibles": disponibles,
            "salon": salones[ruta],
            "modulos": modulos
        }

    # Guardar el JSON por primera vez
    with open("rutas.json", "w") as f:
        json.dump(rutas, f, indent=4)




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
                        "id": 1234,
                        "nombre": "Jessica",
                        "apellidos": "Urrego",
                        "direccion": "calle 10 #47-12",

                        "contacto": {
                            "acudiente": "Maria Leal",
                            "celular": "324563548",
                            "telefonoFijo": "6098754"
                        },

                        "academico": {
                            "estado": "Aprobado",
                            "riesgo": "Bajo",
                            "ruta": "NetCore",
                            "salon": 0,
                            "trainer":0 ,
                            "modulos": [
                            {
                                "teorica": 60,
                                "practica": 68,
                                "trabajos": 90,
                                "final": 67.8
                            }
                            ]
                        }
                    }
                    print ("Bienvenido a el registro")
                    print("Recuerda que solo te debes registrar una vez")
                    print ("presiona ENTER para inicial")
                    input ("")

                    nuevo["id"]=int(input("Digita tu número de documento : "))
                    print("¿cual es tu nombre? OJO solo nombre, no apellidos")
                    nuevo["nombre"]=input(": ")
                    print ("Apellido")
                    nuevo["apellidos"]=input(": ")
                    print("direccion")
                    nuevo["direccion"]=input(": ")
                    print("Acudiente")
                    nuevo["contacto"]["acudiente"]=input(": ")
                    print("telefono celular")
                    nuevo["contacto"]["telCel"]=input(": ")
                    print("telefono fijo")
                    nuevo["contacto"]["TelFijo"]=input(": ")
                    
                    infoCampers.append(nuevo)
                    json.dump(infoCampers, f, indent=4)

                print(" ")
                print("Ya quedaste registrado :D")
                print("Diste el primer paso, El más importante")
                print(" ")
            if opcamper==2:
                print("")
                print("Primero queremos reconocerte :P")
                nombreBuscar=input("Nombre con el que te registraste  / solo nombre, no apellido (Recuerda escribirlo igual)")
                apellidoBuscar=input("¿Cual es tu apellido?")
                infoCampers = lecturaInfocampers()
                for i in range (len(infoCampers)):
                    if infoCampers["campers"][i]["nombre"].lower().strip()== nombreBuscar.lower().strip() and infoCampers["campers"][i]["apellidos"].lower().strip()==apellidoBuscar.lower().strip():
                        booleanito2=True
                        while booleanito2==True:
                            print(" ")
                            print("Bienvenido ",infoCampers["campers"][i]["nombre"])
                            if infoCampers["campers"][i]["academico"]["estado"]==0:
                                infoCampers["campers"][i]["academico"]["estado"]="Postulado"
                            print("tu estado actual es:",infoCampers["campers"][i]["academico"]["estado"])
                            print("Que deseas hacer?")
                            print("1.¿Cual es mi ruta?")
                            print("2.¿Cuales son mis notas?")
                            print("3.Retirarse")
                            print("4.Volver Menu Principal")
                            print(" ")
                            decision2=int(input(''))
                            if decision2==1:
                                if infoCampers["campers"][i]["academico"]["ruta"] !=0:
                                    print("Tu ruta es:", infoCampers["campers"][i]["academico"]["ruta"])
                                    print("Tu salón es:", infoCampers["campers"][i]["academico"]["salon"])
                                    print("Tu trainer encargado es:", infoCampers["campers"][i]["academico"]["trainer"])
                                    print(" ")
                                else:
                                    print("Aún no te han asignado una ruta.")
                                    print(" ")
                                
                            if decision2==2:
                                if infoCampers["campers"][i]["academico"]["modulos"] != 0:
                                    print("Tus notas son:", infoCampers["campers"][i]["academico"]["modulos"])
                                else:
                                    print("Aún no tienes notas asignadas.")
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
                                        infoCampers["campers"][i]["estado"]= "Retirado"
                                        json.dump(infoCampers, f)
                            if decision2 == 4:
                                print("Volviendo al menú principal...")
                                booleanito2 = False
                                break 
                    else:
                        print (" ")
                        print("El nombre no está inscrito en el programa")
                        print(" ")
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
       
     def ver_campers(infoCampers):
        print("\n--- LISTADO DE CAMPERS ---")
        for i in range(len(infoCampers["campers"])):
            print(f"{i+1}. {infoCampers['campers'][i]['nombre']} {infoCampers['campers'][i]['apellido']}")
            print(f"   Estado: {infoCampers['campers'][i]['estado']}")
            print(f"   Ruta: {infoCampers['campers'][i]['ruta']}")
            print("-" )

     def crear_salon(salones):
            nombre = input("Nombre del nuevo salón (Sputnik/Artemis/Apolo): ")
            nuevo_salon = {"nombre": nombre, "capacidad": 35}
            datos["salones"].append(nuevo_salon)
            print(f"Salón {nombre} creado con éxito.")

     def ver_trainers(trainers):
            print("\n--- LISTADO DE TRAINERS ---")
            for i in range(len(trainers)):
                print(f"{i+1}. {trainers[i]['nombre']}")
                print(f"   Rutas: {trainers[i]['ruta']}")
                print(f"   Horario: {trainers[i]['horario']}")
                print("-" )

     def ver_rutas(rutas):
            print("\n--- RUTAS DISPONIBLES ---")
            for i in range(len(rutas)):
                print(f"{i+1}. {ver_rutas[i]['nombre']}")
     def asignar_camper_a_ruta(infoCampers):
      print("\n--- ASIGNAR CAMPER A RUTA ---")
    
    # 1. Pedimos el ID directamente
      documento = input("Ingrese el número de identificación del camper: ")

    # 2. Buscamos al camper con un for i
     for i in range(len(datos["campers"])):
        
        # Si encontramos al camper con ese ID:
        if datos["campers"][i]["id"] == documento:
            
            # Verificamos si aprobó
            if datos["campers"][i]["estado"] == "Aprobado":
                
                print(f"Camper {datos['campers'][i]['nombre']} encontrado.")
                nueva_ruta = input("Ingrese el nombre de la ruta (Java, NodeJS, NetCore): ")
                
                # Cambiamos los datos directamente usando [i]
                datos["campers"][i]["ruta"] = nueva_ruta
                datos["campers"][i]["estado"] = "Cursando"
                
                print("¡Ruta asignada con éxito!")
               return # Salimos de la función porque ya lo encontramos
            else:
                print("El camper aún no está aprobado.")
               return

    # Si el bucle termina y no encontró nada:
    print("No se encontró ningún camper con ese número de identificación.")

     def menu_coordinador(datos):
            while True:
                print("\n===== MENÚ COORDINADOR =====")
                print("1. Ver Campers")
                print("2. Crear Salón")
                print("3. Ver Trainers")
                print("4. Ver Rutas")
                print("5. Asignar Camper a Ruta")
                print("6. Salir")

                opcion = input("Seleccione: ")

                if opcion == "1":
                    ver_campers(infoCampers)
                elif opcion == "2":
                    crear_salon(salones)
                elif opcion == "3":
                    ver_trainers(trainers)
                elif opcion == "4":
                    ver_rutas(ruta)
                elif opcion == "5":
                    asignar_camper_a_ruta(infoCampers)
                elif opcion == "6":
                    # Aquí llamarías a tu función para guardar el JSON
                    print("Guardando datos y saliendo...")
                    break
                else:
                    print("Opción inválida")

    
    if opcion1==4:
        print("Gracias por usar nuestro sistema")
        print("Te esperamos pronto")
        print(":D")
        booleanito=False