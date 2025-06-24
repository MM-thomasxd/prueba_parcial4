opcion=0
concierto_diccionario={}



def eliminar_comprador_concierto(nombre): 
    nombre=nombre.lower()
    if nombre in concierto_diccionario:
       del concierto_diccionario[nombre]
       print(" compra cancelada ")
       return True
    else:
       print("No se pudo cancelar la compra")
       return False
    
def buscar_comprador_concierto (nombre):
  nombre=nombre.lower()
  if nombre in concierto_diccionario:
       print("se ha buscado exitosamente") 
       print (f"tipo de entrada: {concierto_diccionario[nombre][0]} ,codigo:{concierto_diccionario[nombre][1]} " )
       return True
  else:
       print("el comprador no se encuentra  o no existe , intente de nuevo")
       return False
 

def contador_numeros_codigo(codigo):
 contador=0 
 for letra in str(codigo):
   if letra.isnumeric():
     contador+=1
 return contador


def contador_mayusculas_codigo(codigo):
 contador=0
 for letra in str(codigo):
   if letra.isupper():
     contador+=1
 return contador


def comprar_y_validar (nombre,entrada,codigo):
  while True :
    if nombre == None : 
       print("no se ha ingresado el nombre, por favor ingrese un nombre ")  
       return False
    elif nombre in concierto_diccionario:
       print ("este nombre ya existe,intente de nuevo")
       return False
    elif entrada != "G" and entrada!="V":
       print("solamente puede ingresar (G y V), intente de nuevo")
       return False
    
    elif len(codigo) != 6 :
       print ("solamente se admiten 6 caracteres en el codigo ,intente de nuevo")
       return False
    elif contador_mayusculas_codigo(codigo) < 1 : 
        print ("minimo 1 mayusculas en el codigo de verificacion, intente de nuevo")
        return False
    elif contador_numeros_codigo(codigo)< 1 :
        print("minimo 1 numero en el codigo de validacion,intente de nuevo")
        return False
    else:
       print("entrada con exito")
       concierto_diccionario[nombre]=[entrada,codigo]
       return True
    


while opcion !="4":
 print("MENU PRINCIPAL")
 print("1.- Comprar entrada.")
 print("2.- Consultar comprador.")
 print("3.- Cancelar compra.")
 print("4.- Salir.")
 opcion=input("ingrese la opcion ")

 match opcion :
   case "1":
     nombre_Comprador=input("por favor ingrese el nombre de comprador :").lower()
     tipo_entrada=input("por favor ,ingrese el tipo de entrada(G/V):").upper()
     codigo_confirmacion=input("por favor ingrese el codigo de confirmacion:")
     comprar_y_validar(nombre_Comprador,tipo_entrada,codigo_confirmacion)
   case "2":
     buscar_comprador=input("ingrese el nombre del comprador que esta buscando:").lower()
     buscar_comprador_concierto(buscar_comprador)
   case "3":
     eliminar_comprador=input("ingrese al comprador que quiere eliminar:").lower()
     eliminar_comprador_concierto(eliminar_comprador)
   case "4":
     print("Programa terminado...")
     
   case default :
     print("Debe ingresar una opción válida!")
      