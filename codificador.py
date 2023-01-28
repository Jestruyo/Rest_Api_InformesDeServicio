import json
import csv

with open("BDinformes.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    listaBD = []
    
    for row in reader:
        listaBD.append({"id":row[0],"nombre":row[1],"apellido":row[2],"grupo":row[3],"horas":row[4],"revisitas":row[5],"cursos biblicos":row[6],"publicaciones":row[7],"videos":row[8]})

with open("BDinformes.json","w") as f:
    json.dump(listaBD,f,indent=4)        