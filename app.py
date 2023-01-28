from flask import Flask,jsonify,request
from base import db

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"Lista general":db})

@app.route("/buscarinfo/<string:nombre>")
def binfo(nombre):
    buscarnombre = []
    for nombres in db:
        if nombres["nombre"] == nombre:
            buscarnombre.append(nombres)
    if(len(buscarnombre)>0):
        return jsonify({"Informe:":buscarnombre[0]})
    return jsonify({"Alerta":"Informacion requerida no encontrada"})

@app.route("/buscargrupo/<string:grupo>")
def bgrupo(grupo):
    buscargrupo = []
    for grupos in db:
        if grupos["grupo"] == grupo:
            buscargrupo.append(grupos)
    if(len(buscargrupo)>0):
        totalgrupos = buscargrupo
        return jsonify({"grupo numero":totalgrupos[0]["grupo"],"Integrantes":totalgrupos})
    return jsonify({"Alerta":"Grupo no encontrado"})

@app.route("/inputintegrante/", methods = ["POST"])
def input():
    nuevo_integrante = {
        "id": request.json["id"],
        "nombre": request.json["nombre"],
        "apellido": request.json["apellido"],
        "grupo": request.json["grupo"],
        "horas": request.json["horas"],
        "revisitas": request.json["revisitas"],
        "cursos biblicos": request.json["cursos biblicos"],
        "publicaciones": request.json["publicaciones"],
        "videos": request.json["videos"]
    }
    db.append(nuevo_integrante)
    print(nuevo_integrante)
    return jsonify({"Lista general":db})

@app.route("/updateintegrante/<string:id>", methods = ["PUT"])
def update(id):
    bid = []
    for ids in db:
        if ids["id"] == id:
            bid.append(ids)
    if(len(bid)>0):
        bid[0]["id"] = request.json["id"]
        bid[0]["nombre"] = request.json["nombre"]
        bid[0]["apellido"] = request.json["apellido"]
        bid[0]["grupo"] = request.json["grupo"]
        bid[0]["horas"] = request.json["horas"]
        bid[0]["revisitas"] = request.json["revisitas"]
        bid[0]["cursos biblicos"] = request.json["cursos biblicos"]
        bid[0]["publicaciones"] = request.json["publicaciones"]
        bid[0]["videos"] = request.json["videos"]
        return jsonify({"Datos actualizados":bid[0]})
    return jsonify({"Alerta":"No se encuentra la persona en lista"})
        
            
@app.route("/deleteintegrante/<string:id>", methods =["DELETE"])
def delete(id):
    bid = []
    for ids in db:
        if ids["id"] == id:
            bid.append(ids)
    if(len(bid)>0):
        db.remove(bid[0])
        return jsonify({"Lista general":db})
    return jsonify({"ERROR":"El id no esta registrado en db"})
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)