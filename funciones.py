def borrado_total(datos):
	""" Borra las primeras
	3 listas de los datos
	que son la poblacion 
	total de España"""
	for i in range(3):
		datos.pop(0)

def opcion1(datos,cifra,años):
	dict1={}
	for año in años:
		dict1[año]=[]
	borrado_total(datos)
	for dato in datos:
		if dato["MetaData"][1]["Nombre"]=="Total":
			for año in dato["Data"]:
				if año["Anyo"] in años and año["Valor"]>cifra:
					poblacion={dato["MetaData"][0]["Nombre"]:año["Valor"]}
					dict1[año["Anyo"]].append(poblacion)
	for key in dict1.keys():
		print("Año {}".format(key))
		print("")
		for provincia in dict1[key]:
			for x,y in provincia.items():
				print("{} --> {} habitantes".format(x,int(y)))
		print("\n\n")

def opcion2(datos,sexo):
	dict1={}
	borrado_total(datos)
	for año in datos[0]["Data"]:
		dict1[str(año[Anyo])]={}
	for dato in datos:
		if dato["MetaData"][1]["Nombre"]=="Hombres" :
		
	for key in dict1.keys():
		print("Año {}".format(key))
		print("")
		for provincia in dict1[key]:
			for x,y in provincia.items():
				print("{} --> {} habitantes".format(x,int(y)))
		print("\n\n")


