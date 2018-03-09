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
	for año in datos[0]["Data"]:
		dict1[año["Anyo"]]={}
	for dato in datos:
		sex=dato["MetaData"][1]["Nombre"]
		provincia=dato["MetaData"][0]["Nombre"]
		if sex=="Total" :
			for año in dato["Data"]:
				dict1[año["Anyo"]][provincia]={}
		else:
			for año in dato["Data"]:
				poblacion=año["Valor"]			
				if sex=="Hombres":
					dict1[año["Anyo"]][provincia][sex]=poblacion
				if sex=="Mujeres":
					dict1[año["Anyo"]][provincia][sex]=poblacion		
	for key in dict1.keys():
		print("Año {}".format(key))
		num=0
		for provincia in dict1[key].keys():
			for sex in dict1[key][provincia].keys():
				pob=dict1[key][provincia][sex]
				if sex==sexo:
					pob1=pob										
				else:
					pob2=pob
			if pob1>pob2:
				num+=1
		print("{} Provincias tienen la mayor población de {}\n".format(num,sexo))


def opcion3(rango1,rango2,año1,datos):
	dict1={}
	for dato in datos:
		provincia=dato["MetaData"][0]["Nombre"]
		sex=dato["MetaData"][1]["Nombre"]		
		for año in dato["Data"]:
			if año["Anyo"]!=año1:
				continue
			total=año["Valor"]
			if sex=="Total":
				if total>=rango1 and total<=rango2:
					opcion=True
					dict1[provincia]={}
					dict1[provincia][sex]=total
				else:
					opcion=False
			if opcion:
				dict1[provincia][sex]=total
	for provincia in dict1.keys():		
		for sex in dict1[provincia].keys():
			pob=dict1[provincia][sex]
			if sex=="Hombres":
				pob1=pob										
			if sex=="Mujeres":
				pob2=pob
			if sex=="Total":
					pob3=pob
		print("{} tiene {} habitantes.".format(provincia,int(pob3)))
		if pob1>pob2:
			print("Hay mas hombres que mujeres en",provincia)
		if pob1<pob2:
			print("Hay mas mujeres que hombres en",provincia)
		if pob1==pob2:
			#seguramente sea imposible...
			print("Hay las mismas mujeres que hombres en",provincia)
		print("")
				

def opcion4(provincia,sexo,año,datos):



def opcion5(sexo,datos):
	

