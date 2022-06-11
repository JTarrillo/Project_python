from pickle import FALSE
import funciones_TPGI
import os

def main ():
    print ("--------------") #Simil menu para recorrer las distintas opciones que brinda el programa
    print ("1 -ingreso de datos- ")
    print ("2 -mostrar datos-")
    print ("3 -mayores y menores datos-")
    print ("4 salir")
    print ("--------------")

    entrada = int (input ("Seleccione una de las opciones: ")) #Seleccionar una opccion
    
    lista_datos = [] # Lista con los datos de los socios
    _todo = 0 #Contador que almacena quienes llevaron los 5 tipos de productos
    
    while entrada != 4:

        if entrada == 1:
            print ("Ingrese los datos acorde a la entrega: ")
            ing_datos = input ()
            while ing_datos != 2: 

                llevaron_todo =  0 #Inicio un contador dos veces para reiniciarlo cuando pase por aca 

                fecha = False # Metodo de banderitas para validar los datos siguientes
                dni = False 
                email = False
                   
                while  fecha != True:  
                    dia = 0
                    mes = 0
                    anio = 0
                    dia = int(input ("Ingrese el dia:"))
                    mes = int(input ("Ingrese el mes:"))
                    anio = int(input ("Ingrese el año:"))

                    fecha = funciones_TPGI.validar_fecha (dia,mes, anio) #Definos distintas funciones que devuelven un booleano por si los datos validan o no
                    if fecha != True: 
                        print ("Dato incorrecto, vuelva a ingresar")
                        input ()
                    os.system ("cls")
                
                print ("Fecha validada")
                input ("Presiona ENTER para continuar")
                os.system ("cls")
                while dni != True:
                    dni = 0
                    _dni = int (input ("Ingrese su DNI (sin puntos ni comas):"))

                    dni = funciones_TPGI.validar_dni (_dni) #Definos distintas funciones que devuelven un booleano por si los datos validan o no

                    if dni != True: 
                        print ("Dato incorrecto, vuelva a ingresar")
                        input ()
                    os.system ("cls")
                
                print ("DNI validado")
                input ("Presiona ENTER para continuar")
                os.system ("cls")

                while email != True:
                    _email = ""
                    _email = input ("Ingrese Email:")

                    email = funciones_TPGI.validar_email (_email) #Definos distintas funciones que devuelven un booleano por si los datos validan o no
                    if email != True:
                        print ("Dato incorrecto, vuelva a ingresar")
                        input ()
                    os.system ("cls")

                print ("Email validado")
                input ("Presiona ENTER para continuar")
                os.system ("cls")
            

                

                print ("Todos los datos han sido validados")
                input ("Presiona ENTER para continuar")
                
                 
            
                os.system ("cls")
                print ("--------------")

                print ("Datos:") #Muestro los previamente validados por pantalla
                print ("Fecha: ",dia,"/",mes,"/",anio)
                print ("DNI: ", _dni)
                print ("Email: ", _email) 
                _fecha = [dia, mes, anio]
                print ("--------------")

                input ("Presiona ENTER para continuar")

                os.system ("cls")
                
                print ("--------------")

                print ("Productos: ") # Una vez validado todos los datos pasamos a la seleccion de productos del socio

                print ("-Yerba mate 1 Kg (1)\n-Té negro en hebras 100 grs(2)\n-Té verde en hebras 100 grs(3)\n-Miel tipo\
                mistol 1/2 Kg(4)\n-Miel tipo algarrobo 1 Kg(5))") #Lista de productos

                print ("--------------")

                ingreso_productos = int(input ("Selecciones su producto: (presione 6 para salir)")) # Ingreso el tipo de productos que quiere llevar

                total_monto = 0 # Acumulador de dinero
                usados = () # En esta lista voy metiendo los prodcutos seleccionados para que en el siguiente ciclo no sea posible utilizarlos
                llevaron_todo = 0 #Segunda variable para cuando llevan todo

                while ingreso_productos != 6 and llevaron_todo != 5: # Se ejecuta el ciclo while mientras el usuario no quiera salir y no haya seleccionado los 5 tipos de productos
                    
                    inventario = (1 , 2, 3, 4, 5)  #Tupla con los numeros de inventario
                
                    for producto in inventario: #Recorro el inventario para ver si el ingreso_productos esta dentro del inventario
                        
                        if (ingreso_productos == producto): #Si el producto esta dentro del inventario...

                            ingreso = (ingreso_productos,) 

                            llevaron_todo += 1 #voy contando cada vez que selecciona un producto y si llega a 5 para el ciclo y tira un mensaje
                            precio_u = float (input ("ingrese el precio unitario del producto: ")) #precio unitario

                            while funciones_TPGI.validez_precio_unitario(precio_u) != True: #se ejecuta el ciclo hasta que se valida el precio unitario
                                print ("Vuelva a introducir el precio unitario.")
                                input ()
                                
                                os.system ("cls") #limpia la pantalla
                                precio_u = float (input ("ingrese el precio unitario del producto: "))
                            
                            cantidad = float (input ("Ingrese la cantidad:")) # Selecciono la cantidad

                            while funciones_TPGI.cantidad_valida (cantidad) != True: # se ejecuta el ciclo hasta que se valida la cantidad
                                print ("Vuelva a introducir la cantidad.")
                                input ()

                                os.system ("cls")
                                cantidad = float (input ("Ingrese la cantidad de:"))

                            total_monto += precio_u * cantidad # Voy acumulando el producto del precio unitario y la cantidad
                            usados += ingreso # Voy metiendo dentro de la tupla los numeros ingresados para que luego no pueda repetirlos

                            os.system ("cls")
            
                    

                    while ingreso_productos in usados: # Se ejecuta el ciclo mientras el valor que yo ingrese siga dentro de la tupla con los valores usados
                        print ("--------------")
                        print ("Productos: ")
                        print ("-Yerba mate 1 Kg (1)\n-Té negro en hebras 100 grs(2)\n-Té verde en hebras 100 grs(3)\n-Miel tipo\
                        mistol 1/2 Kg(4)\n-Miel tipo algarrobo 1 Kg(5))")
                        print ("--------------")
                            
                        ingreso_productos = int(input ("Selecciones su producto:(presione 6 para salir)"))

                        if ingreso_productos in usados:
                            
                            print ("El valor ingresado es correcto, ingrese otro") # Mensaje para indicar que el valor ingresado esta dentro de la tupla de usados
                            input()
                            os.system("cls")

                    if llevaron_todo == 5: # Si ya llevaron todos los productos te va a tirar el siguiente mensaje 

                        print ("No hay mas productos por seleccionar para este socio.")   
                        print ("Presione ENTER para continuar.")    
                        input ()
                        os.system ("cls")  
                        _todo += 1

                
                lista_socios = [_dni,_email,_fecha, total_monto, _todo ] # mMeto en una lista todos los datos que saque de esta vuelta 

                lista_datos.append (lista_socios) #Meto en una lista global la lista de socios

                print ("¿Quiere ingresar otro socio?\n - 1 (Si)\n - 2 (No)") # Le pregunto al usuario si quiere ingresar otro socio o si quiere volver al menu principal

                ing_datos = int(input ("")) # Es simplemente algo decorativo para responder a lo de arriba 

                os.system ("cls")

        print ("--------------")
        print ("1 -ingreso de datos- ")
        print ("2 -mostrar datos-")
        print ("3 -mayores y menores datos-")
        print ("4 salir")
        print ("--------------")

        entrada = int (input ("Seleccione una de las opciones: ")) # Me remito al ciclo principal y selecciono de nuevo lo que quiero hacer

main ()



