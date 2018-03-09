import json
from funciones import opcion1

with open("poblacion.json") as fichero:
	datos=json.load(fichero)


while True:
	print("""Elija una opción de las siguientes 5 (\"0\" para salir)\n
1.Provincias que tienen mas de una cifra de poblacion en los años dados.
2.Numero de provincias que tengan mas población de un sexo por años.
3.Muestra las provincias que esten en un rango de población y año y muestra el sexo 
con mayor población en cada provincia.
4.Muestra la población dada una provincia, sexo y año.
5.Muestra las provincias por año en el que la población mayor es de un sexo.\n""")
	opcion=input("Opcion: ")
	if opcion not in ["0","1","2","3","4","5"]:
		print("Por favor elija una opcion correcta\n")
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
			num=0
			print("Escriba los años deseados comprendidos entre 1998-2017 o 1996")
			while True:
				num+=1
				año=int(input("Año {} (0) para continuar: ".format(num)))
				if año !=0:
					años.append(año)
				else:
					break
			print("")
			opcion1(datos,cifra,años)
	if opcion=="2":
		while True:
			sexo=input("Elija un sexo (h/Hombre m/mujer) (0 para volver):\n")
			print("")
			if sexo=="0":
				break
			if sexo=="h":
				sexo="Hombres"
			if sexo=="m":
				sexo="Mujeres"
			opcion2(datos,sexo)
	if opcion=="3":
		asd
	if opcion=="4":
		asd
	if opcion=="5":
		asd