
# usuario=(input("señor deme la palabra: "))
# for i in range(10):
#     print(usuario)

# 

# numero=int(input("ingrese su  numero : "))

# for i in range(1,numero+1,2):
#        print(i,end=",") 
            
# numero=int(input("ingrese su  numero : "))

# for i in range(numero,-1,-1):
#        print(i,end=",") 
               
                    
# nombre= input("ingrese su nombre : ") 
# dinero_dis=float(input("cual es el monto que desea invertir :"))
# el_int= float(input("cual es el interes  anual : "))
# cda= int(input("cuantos años va a invertir : "))

# #hojo una leccion es cuando vallamos a concatenar no lo podemos hacer con datos float 
# for i in range(cda+1):
#     dinero_dis*= 1 + el_int/100
#     print("capital tras" + str (i+1) +"años : " + str(round(dinero_dis,2)))
    
   
    
# numero=int(input("ingrese un numero"))
# for i in range(numero):
#     print("*"*(i+1))
    
# while True:
#     ndu= int(input("ingrese el numero  : ")) 
#     if ndu >0:
#         try:
#             for i in range(1,10+1): 
#                 resultado = str(ndu) + "*"+ str(i) + "="+ str(ndu*i)
#                 print(resultado) 
#         except:
#             print("te pedi un numero positivo no una letra ni numero negativo")
#         else:
#             break
    
    
    
# while True:
#     ndu= int(input("ingrese el numero  : ")) 
#     if ndu >0:
        
#         try:
#             resultado=0
#             for i in range(1,ndu+1):
                
#                 resultado +=  (1/i) 
#             print("el resultado de la serie es de :",round(resultado,2)) 
#         except:
#             print("te pedi un numero positivo no una letra ni numero negativo")
#         else:
#             break
     
         
# while True:
#     ndu= int(input("ingrese el numero  : ")) 
#     if ndu >0:
        
#         try:
#             resultado=1 
#             for i in range(2,ndu+1):
#                 if i % 2==0:
#                     resultado=resultado / (1/i) 
                    
#                 else:
#                     resultado= resultado *(1/i)    
                
#             print(resultado)   
#         except:
#             print("te pedi un numero positivo no una letra ni numero negativo")
#         else:
#             break


# while True:
#     numeros= int(input("ingrese sus numeros :"))
#     positivos=0
#     negativos=0
#     nulos=0
#     try:
#         for i in range(numeros):
#             dato=int(input("ingrese un numero natural"))
    
#             if dato > 0:
#                 positivos+=1
                
#             elif dato < 0:
#                 negativos+=1
#             else: 
#                 nulos+=1
                
                
#         print("la cantidad de numeros pasitivos fue :",positivos,
#               "\n la cantidad de numeros negativos fue :",negativos,
#             "\n la cantidad de numeros nulos fue: ",nulos)       
        
#     except:
#         print("ingresa nuevamente LOS NUMEROS ")
        
#     else:
#         break            


# while True:
    
#     num_de_per=int(input("ingrese el numero de pesonas del estado: "))
#     cantidad_h=0
#     cantidad_m=0
#     peso_h=0
#     altura_h=0
#     peso_m=0
#     altura_m=0
    
#     try: 
#         for i in range(num_de_per):
            
#             peso= float(input("ingrese su peso : "))
#             altura=int(input("ingrese su altura "))
#             genero= input("ingrese su genero : ")
            
#             while True:
#                 if genero.upper()== "M" :
#                     peso_h+=peso
#                     altura_h+= altura
#                     cantidad_h+=1
#                     False
#                 elif genero.upper()== "F":
#                     peso_m+=peso
#                     altura_m+=altura
#                     cantidad_m+=1
#                     False
#                 else:
#                     print("intentelo nuevamente")    
        
#         promedi_altura_h=0
#         promedi_peso_h=0           
#         if cantidad_h > 0:
#             promedi_peso_h= peso_h / cantidad_h
#             promedi_altura_h= altura_h / cantidad_h
            
#         promedi_altura_m=0
#         promedi_peso_m=0
            
#         if cantidad_m > 0:
#             promedi_altura_m= altura_m / cantidad_m
#             promedi_peso_m= peso_m / cantidad_m
        
#         print(" el peso y altura promedio de mujeres y hombres son:"
#             "\n promedio peso de hombres es de ",promedi_peso_h,        
#             "\n promedio altura de hombres es de ",promedi_altura_h,        
#             "\n promedio peso de mujeres  es de ",promedi_peso_m,
#             "\n promedio altura de mujeres es de ",promedi_altura_m)        
             
#     except :
#         print("te pedi un genero no cualquier cosa ")    
            
#     else:
#         break        
                
        
# while True:
#     dato=int(input("igrese el numero entero :"))
    
#     if dato>0:
#         try:
            
#             resultado=0
#             for i in range(1,dato+1):
#                 if i % 2==0:
#                     resultado-=   i**i 
                    
#                 else:
#                     resultado+=  i**i   
                
#             print(f" el resultado de la serie :{resultado}")
#         except:
#             print("te pedi un numero positivo no una letra ni numero negativo")
#         else:
#             break


while True:
    numero_positivo= int(input("ingrese el numero entero positivo:>"))
    if numero_positivo > 0:
        try:
            
            for i in range(2,numero_positivo):
                creciente=2
                es_primo=True
                while es_primo and creciente < i:
                    if i % creciente==0:
                        es_primo=False
                    else:
                        creciente+=1
                if es_primo:
                            
                            
                    print(f"todos los numeros primos menores a dicho numero son : {i}")
                
        except:
            print("te pedi un numero  y que sea positivo") 
        else:
            break           

    
 
   
            
        
        
    
    


