import json

def lecturaInfocampers():
    with open('./infoCampers.json', "r") as f:
        infoCampers = json.load(f)
        return infoCampers

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
                    nuevo["contacto"]["celular"]=input(": ")
                    print("telefono fijo")
                    nuevo["contacto"]["telefonoFijo"]=input(": ")
                    
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
        condMenuTrainer=True
        while condMenuTrainer==True:
            print ("Cual es tu nombre?")
            nombreTrainer=input(": ")
            with open("trainers.json", "r") as f:
                trainers = json.load(f)
                trainer_encontrado = False
                for i in trainers:
                    if trainers[i]["nombre"].lower().strip() == nombreTrainer.lower().strip():
                        trainerEncontrado = True
                if not trainerEncontrado:
                    print("No se encontró ningún trainer con ese nombre.")
                    continue
                if trainerEncontrado==True:
                    print("Bienvenido al menú de trainer")
                    print("¿Qué deseas hacer?")
                    print("1.Ver campers a cargo")
                    print("2.Modificar información de campers a cargo")
                    print("3.Volver al menú principal")
                    decisionTrainer=int(input(": "))
                    if decisionTrainer==1:
                        with open("infoCampers.json", "r") as f:
                            infoCampers = json.load(f)
                            print("\n--- LISTADO DE CAMPERS A CARGO ---")
                            for i in range(len(infoCampers["campers"])):
                                if infoCampers["campers"][i]["academico"]["trainer"] == trainers[i]["nombre"]:
                                    print(f"{infoCampers['campers'][i]['nombre']} {infoCampers['campers'][i]['apellidos']} - Ruta: {infoCampers['campers'][i]['academico']['ruta']} - Salón: {infoCampers['campers'][i]['academico']['salon']}")
                    if decisionTrainer==2:
                        with open("infoCampers.json", "r+") as f:
                            infoCampers = json.load(f)
                            print("¿Qué camper deseas modificar?")
                            for i in range(len(infoCampers["campers"])):
                                if infoCampers["campers"][i]["academico"]["trainer"] == trainers[i]["nombre"]:
                                    print(f"{i+1}. {infoCampers['campers'][i]['nombre']} {infoCampers['campers'][i]['apellidos']}")
                            seleccion = int(input("Seleccione el número del camper: "))
                            if 1 <= seleccion <= len(infoCampers["campers"]):
                                camper_seleccionado = infoCampers["campers"][seleccion - 1]
                                print("¿Qué información deseas modificar?")
                                print("1. Notas")
                                opcion_modificacion = input("Seleccione: ")
                                if opcion_modificacion == "1":
                                    print("Ingrese las nuevas notas del camper:")
                                    teorica = float(input("Nota teórica: "))
                                    practica = float(input("Nota práctica: "))
                                    trabajos = float(input("Nota trabajos: "))
                                    final = float(input("Nota final: "))
                                    camper_seleccionado["academico"]["modulos"] = {
                                        "teorica": teorica,
                                        "practica": practica,
                                        "trabajos": trabajos,
                                        "final": final
                                    }
                                with open("infoCampers.json", "w") as f:
                                    json.dump(infoCampers, f, indent=4)
                                print("Información del camper actualizada con éxito.")       
                            else:
                                print("Selección inválida.")
                    if decisionTrainer==3:
                        print("Volviendo al menú principal...")
                        print(" ")
                        condMenuTrainer=False

    if opcion1 == 3:
            condCoordinador = True
            while condCoordinador == True:
                print("\n===== MENÚ COORDINADOR =====")
                print ("Bienvenido al menú de Coordinador")
                print("Información de quien quieres modificar o leer?")
                print("1. Campers")
                print("2. Trainers")
                print("3. Salones")
                print("4. Rutas")
                print("5. Volver al menú principal")
                opcion = input("Seleccione: ")

                if opcion == "1":
                    with open("infoCampers.json", "r") as f:
                        infoCampers = json.load(f)
                        print("Por qué metodo vas a buscar?")
                        print("1. Por número de documento / ID")
                        print("2. Por nombre")
                        metodoBusqeda = input("Seleccione: ")
                        if metodoBusqeda == "1":
                            documento = input("Ingrese el número de identificación del camper: ")
                            for i in range(len(infoCampers["campers"])):
                                if infoCampers["campers"][i]["id"] == documento:
                                    print ("Camper encontrado:",infoCampers["campers"][i]["nombre"], infoCampers["campers"][i]["apellidos"])
                                    print("Estado:", infoCampers["campers"][i]["academico"]["estado"])
                                    camperEncontrado=0
                            else:
                                print("No se encontró ningún camper con ese número de identificación.") 
                        elif metodoBusqeda == "2":
                            nombreBuscar = input("Ingrese el nombre del camper: ")
                            apellidoBuscar = input("Ingrese el apellido del camper: ")
                            for i in range(len(infoCampers["campers"])):
                                if infoCampers["campers"][i]["nombre"].lower().strip() == nombreBuscar.lower().strip() and infoCampers["campers"][i]["apellidos"].lower().strip() == apellidoBuscar.lower().strip():
                                    print ("Camper encontrado:",infoCampers["campers"][i]["nombre"], infoCampers["campers"][i]["apellidos"])
                                    print("Estado:", infoCampers["campers"][i]["academico"]["estado"])
                                    camperEncontrado=0
                            else:
                                print("No se encontró ningún camper con ese nombre y apellido.")
                            
                            if camperEncontrado == 0:
                                print("¿Qué deseas hacer con este camper?")
                                print("1. Modificar estado")
                                print("2. Modificar ruta")
                                print("3. Modificar salón")
                                print("4. Modificar trainer")
                                print("5. Modificar notas")
                                print("6. Volver al menú de coordinador")
                                opcion = input("Seleccione: ")

                                if opcion == "1":
                                    nuevo_estado = input("Ingrese el nuevo estado del camper (Postulado, Aprobado, Cursando, Retirado): ")
                                    infoCampers["campers"][i]["academico"]["estado"] = nuevo_estado
                                    with open("infoCampers.json", "w") as f:
                                        json.dump(infoCampers, f, indent=4)
                                    print("Estado actualizado con éxito.")
                                if opcion == "2":
                                    nueva_ruta = input("Ingrese la nueva ruta del camper Java, NodeJS, NetCore: ")
                                    infoCampers["campers"][i]["academico"]["ruta"] = nueva_ruta
                                    with open("infoCampers.json", "w") as f:
                                        json.dump(infoCampers, f, indent=4)
                                    print("Ruta actualizada con éxito.")
                                if opcion == "3":
                                    nuevo_salon = input("Ingrese el nuevo salón del camper Sputnik, Artemis, Apolo: ")
                                    infoCampers["campers"][i]["academico"]["salon"] = nuevo_salon
                                    with open("infoCampers.json", "w") as f:
                                        json.dump(infoCampers, f, indent=4)
                                    print("Salón actualizado con éxito.")
                                if opcion == "4":
                                    nuevo_trainer = input("Ingrese el nuevo trainer encargado del camper: ")
                                    infoCampers["campers"][i]["academico"]["trainer"] = nuevo_trainer
                                    with open("infoCampers.json", "w") as f:
                                        json.dump(infoCampers, f, indent=4)
                                    print("Trainer actualizado con éxito.")
                                if opcion == "5":
                                    print("Ingrese las nuevas notas del camper:")
                                    teorica = float(input("Nota teórica: "))
                                    practica = float(input("Nota práctica: "))
                                    trabajos = float(input("Nota trabajos: "))
                                    final = float(input("Nota final: "))
                                    infoCampers["campers"][i]["academico"]["modulos"] = {
                                        "teorica": teorica,
                                        "practica": practica,
                                        "trabajos": trabajos,
                                        "final": final
                                    }
                                    with open("infoCampers.json", "w") as f:
                                        json.dump(infoCampers, f, indent=4)
                                    print("Notas actualizadas con éxito.")
                                if opcion == "6":
                                    print("Volviendo al menú de coordinador...")
                                    camperEncontrado = 1
                elif opcion == "2":
                    condTrainer = True
                    while condTrainer == True:
                        print("Bienvenido al menú de Trainers")
                        print("1.Crear un nuevo Trainer")
                        print("2.Ver Trainers")
                        print("3.Modificar información de un Trainer")
                        print("4.Eliminar un Trainer")
                        print("5.Asignar salones a un Trainer")
                        print("6.Volver al menú de coordinador")
                        decisionTrainer = input("Seleccione: ")
                        if decisionTrainer == "1":
                            nueco_trainer = {
                                "nombre": "",
                                "ruta": "",
                                "horario": ""
                            }
                            print("Ingrese el nombre del nuevo Trainer:")
                            nueco_trainer["nombre"] = input(": ")
                            print("Ingrese la ruta que va a impartir el Trainer Java, NodeJS, NetCore:")
                            nueco_trainer["ruta"] = input(": ")
                            print("Ingrese el horario del Trainer:")
                            nueco_trainer["horario"] = input(": ")
                            with open("trainers.json", "r+") as f:
                                trainers = json.load(f)
                                trainers.append(nueco_trainer)
                                json.dump(trainers, f, indent=4)
                        if decisionTrainer == "2":
                            with open("trainers.json", "r") as f:
                                trainers = json.load(f)
                                print("\n--- LISTa DE TRAINERS ---")
                                with open("trainers.json", "r") as f:
                                    trainers = json.load(f)
                                    for i in range(len(trainers)):
                                        print(f"{i+1}. {trainers[i]['nombre']}")
                                        print(f"   Rutas: {trainers[i]['ruta']}")
                                        print(f"   Horario: {trainers[i]['horario']}")
                                        print("-" )
                        if decisionTrainer == "3":
                            with open ("trainer.json", "r") as f:
                                trainers = json.load(f)
                                print("¿Qué trainer deseas modificar?")
                                for i in range(len(trainers)):
                                    print(f"{i+1}. {trainers[i]['nombre']}")
                                seleccion = int(input("Seleccione el número del trainer: "))
                                if 1 <= seleccion <= len(trainers):
                                    trainer_seleccionado = trainers[seleccion - 1]
                                    print("¿Qué información deseas modificar?")
                                    print("1. Nombre")
                                    print("2. Ruta")
                                    print("3. Horario")
                                    opcion_modificacion = input("Seleccione: ")
                                    if opcion_modificacion == "1":
                                        nuevo_nombre = input("Ingrese el nuevo nombre del trainer: ")
                                        trainer_seleccionado["nombre"] = nuevo_nombre
                                    elif opcion_modificacion == "2":
                                        nueva_ruta = input("Ingrese la nueva ruta del trainer Java, NodeJS, NetCore: ")
                                        trainer_seleccionado["ruta"] = nueva_ruta
                                    elif opcion_modificacion == "3":
                                        nuevo_horario = input("Ingrese el nuevo horario del trainer: ")
                                        trainer_seleccionado["horario"] = nuevo_horario
                                    with open("trainers.json", "w") as f:
                                        json.dump(trainers, f, indent=4)
                                    print("Información del trainer actualizada con éxito.")
                                else:
                                    print("Selección inválida.")
                        if decisionTrainer == "4":
                            with open("trainers.json", "r") as f:
                                trainers = json.load(f)
                                print("¿Qué trainer deseas eliminar?")
                                for i in range(len(trainers)):
                                    print(f"{i+1}. {trainers[i]['nombre']}")
                                seleccion = int(input("Seleccione el número del trainer: "))
                                if 1 <= seleccion <= len(trainers):
                                    trainer_eliminado = trainers.pop(seleccion - 1)
                                    with open("trainers.json", "w") as f:
                                        json.dump(trainers, f, indent=4)
                                    print(f"Trainer {trainer_eliminado['nombre']} eliminado con éxito.")
                                else:
                                    print("Selección inválida.")
                        if decisionTrainer == "5":
                            with open("trainers.json", "r") as f:
                                trainers = json.load(f)
                                print("¿A qué trainer deseas asignar un salón?")
                                for i in range(len(trainers)):
                                    print(f"{i+1}. {trainers[i]['nombre']}")
                                seleccion = int(input("Seleccione el número del trainer: "))
                                if 1 <= seleccion <= len(trainers):
                                    trainer_seleccionado = trainers[seleccion - 1]
                                    nuevo_salon = input("Ingrese el nuevo salón para el trainer Sputnik, Artemis, Apolo: ")
                                    trainer_seleccionado["salon"] = nuevo_salon
                                    json.dump(trainers, f, indent=4)
                                    print("Salón asignado al trainer con éxito.")
                                else:
                                    print("Selección inválida.")
                        if decisionTrainer == "6":
                            print("Volviendo al menú de coordinador...")
                            print(" ")
                            condtrainer = False
                elif opcion == "3":
                    condSalones = True
                    while condSalones == True:
                        print("menú salones")
                        print("1.Crear un nuevo salón")
                        print("2.Ver salones")
                        print("3.Modificar información de un salón")
                        print("4.Eliminar un salón")
                        print("5.Volver al menú de coordinador")
                        decisionSalones = input("Seleccione: ")
                        if decisionSalones == "1":  
                            with open("salones.json ", "r+") as f:  
                                salones = json.load(f)
                                nombre = input("Nombre del nuevo salón: ")
                                nuevo_salon = {"nombre": nombre, "capacidad": 35}
                                salones.append(nuevo_salon)
                                print(f"Salón {nombre} creado con éxito.")
                                json.dump(salones, f, indent=4)
                        if decisionSalones == "2":
                            with open("salones.json", "r") as f:
                                salones = json.load(f)
                                print("\n--- LISTADO DE SALONES ---")
                                for i in range(len(salones)):
                                    print(f"{i+1}. {salones[i]['nombre']} - Capacidad: {salones[i]['capacidad']}")
                        if decisionSalones == "3":
                            with open("salones.json", "r+") as f:
                                salones = json.load(f)
                                print("¿Qué salón deseas modificar?")
                                for i in range(len(salones)):
                                    print(f"{i+1}. {salones[i]['nombre']}")
                                seleccion = int(input("Seleccione el número del salón: "))
                                if 1 <= seleccion <= len(salones):
                                    salon_seleccionado = salones[seleccion - 1]
                                    nuevo_nombre = input("Ingrese el nuevo nombre del salón: ")
                                    salon_seleccionado["nombre"] = nuevo_nombre
                                    with open("salones.json", "w") as f:
                                        json.dump(salones, f, indent=4)
                                    print("Información del salón actualizada con éxito.")
                                else:
                                    print("Selección inválida.")
                        if decisionSalones == "4":
                            with open("salones.json", "r") as f: 
                                salones = json.load(f)
                                print("¿Qué salón deseas eliminar?")
                                for i in range(len(salones)):
                                    print(f"{i+1}. {salones[i]['nombre']}")
                                seleccion = int(input("Seleccione el número del salón: "))
                                if 1 <= seleccion <= len(salones):
                                    salon_eliminado = salones.pop(seleccion - 1)
                                    with open("salones.json", "w") as f:
                                        json.dump(salones, f, indent=4)
                                    print(f"Salón {salon_eliminado['nombre']} eliminado con éxito.")
                                else:
                                    print("Selección inválida.")
                        if decisionSalones == "5":
                            print("Volviendo al menú de coordinador")
                            print(" ")
                            condSalones = False
                elif opcion == "4":
                    condRutas = True
                    while condRutas == True:
                        print("Bienvenido al menú de rutas")
                        print("1.Crear una nueva ruta")
                        print("2.Ver rutas")
                        print("3.Modificar información de una ruta")
                        print("4.Eliminar una ruta")
                        print("5.Volver al menú de coordinador")
                        decisionRutas = input("Seleccione: ")
                        if decisionRutas == "1":
                            nueva_ruta = {
                                "nombre": "",
                                "descripcion": "",
                                "duracion": ""
                            }
                            print("Ingrese el nombre de la nueva ruta:")
                            nueva_ruta["nombre"] = input(": ")
                            print("Ingrese una descripción de la ruta:")
                            nueva_ruta["descripcion"] = input(": ")
                            print("Ingrese la duración de la ruta (en semanas):")
                            nueva_ruta["duracion"] = input(": ")
                            with open("rutas.json", "r+") as f:
                                rutas = json.load(f)
                                rutas.append(nueva_ruta)
                                json.dump(rutas, f, indent=4)
                        if decisionRutas == "2":
                            with open("rutas.json", "r") as f:
                                rutas = json.load(f)
                                print("\n--- LISTADO DE RUTAS ---")
                                for i in range(len(rutas)):
                                    print(f"{i+1}. {rutas[i]['nombre']}")
                                    print(f"   Descripción: {rutas[i]['descripcion']}")
                                    print(f"   Duración: {rutas[i]['duracion']} semanas")
                                    print("-" )
                        if decisionRutas == "3":
                            with open("rutas.json", "r+") as f:
                                rutas = json.load(f)
                                print("¿Qué ruta deseas modificar?")
                                for i in range(len(rutas)):
                                    print(f"{i+1}. {rutas[i]['nombre']}")
                                seleccion = int(input("Seleccione el número de la ruta: "))
                                if 1 <= seleccion <= len(rutas):
                                    ruta_seleccionada = rutas[seleccion - 1]
                                    nuevo_nombre = input("Ingrese el nuevo nombre de la ruta: ")
                                    nueva_descripcion = input("Ingrese la nueva descripción de la ruta: ")
                                    nueva_duracion = input("Ingrese la nueva duración de la ruta (en semanas): ")
                                    ruta_seleccionada["nombre"] = nuevo_nombre
                                    ruta_seleccionada["descripcion"] = nueva_descripcion
                                    ruta_seleccionada["duracion"] = nueva_duracion
                                    with open("rutas.json", "w") as f:
                                        json.dump(rutas, f, indent=4)
                                    print("Información de la ruta actualizada con éxito.")
                                else:
                                    print("Selección inválida.")
                        if decisionRutas == "4":
                            with open("rutas.json", "r") as f:
                                rutas = json.load(f)
                                print("¿Qué ruta deseas eliminar?")
                                for i in range(len(rutas)):
                                    print(f"{i+1}. {rutas[i]['nombre']}")
                                seleccion = int(input("Seleccione el número de la ruta: "))
                                if 1 <= seleccion <= len(rutas):
                                    ruta_eliminada = rutas.pop(seleccion - 1)
                                    with open("rutas.json", "w") as f:
                                        json.dump(rutas, f, indent=4)
                                    print(f"Ruta {ruta_eliminada['nombre']} eliminada con éxito.")
                                else:
                                    print("Selección inválida.")
                        if decisionSalones == "5":
                            print("Volviendo al menú de coordinador")
                            print(" ")
                            condRutas = False
                elif opcion == "5":
                    print("GRACIAS POR USAR NUESTRO SISTEMA")
                    print("Estás saliendo del menú de coordinador")
                    print(" :D")
                    print(" ")
                    condCoordinador = False
                else:
                    print("Opción inválida")
    
    if opcion1==4:
        print("Gracias por usar nuestro sistema")
        print("Te esperamos pronto")
        print(":D")
        booleanito=False