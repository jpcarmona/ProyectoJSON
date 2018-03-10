import json
from funciones import borrado_total,opcion1,opcion2,opcion3,opcion4,opcion5,provincias,años

with open("poblacion.json") as fichero:
	datos=json.load(fichero)

borrado_total(datos)

listaaños=años(datos)

while True:
	print("""Escriba una opción de las siguientes 5 (\"0\" para salir)\n
1.Provincias que tienen mas de una cifra de poblacion en los años dados.
2.Numero de provincias que tengan mas población de un sexo por años.
3.Muestra las provincias que esten en un rango de población y año y muestra el sexo 
con mayor población en cada provincia.
4.Muestra la población dada una provincia, sexo y año.
5.Muestra las provincias por año en el que la población mayor es de un sexo.\n""")
	opcion=input("Opcion: ")
	if opcion not in ["0","1","2","3","4","5"]:
		print("Por favor Escriba una opcion correcta\n")
		continue
	if opcion=="0":
		break
	if opcion=="1":
		while True:
			cifra=int(input("Escriba una cifra de población (0 para volver):\n"))
			print("")
			if cifra==0:
				break			
			años=[]
			num=1
			print("Escriba los años deseados comprendidos entre 1998-2017 o sea 1996")
			while True:				
				año=int(input("Año {} (0) para continuar: ".format(num)))
				if año==0:
					break
				if año not in listaaños:
					print("No es un año valido")
					continue
				else:
					años.append(año)
					num+=1					
			print("")
			opcion1(datos,cifra,años)
	if opcion=="2":
		while True:
			sexo=input("Escriba un sexo (h/Hombre m/mujer) (0 para volver):\n")
			print("")
			if sexo=="0":
				break
			if sexo=="h":
				sexo="Hombres"
			if sexo=="m":
				sexo="Mujeres"
			opcion2(datos,sexo)
	if opcion=="3":
		while True:
			año=int(input("Escriba un año que esté comprendido entre 1998-2017 o sea 1996 (0 para volver):\n"))
			print("")
			if año==0:
				break
			if año not in listaaños:
				print("No es un año valido")
				continue
			rango1=int(input("Escriba el rango1 de población:\n"))
			while True:
				rango2=int(input("Escriba el rango2 de población:\n"))
				if rango2<rango1:
					print("Por favor Escriba un rango2 mayor al de rango1")
				else:
					break
			print("")
			opcion3(rango1,rango2,año,datos)
	if opcion=="4":
		while True:
			año=int(input("Escriba un año que esté comprendido entre 1998-2017 o sea 1996 (0 para volver):\n"))
			print("")
			if año==0:
				break
			if año not in listaaños:
				print("No es un año valido")
				continue
			while True:
				provincia=input("Escriba una provincia de España (0 para volver):\n")
				print("")
				if provincia=="0":
					break				
				if not provincias(datos,provincia):
					print("Provincia Incorrecta")
					continue
				else:
					provincia=provincias(datos,provincia)
					break
			if provincia=="0":
				break
			sexo=input("Escriba un sexo (h/Hombre m/mujer) (0 para volver):\n")
			print("")
			if sexo=="0":
				break
			if sexo=="h":
				sexo="Hombres"
			if sexo=="m":
				sexo="Mujeres"
			opcion4(provincia,sexo,año,datos)
	if opcion=="5":
		while True:
			sexo=input("Escriba un sexo (h/Hombre m/mujer) (0 para volver):\n")
			print("")
			if sexo=="0":
				break
			if sexo=="h":
				sexo="Hombres"
			if sexo=="m":
				sexo="Mujeres"			
			opcion5(sexo,datos)