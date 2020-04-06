import time, os
def resolfast():
    print("                            ____                      __ ____              __                ____     ___ ")
    print("                           / __ \ ___   _____ ____   / // __/____ _ _____ / /_     _   __   / __ \   |__ \"")
    print("                          / /_/ // _ \ / ___// __ \ / // /_ / __ `// ___// __/    | | / /  / / / /   __/ /")
    print("                         / _, _//  __/(__  )/ /_/ // // __// /_/ /(__  )/ /_      | |/ /_ / /_/ /_  / __/ ")
    print("                        /_/ |_| \___//____/ \____//_//_/   \__,_//____/ \__/      |___/(_)\____/(_)/____/ ")


    print("                        	    __                      _     __      __          ____          ")
    print("                        	   / /_  __  ______ ___  __(_)___/ /___  / /_  ____ _/ / /__  __  __")
    print("                        	  / __ \/ / / / __ `/ / / / / __  / __ \/ __ \/ __ `/ / / _ \/ / / /")
    print("                        	 / /_/ / /_/ / /_/ / /_/ / / /_/ / /_/ / / / / /_/ / / /  __/ /_/ / ")
    print("                        	/_.___/\__, /\__, /\__,_/_/\__,_/\____/_/ /_/\__,_/_/_/\___/\__, /  ")
    print("                        	      /____//____/                                         /____/   ")
    pass

def datos_expte():
    print ("***********************DATOS DEL EXPEDIENTE**************************")
    NdeExpediente=input("Numero de expediente (sin el año): ")
    AnioExpediente=input("Año del expediente: ")
    nuevoexp=NdeExpediente+"/"+AnioExpediente
    Comisarioa=input("Ingrese el Nombre Completo de la Comisaria: ")
    return nuevoexpte
    DomicilioDenunciante

def denunciante():
    while cerrarWhile==0:
        print ("*****************************************DATOS DEL DENUNCIANTE**************************************")    
        NombreDenunciante=input("Nombre completo del denunciante: ")
        NombreDenunciante=NombreDenunciante.upper()
    while True:
        SexoDenunciante = input("Sexo del/la denunciante (0=Masculino, 1=Femenino): ")
        if SexoDenunciante != "1" and SexoDenunciante != "0":
            print ("Respuesta incorrecta, vuelva a ingresar...")
        break    
    while True:
        Dnidenunciante = input("D.N.I del denunciante (Eje: xx.xxx.xxx ) Ingrese 0 para DESCONOCIDO: ")
        if Dnidenunciante=="0":
            Dnidenunciante = "DESCONOCIDO"
            break
        else:
            if len(Dnidenunciante)<9 or len(Dnidenunciante)>10:
                print ("Cantidad incorecta de caracteres: ")
                break
       
        DomicilioDenunciante = input("Domicilio del denunciante (Ingrese 0 para DESCONOCIDO): ")
        DomicilioDenunciante=DomicilioDenunciante.upper()
        NumeroDeTelefonoDenunciante = input("N° de telefono del denunciante (Ingrese 0 para DESCONOCIDO): ")
        VinculoConElDenunciado = input("Vinculo con el denunciado: ")
        VinculoConElDenunciado=VinculoConElDenunciado.upper()
        if DomicilioDenunciante=="0":
            DomicilioDenunciante= "DESCONOCIDO"
        if NumeroDeTelefonoDenunciante == "0" :
            NumeroDeTelefonoDenunciante = "DESCONOCIDO"
        if SexoDenunciante == "0" :
            sexo = "el Sr."
        if SexoDenunciante == "1" :
            sexo = "la Sra."      
        os.system ("cls")    
        if SexoDenunciante == "1":
            print ("Sexo del/la denunciante: Femenino")
        if SexoDenunciante == "0":
            print ("Sexo del/la denunciante: Masculino")       
            print (Dnidenunciante)
            print (DomicilioDenunciante)
            print (NumeroDeTelefonoDenunciante)
            print (VinculoConElDenunciado)
            print (" ")        
    while True:
        preg=input ("Si la informacion es correcta, Ingrese 1, para volver a ingresar presione 0: ")
        if preg == "1":
            cerrarWhile=cerrarWhile+1
        break
        if preg != "1" and preg != "0":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR LA OPCION.")
        if preg == "0":
            break
    return Dnidenunciante,DomicilioDenunciante,NumeroDeTelefonoDenunciante,VinculoConElDenunciado

def denuciado():
    while cerrarWhile==0:
        print("****************************************DATOS DEL DENUNCIADO****************************************\n")
        NombreDenunciado=input("Nombre completo del denunciado: ")
        NombreDenunciado=NombreDenunciado.upper()
    while True:
        SexoDenunciado = input("Sexo del/la denunciante (0=Masculino, 1=Femenino): ")
        if SexoDenunciado != "1" and SexoDenunciado != "0":
            print ("Respuesta incorrecta, vuelva a ingresar...")
            break    
    while True:
            Dnidenunciado = input("D.N.I del denunciante (Eje: xx.xxx.xxx ) Ingrese 0 para DESCONOCIDO: ")
            if Dnidenunciado=="0":
                Dnidenunciado = "DESCONOCIDO"
                break
            else:
                if len(Dnidenunciado)<9 or len(Dnidenunciado)>10:
                    print ("Cantidad incrrecta de caracteres: ")
                    break
    DomicilioDenunciado = input("Domicilio del denunciado (Ingrese 0 para DESCONOCIDO): ")
    DomicilioDenunciado=DomicilioDenunciado.upper()
    NumeroDeTelefonoDenunciado = input("N° de telefono del denunciado (Ingrese 0 para DESCONOCIDO): ")
    if DomicilioDenunciado == "0" :
        DomicilioDenunciado = "DESCONOCIDO"
    if NumeroDeTelefonoDenunciado == "0" :
        NumeroDeTelefonoDenunciado = "DESCONOCIDO"
    if SexoDenunciado == "0" :
        sexo1 = "el Sr."
    if SexoDenunciado == "1" :
        sexo1 = "la Sra."    
    os.system ("cls")
    print ("************************* ")
    print ("LOS DATOS INGRESADOS SON: ")
    print ("************************* ")
    print (" ")
    print (NombreDenunciado)
    if SexoDenunciado == "1":
        print ("Sexo del/la denunciado: Femenino")
    if SexoDenunciado == "0":
        print ("Sexo del/la denunciado: Masculino")
        print (Dnidenunciado)
        print (DomicilioDenunciado)
        print (NumeroDeTelefonoDenunciado)
        print (" ")
    while True:
        preg=input ("Si la informacion es correcta, Ingrese 1, para volver a ingresar presione 0: ")
        if preg == "1":
            cerrarWhile=cerrarWhile+1
            break
        if preg != "1" and preg != "0":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR LA OPCION.")
        if preg == "0":
            break
    return NombreDenunciado,SexoDenunciado,Dnidenunciado,DomicilioDenunciado,NumeroDeTelefonoDenunciado

def providencia():

	pp1="Agréguese denuncia efectuada ante la"+Comisaria+",por "+sexo+" "+NombreDenunciante+".\nTéngase por iniciada formal denuncia en los términos de la Ley XIV Nº 6 contra "+sexo1+""+NombreDenunciado+"."
	pp2="\nGírense las actuaciones al defensor oficial en turno a fin de que asuma el patrocinio letrado de "+sexo+" "+NombreDenunciante+" y efectúe las peticiones y diligencias necesarias."
	pp3="\nSeñálese primera audiencia en los términos del art. 5 de la Ley XIV Nº 6  a fin de que "+sexo+" "+NombreDenunciante+" comparezca, cualquier día hábil de la semana, de lunes a viernes de 07:00 a 11:00 ante los estrados de este Juzgado de Violencia Familiar Nº 1. Notifíquese personalmente o por cédula estando a cargo de la defensoría patrocinante su confección y diligenciamiento."
	pp4="\nSeñálese entrevista psicológica a "+sexo+" "+NombreDenunciante+" y "+sexo1+""+NombreDenunciado+", a cargo del Gabinete Psicológico del Cuerpo Médico Forense del Poder Judicial anexo Palacio de Justicia sito en Av. Santa Catalina Nº 1735, quienes deberán cumplir su cometido ante la presentación de las nombradas por ante dicho cuerpo, debiendo elevar el informe correspondiente en forma urgente. Notifíquese personalmente o por cédula estando a cargo de la defensoría patrocinante su confección y diligenciamiento."
	pp5="\nRemítanse las presentes actuaciones al Servicio Social, a los fines de la notificación y para que realicen de manera URGENTE un amplio informe socio ambiental en el domicilio de "+sexo+" "+NombreDenunciante+", sito en "+ DomicilioDenunciante +", respecto de: 1).- El estado de la vivienda, 2).- Personas que habitan en el domicilio, 3).- Relación de vecindad, 4).- Si los niños y/o adolescentes tienen seguimiento de salud (como ser vacunaciones, controles médicos, etc.), 5).- Personas que se encuentran en el hogar al momento de la entrevista y su relación con la familia, 6).- Si existen indicios de violencia intrafamiliar; y todo otro dato de interés relacionado a la problemática familiar."
	pp6="\nDése intervención a la Subsecretaria de la Mujer y de la Juventud - Dirección de Violencia Familiar y Género, dependiente del Ministerio de Desarrollo Social, la Mujer y la Juventud de la provincia de Misiones, a fin de que coordinen los Servicios  Públicos y privados a fin de contener, evitar o en su caso superar las causas de maltrato, abuso y todo tipo de violencia dentro de la familia de la denunciante, a tal fin líbrese oficio pertinente."
	pp7="\nGírense las actuaciones al Ministerio Pupilar a fin de que tome intervención y realice las peticiones que estime corresponder."
	pp8="\nNOTIFÍQUESE"
	pp0=pp1+pp2+pp3+pp4+pp5+pp6+pp7+pp8
	return pp0


def  sfaasdas(args):
    











    pass    


