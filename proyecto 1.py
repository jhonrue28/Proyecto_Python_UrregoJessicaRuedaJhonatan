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
        condcamper = True
        while condcamper:
            print("Bienvenido al menú de camper")
            print("¿Qué deseas ver?")
            print("1. Inscribirse al programa")
            print("2. Ya estoy inscrito")
            print("3. Salir del perfil de Camper")
            
            opcamper = int(input(": "))
            
            if opcamper == 1:
                with open("infoCampers.json", "r") as f: 
                    data = json.load(f)
                    infoCampers = data["campers"]
                
                nuevo = {
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
                        "trainer": 0,
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
                
                print("Bienvenido al registro")
                print("Recuerda que solo te debes registrar una vez")
                print("Presiona ENTER para iniciar")
                input("")
                
                nuevo["id"] = int(input("Digita tu número de documento: "))
                print("¿Cuál es tu nombre? (OJO: solo nombre, no apellidos)")
                nuevo["nombre"] = input(": ")
                print("Apellido")
                nuevo["apellidos"] = input(": ")
                print("Dirección")
                nuevo["direccion"] = input(": ")
                print("Acudiente")
                nuevo["contacto"]["acudiente"] = input(": ")
                print("Teléfono celular")
                nuevo["contacto"]["celular"] = input(": ")
                print("Teléfono fijo")
                nuevo["contacto"]["telefonoFijo"] = input(": ")
                
                infoCampers.append(nuevo)
                
                with open("infoCampers.json", "w") as f:
                    json.dump({"campers": infoCampers}, f, indent=4)
                
                print(" ")
                print("Ya quedaste registrado :D")
                print("Diste el primer paso, el más importante")
                print(" ")
            
            elif opcamper == 2:
                print("")
                print("Primero queremos reconocerte :P")
                nombreBuscar = input("Nombre con el que te registraste (solo nombre, no apellido): ").strip().lower()
                apellidoBuscar = input("¿Cuál es tu apellido? ").strip().lower()
                
                with open("infoCampers.json", "r") as f:
                    infoCampers = json.load(f)
                
                found = False
                for camper in infoCampers["campers"]:
                    if camper["nombre"].lower() == nombreBuscar and camper["apellidos"].lower() == apellidoBuscar:
                        found = True
                        booleanito2 = True
                        while booleanito2:
                            print(" ")
                            print("Bienvenido", camper["nombre"])
                            if camper["academico"]["estado"] == 0:
                                camper["academico"]["estado"] = "Postulado"
                            print("Tu estado actual es:", camper["academico"]["estado"])
                            print("¿Qué deseas hacer?")
                            print("1. ¿Cuál es mi ruta?")
                            print("2. ¿Cuáles son mis notas?")
                            print("3. Retirarse")
                            print("4. Volver al menú principal")
                            print(" ")
                            decision2 = int(input(": "))
                            
                            if decision2 == 1:
                                if camper["academico"]["ruta"] != 0:
                                    print("Tu ruta es:", camper["academico"]["ruta"])
                                    print("Tu salón es:", camper["academico"]["salon"])
                                    print("Tu trainer encargado es:", camper["academico"]["trainer"])
                                    print(" ")
                                else:
                                    print("Aún no te han asignado una ruta.")
                                    print(" ")
                            
                            elif decision2 == 2:
                                if camper["academico"]["modulos"]:
                                    print("Tus notas son:", camper["academico"]["modulos"])
                                else:
                                    print("Aún no tienes notas asignadas.")
                            
                            elif decision2 == 3:
                                print("¿Estás seguro de querer retirarte?")
                                print("1. Sí  2. No")
                                confirmacion = int(input(": "))
                                if confirmacion == 1:
                                    camper["academico"]["estado"] = "Retirado"
                                    with open("infoCampers.json", "w") as f:
                                        json.dump(infoCampers, f, indent=4)
                                    print("Esperamos te vaya super bien")
                                    print("Muchas gracias por haber estado acá")
                                    booleanito2 = False
                            
                            elif decision2 == 4:
                                print("Volviendo al menú principal...")
                                booleanito2 = False
                                break
                        
                if not found:
                    print(" ")
                    print("El nombre no está inscrito en el programa")
                    print(" ")
            
            elif opcamper == 3:
                print(" ")
                print("-_-")
                print("Te estaré vigilando")
                print("Vuelve pronto :D")
                condcamper = False
                print(" ")
               
    if opcion1==2:
        condMenuTrainer = True
        while condMenuTrainer:
            print("¿Cuál es tu nombre?")
            nombreTrainer = input(": ").strip().lower()
            with open("trainers.json", "r") as f:
                trainers = json.load(f)
                trainerEncontrado = None
                for trainer in trainers:
                    if trainer["nombre"].lower().strip() == nombreTrainer:
                        trainerEncontrado = trainer
                        break
                if not trainerEncontrado:
                    print("No se encontró ningún trainer con ese nombre.")
                    continue

            print("Bienvenido al menú de trainer")
            print("¿Qué deseas hacer?")
            print("1. Ver campers a cargo")
            print("2. Modificar información de campers a cargo")
            print("3. Volver al menú principal")
            decisionTrainer = int(input(": "))

            if decisionTrainer == 1:
                with open("infoCampers.json", "r") as f:
                    infoCampers = json.load(f)
                    print("\n--- LISTADO DE CAMPERS A CARGO ---")
                    campers_a_cargo = [
                        camper for camper in infoCampers["campers"]
                        if str(camper["academico"]["trainer"]).lower().strip() == trainerEncontrado["nombre"].lower().strip()
                    ]
                    if campers_a_cargo:
                        for camper in campers_a_cargo:
                            print(f"{camper['nombre']} {camper['apellidos']} - Ruta: {camper['academico']['ruta']} - Salón: {camper['academico']['salon']}")
                    else:
                        print("No tienes campers a cargo.")

            elif decisionTrainer == 2:
                with open("infoCampers.json", "r+") as f:
                    infoCampers = json.load(f)
                    campers_a_cargo = [
                        camper for camper in infoCampers["campers"]
                       if str(camper["academico"]["trainer"]).lower().strip() == trainerEncontrado["nombre"].lower().strip()
                    ]
                    if not campers_a_cargo:
                        print("No tienes campers a cargo para modificar.")
                        continue

                    print("¿Qué camper deseas modificar?")
                    for idx, camper in enumerate(campers_a_cargo, start=1):
                        print(f"{idx}. {camper['nombre']} {camper['apellidos']}")
                    seleccion = int(input("Seleccione el número del camper: "))
                    if 1 <= seleccion <= len(campers_a_cargo):
                        camper_seleccionado = campers_a_cargo[seleccion - 1]
                        print("¿Qué información deseas modificar?")
                        print("1. Notas")
                        opcion_modificacion = input("Seleccione: ")
                        if opcion_modificacion == "1":
                            print("Ingrese las nuevas notas del camper:")
                            teorica = float(input("Nota teórica: "))
                            practica = float(input("Nota práctica: "))
                            trabajos = float(input("Nota trabajos: "))
                            final = float(input("Nota final: "))
                            camper_seleccionado["academico"]["modulos"] = [{
                                "teorica": teorica,
                                "practica": practica,
                                "trabajos": trabajos,
                                "final": final
                            }]
                            with open("infoCampers.json", "w") as f:
                                json.dump(infoCampers, f, indent=4)
                            print("Información del camper actualizada con éxito.")
                        else:
                            print("Opción inválida.")
                    else:
                        print("Selección inválida.")

            elif decisionTrainer == 3:
                print("Volviendo al menú principal...")
                condMenuTrainer = False

            else:
                print("Opción inválida.")

    if opcion1 == 3:
        import json

        condCoordinador = True
        while condCoordinador:
            print("\n===== MENÚ COORDINADOR =====")
            print("Bienvenido al menú de Coordinador")
            print("Información de quién quieres modificar o leer?")
            print("1. Campers")
            print("2. Trainers")
            print("3. Salones")
            print("4. Rutas")
            print("5. Volver al menú principal")
            opcion = input("Seleccione: ")

            if opcion == "1":
                with open("infoCampers.json", "r") as f:
                    infoCampers = json.load(f)
                print("¿Por qué método vas a buscar?")
                print("1. Por número de documento / ID")
                print("2. Por nombre")
                metodoBusqueda = input("Seleccione: ")
                camperEncontrado = False
                if metodoBusqueda == "1":
                    documento = int(input("Ingrese el número de identificación del camper: "))
                    for camper in infoCampers["campers"]:
                        if camper["id"] == documento:
                            print("Camper encontrado:", camper["nombre"], camper["apellidos"])
                            print("Estado:", camper["academico"]["estado"])
                            camperEncontrado = camper
                            break
                    if not camperEncontrado:
                        print("No se encontró ningún camper con ese número de identificación.")
                elif metodoBusqueda == "2":
                    nombreBuscar = input("Ingrese el nombre del camper: ").strip().lower()
                    apellidoBuscar = input("Ingrese el apellido del camper: ").strip().lower()
                    for camper in infoCampers["campers"]:
                        if camper["nombre"].lower() == nombreBuscar and camper["apellidos"].lower() == apellidoBuscar:
                            print("Camper encontrado:", camper["nombre"], camper["apellidos"])
                            print("Estado:", camper["academico"]["estado"])
                            camperEncontrado = camper
                            break
                    if not camperEncontrado:
                        print("No se encontró ningún camper con ese nombre y apellido.")
                
                if camperEncontrado:
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
                        camperEncontrado["academico"]["estado"] = nuevo_estado
                        with open("infoCampers.json", "w") as f:
                            json.dump(infoCampers, f, indent=4)
                        print("Estado actualizado con éxito.")
                    elif opcion == "2":
                        nueva_ruta = input("Ingrese la nueva ruta del camper (Java, NodeJS, NetCore): ")
                        camperEncontrado["academico"]["ruta"] = nueva_ruta
                        with open("infoCampers.json", "w") as f:
                            json.dump(infoCampers, f, indent=4)
                        print("Ruta actualizada con éxito.")
                    elif opcion == "3":
                        nuevo_salon = input("Ingrese el nuevo salón del camper (Sputnik, Artemis, Apolo): ")
                        camperEncontrado["academico"]["salon"] = nuevo_salon
                        with open("infoCampers.json", "w") as f:
                            json.dump(infoCampers, f, indent=4)
                        print("Salón actualizado con éxito.")
                    elif opcion == "4":
                        nuevo_trainer = input("Ingrese el nuevo trainer encargado del camper: ")
                        camperEncontrado["academico"]["trainer"] = nuevo_trainer
                        with open("infoCampers.json", "w") as f:
                            json.dump(infoCampers, f, indent=4)
                        print("Trainer actualizado con éxito.")
                    elif opcion == "5":
                        print("Ingrese las nuevas notas del camper:")
                        teorica = float(input("Nota teórica: "))
                        practica = float(input("Nota práctica: "))
                        trabajos = float(input("Nota trabajos: "))
                        final = float(input("Nota final: "))
                        camperEncontrado["academico"]["modulos"] = [{
                            "teorica": teorica,
                            "practica": practica,
                            "trabajos": trabajos,
                            "final": final
                        }]
                        with open("infoCampers.json", "w") as f:
                            json.dump(infoCampers, f, indent=4)
                        print("Notas actualizadas con éxito.")
                    elif opcion == "6":
                        print("Volviendo al menú de coordinador...")

            elif opcion == "2":
                condTrainer = True
                while condTrainer:
                    print("\n===== MENÚ TRAINERS =====")
                    print("1. Crear un nuevo Trainer")
                    print("2. Ver Trainers")
                    print("3. Modificar información de un Trainer")
                    print("4. Eliminar un Trainer")
                    print("5. Volver al menú de coordinador")
                    decisionTrainer = input("Seleccione: ")

                    if decisionTrainer == "1":
                        nuevo_trainer = {
                            "nombre": input("Ingrese el nombre del nuevo Trainer: "),
                            "ruta": input("Ingrese las rutas que va a impartir el Trainer (separadas por comas): ").split(","),
                            "horario": input("Ingrese el horario del Trainer: ")
                        }
                        with open("trainers.json", "r+") as f:
                            trainers = json.load(f)
                            trainers.append(nuevo_trainer)
                            f.seek(0)
                            json.dump(trainers, f, indent=4)
                        print("Trainer creado con éxito.")
                    elif decisionTrainer == "2":
                        with open("trainers.json", "r") as f:
                            trainers = json.load(f)
                            print("\n--- LISTADO DE TRAINERS ---")
                            for i, trainer in enumerate(trainers, start=1):
                                print(f"{i}. {trainer['nombre']}")
                                print(f"   Rutas: {', '.join(trainer['ruta'])}")
                                print(f"   Horario: {trainer['horario']}")
                                print("-")
                    elif decisionTrainer == "3":
                        with open("trainers.json", "r+") as f:
                            trainers = json.load(f)
                            print("¿Qué trainer deseas modificar?")
                            for i, trainer in enumerate(trainers, start=1):
                                print(f"{i}. {trainer['nombre']}")
                            seleccion = int(input("Seleccione el número del trainer: "))
                            if 1 <= seleccion <= len(trainers):
                                trainer_seleccionado = trainers[seleccion - 1]
                                print("¿Qué información deseas modificar?")
                                print("1. Nombre")
                                print("2. Ruta")
                                print("3. Horario")
                                opcion_modificacion = input("Seleccione: ")
                                if opcion_modificacion == "1":
                                    trainer_seleccionado["nombre"] = input("Ingrese el nuevo nombre del trainer: ")
                                elif opcion_modificacion == "2":
                                    trainer_seleccionado["ruta"] = input("Ingrese las nuevas rutas del trainer (separadas por comas): ").split(",")
                                elif opcion_modificacion == "3":
                                    trainer_seleccionado["horario"] = input("Ingrese el nuevo horario del trainer: ")
                                f.seek(0)
                                json.dump(trainers, f, indent=4)
                                f.truncate()
                                print("Información del trainer actualizada con éxito.")
                            else:
                                print("Selección inválida.")
                    elif decisionTrainer == "4":
                        with open("trainers.json", "r+") as f:
                            trainers = json.load(f)
                            print("¿Qué trainer deseas eliminar?")
                            for i, trainer in enumerate(trainers, start=1):
                                print(f"{i}. {trainer['nombre']}")
                            seleccion = int(input("Seleccione el número del trainer: "))
                            if 1 <= seleccion <= len(trainers):
                                trainer_eliminado = trainers.pop(seleccion - 1)
                                f.seek(0)
                                json.dump(trainers, f, indent=4)
                                f.truncate()
                                print(f"Trainer {trainer_eliminado['nombre']} eliminado con éxito.")
                            else:
                                print("Selección inválida.")
                    elif decisionTrainer == "5":
                        print("Volviendo al menú de coordinador...")
                        condTrainer = False
                    else:
                        print("Opción inválida.")

            elif opcion == "3":
                condSalones = True
                while condSalones:
                    print("\n===== MENÚ SALONES =====")
                    print("1. Crear un nuevo salón")
                    print("2. Ver salones")
                    print("3. Modificar información de un salón")
                    print("4. Eliminar un salón")
                    print("5. Volver al menú de coordinador")
                    decisionSalones = input("Seleccione: ")

                    if decisionSalones == "1":
                        with open("salones.json", "r+") as f:
                            datos = json.load(f)
                            salones_dict = datos[0]["Salones"]
                            nombre = input("Ingrese el nombre del nuevo salón: ")
                            nuevo_salon = {
                                "horarios": [
                                    {
                                        "6:00-10:00": {"ruta": 0, "trainer": 0, "capacidad": 35, "integrantes": []},
                                        "10:00-14:00": {"ruta": 0, "trainer": 0, "capacidad": 35, "integrantes": []},
                                        "14:00-18:00": {"ruta": 0, "trainer": 0, "capacidad": 35, "integrantes": []},
                                        "18:00-22:00": {"ruta": 0, "trainer": 0, "capacidad": 35, "integrantes": []}
                                    }
                                ]
                            }
                            salones_dict[nombre] = nuevo_salon
                            f.seek(0)
                            json.dump(datos, f, indent=4)
                            f.truncate()
                        print(f"Salón {nombre} creado con éxito.")
                    elif decisionSalones == "2":
                        with open("salones.json", "r") as f:
                            datos = json.load(f)
                            salones_dict = datos[0]["Salones"]
                            print("\n--- LISTADO DE SALONES ---")
                            for i, (nombre_salon, info_salon) in enumerate(salones_dict.items(), start=1):
                                print(f"{i}. {nombre_salon}")
                                if info_salon.get("horarios"):
                                    print(f"   Horarios: {list(info_salon['horarios'][0].keys())}")
                    elif decisionSalones == "3":
                        with open("salones.json", "r+") as f:
                            datos = json.load(f)
                            salones_dict = datos[0]["Salones"]
                            print("¿Qué salón deseas modificar?")
                            salones_lista = list(salones_dict.keys())
                            for i, nombre_salon in enumerate(salones_lista, start=1):
                                print(f"{i}. {nombre_salon}")
                            seleccion = int(input("Seleccione el número del salón: "))
                            if 1 <= seleccion <= len(salones_lista):
                                nombre_antiguo = salones_lista[seleccion - 1]
                                nombre_nuevo = input("Ingrese el nuevo nombre del salón: ")
                                salones_dict[nombre_nuevo] = salones_dict.pop(nombre_antiguo)
                                f.seek(0)
                                json.dump(datos, f, indent=4)
                                f.truncate()
                                print("Información del salón actualizada con éxito.")
                            else:
                                print("Selección inválida.")
                    elif decisionSalones == "4":
                        with open("salones.json", "r+") as f:
                            datos = json.load(f)
                            salones_dict = datos[0]["Salones"]
                            print("¿Qué salón deseas eliminar?")
                            salones_lista = list(salones_dict.keys())
                            for i, nombre_salon in enumerate(salones_lista, start=1):
                                print(f"{i}. {nombre_salon}")
                            seleccion = int(input("Seleccione el número del salón: "))
                            if 1 <= seleccion <= len(salones_lista):
                                salon_eliminado = salones_lista[seleccion - 1]
                                del salones_dict[salon_eliminado]
                                f.seek(0)
                                json.dump(datos, f, indent=4)
                                f.truncate()
                                print(f"Salón {salon_eliminado} eliminado con éxito.")
                            else:
                                print("Selección inválida.")
                    elif decisionSalones == "5":
                        print("Volviendo al menú de coordinador...")
                        condSalones = False
                    else:
                        print("Opción inválida.")

            elif opcion == "4":
                condRutas = True
                while condRutas:
                    print("\n===== MENÚ RUTAS =====")
                    print("1. Crear una nueva ruta")
                    print("2. Ver rutas")
                    print("3. Modificar información de una ruta")
                    print("4. Eliminar una ruta")
                    print("5. Volver al menú de coordinador")
                    decisionRutas = input("Seleccione: ")

                    if decisionRutas == "1":
                        nueva_ruta = {
                            "nombre": input("Ingrese el nombre de la nueva ruta: "),
                            "descripcion": input("Ingrese una descripción de la ruta: "),
                            "duracion": input("Ingrese la duración de la ruta (en semanas): ")
                        }
                        with open("rutas.json", "r+") as f:
                            rutas = json.load(f)
                            rutas.append(nueva_ruta)
                            f.seek(0)
                            json.dump(rutas, f, indent=4)
                            f.truncate()
                        print("Ruta creada con éxito.")
                    elif decisionRutas == "2":
                        with open("rutas.json", "r") as f:
                            rutas = json.load(f)
                            print("\n--- LISTADO DE RUTAS ---")
                            for i, ruta in enumerate(rutas, start=1):
                                print(f"{i}. {ruta['nombre']}")
                                print(f"   Descripción: {ruta['descripcion']}")
                                print(f"   Duración: {ruta['duracion']} semanas")
                                print("-")
                    elif decisionRutas == "3":
                        with open("rutas.json", "r+") as f:
                            rutas = json.load(f)
                            print("¿Qué ruta deseas modificar?")
                            for i, ruta in enumerate(rutas, start=1):
                                print(f"{i}. {ruta['nombre']}")
                            seleccion = int(input("Seleccione el número de la ruta: "))
                            if 1 <= seleccion <= len(rutas):
                                ruta_seleccionada = rutas[seleccion - 1]
                                ruta_seleccionada["nombre"] = input("Ingrese el nuevo nombre de la ruta: ")
                                ruta_seleccionada["descripcion"] = input("Ingrese la nueva descripción de la ruta: ")
                                ruta_seleccionada["duracion"] = input("Ingrese la nueva duración de la ruta (en semanas): ")
                                f.seek(0)
                                json.dump(rutas, f, indent=4)
                                f.truncate()
                                print("Información de la ruta actualizada con éxito.")
                            else:
                                print("Selección inválida.")
                    elif decisionRutas == "4":
                        with open("rutas.json", "r+") as f:
                            rutas = json.load(f)
                            print("¿Qué ruta deseas eliminar?")
                            for i, ruta in enumerate(rutas, start=1):
                                print(f"{i}. {ruta['nombre']}")
                            seleccion = int(input("Seleccione el número de la ruta: "))
                            if 1 <= seleccion <= len(rutas):
                                ruta_eliminada = rutas.pop(seleccion - 1)
                                f.seek(0)
                                json.dump(rutas, f, indent=4)
                                f.truncate()
                                print(f"Ruta {ruta_eliminada['nombre']} eliminada con éxito.")
                            else:
                                print("Selección inválida.")
                    elif decisionRutas == "5":
                        print("Volviendo al menú de coordinador...")
                        condRutas = False
                    else:
                        print("Opción inválida.")

            elif opcion == "5":
                print("GRACIAS POR USAR NUESTRO SISTEMA")
                print("Estás saliendo del menú de coordinador")
                condCoordinador = False
            else:
                print("Opción inválida.")
    if opcion1==4:
        print("Gracias por usar nuestro sistema")
        print("Te esperamos pronto")
        print(":D")
        booleanito=False