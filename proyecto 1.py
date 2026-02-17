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
           
     print("\n--- MENÚ COORDINADOR ---")
     with open("infoCampers.json", "r") as f:
        infoCampers = json.load(f)
       
        print("¿Cómo deseas buscar al Camper?")
        print("1. Por ID")
        print("2. Por Nombre y Apellido")
        print("3. Volver Atras")
        
        metodo = int(input(": "))

        camper_encontrado = None

        if metodo == 1:
            id_buscar = int(input("Ingrese el ID: "))
            if infoCampers["campers"][i]["id"] == id_buscar:
                camperEncontrado=True
        elif metodo == 2:
            nom = input("Nombre: ")
            ape = input("Apellido: ")
            if infoCampers["campers"][i]["nombre"].lower().strip()== nom.lower().strip() and infoCampers["campers"][i]["apellidos"].lower().strip()==ape.lower().strip():
                camperEncontrado=True
                  
            if camper_encontrado==True:
                print(f"\nCamper seleccionado: {infoCampers["campers"][i]["academico"]['nombre']} (Estado: {infoCampers["campers"][i]["academico"]['Estado']})")
                print("1. Cambiar Estado (Aprobado/Expulsado/etc)")
                print("2. Asignar Ruta de Entrenamiento")
                print("3. Registrar Notas De Estudiante")
                print("4. Volver atras")
                accion = int(input(": "))

                if accion == 1:
                        print("Estados: 1.Aprobado, 2.Expulsado, 3.Retirado")
                        nuevo_est = int(input(": "))
                        mapa = {1: "Aprobado", 2: "Expulsado", 3: "Retirado"}
                        if nuevo_est in mapa:
                            infoCampers["campers"][i]["academicas"]["Estado"] = mapa[nuevo_est]
                        print("Estado actualizado.")
                if accion == 2:
                        with open('./rutas.json', "r+") as f:
                            rutas = json.load(f)

                        print("\n--- RUTAS DISPONIBLES ---")
                        for i in range(len(rutas)):
                            if rutas[i]["capacidad"]< rutas[i]["integrantes"]:
                                print(rutas[i]["Nombre"])
                                print("horarios disponibles")

                        ruta_elegida = input("Ingrese la ruta a asignar: ")

                        if ruta_elegida in range:
                            ruta_info = rutas[ruta_elegida]
                        if len(ruta_info["campers"]) < ruta_info["capacidad_salon"]:
                            # Guardamos la asignación dentro del camper
                            camper_encontrado["Ruta"] = ruta_elegida
                            camper_encontrado["Salon"] = ruta_info["salon"]
                            camper_encontrado["Trainer"] = ruta_info["trainer"]
                            camper_encontrado["Estado"] = "Cursando"

                            # Actualizamos la lista de campers de la ruta
                            ruta_info["campers"].append(camper_encontrado["Id"])

                            # Guardamos cambios en ambos JSON
                            with open("infoCampers.json", "w") as f:
                                json.dump(infoCampers, f, indent=4)
                            with open("rutas.json", "w") as f:
                                json.dump(rutas, f, indent=4)

                            print(f" Camper {camper_encontrado['nombre']} asignado a {ruta_elegida} con Trainer {ruta_info['trainer']} en el salón {ruta_info['salon']}")
                        else:
                            print(" La ruta seleccionada ya alcanzó su capacidad máxima")
                        
                            print(" Ruta inválida") 
                if accion == 3: # Nueva opción: Registrar Notas de Módulo
                 print("\n--- REGISTRO DE NOTAS DE MÓDULO ---")
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
                            with open("infoCampers.json", "w") as f:
                              json.dump(infoCampers, f, indent=4)
                     
                    except ValueError:
                            print("Error: Ingrese solo números para las notas.")
                else:
                    print("Camper no encontrado en el JSON")
                    print("Aún no existe para nosotros :P")
                    print("Busquemos a alguien con ese nombre o ID JAJAJJAJAJ")
    if opcion1==4:
        print("Gracias por usar nuestro sistema")
        print("Te esperamos pronto")
        print(":D")
        booleanito=False