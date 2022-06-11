def validez_precio_unitario (precio_u):

    min = float (10)
    max = float (1000)

    return precio_u > min and precio_u <= max #evaluo que el precio pasado sea entre el rango definido
 
      
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def cantidad_valida (cantidad):
    return cantidad >0 and cantidad < 11
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def validar_dni (dni):

    return dni > 5*(10**6) and dni < 99*(10**6)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def validar_email (email): 
    
    
    if len(email) > 10 and arroba (email) == True and punto (email) == True and espacio (email) == True:

        retorno_email = True

    else:

        retorno_email = False

    return retorno_email

def arroba (email): 

    retorno_arroba = True  
    contador_arroba = 0
    _arroba = "@" 
    for caracter in email: 
        
        if caracter == _arroba: 
            contador_arroba += 1
    

    if email[0] == _arroba or email [-1] == _arroba or contador_arroba > 1:

        retorno_arroba = False
    

    return retorno_arroba 

def punto (email):
    retorno_punto = False
    _puntos = 0
    _punto = "."
    

    for caracter in email:
        
        if caracter == _punto:

            _puntos += 1

    if  email[0] == _punto or email [-1] == _punto:

        retorno_punto = False

    elif _puntos >= 1:

        retorno_punto = True
    
    return retorno_punto

def espacio (email):

    retorno_espacio = True
    contador_espacio = 0
    _espacio = " "
    for caracter in email:
        
        if caracter == _espacio: 

            contador_espacio += 1

    if contador_espacio > 0:

        retorno_espacio = False

    return retorno_espacio

def validar_fecha (dia,mes,anio):
    
    ret = False

    if mes % 2 != 0 and (dia == 15 or dia == 31) and anio in range (2022,9999):

        ret = True

    elif mes % 2 == 0 and (dia == 15 or dia == 30) and anio in range (2022,9999):

        ret = True

    elif mes == 2 and(dia == 15 or dia == 28) and anio in range (2022,9999):

        ret = True

    elif mes == 2 and anio % 4 == 0 and anio % 100 != 0 and (dia == 15 or dia == 29)and anio in range (2022,9999):

        ret = True

    return ret


 #inventario = (("A","a","Yerba mate", 300),("B", "b";"Te negro", 100), ("C", "C","Te verde", 125), ("D", "d","Miel tipo mistol", 200), ("E", "e","Miel de algarrobo", 225))