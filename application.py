from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route("/")
#def index():
#	return "<p><b>Hello, World!!!</b></p>"

#@app.route("/<string:name>")
#def makako(name):
#	return "<p><b>Hello, {}!!!</b></p>".format(name)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/curriculum", methods=["POST"])
def curriculum():
	name=request.form.get("name")
	fecha=request.form.get("fecha")
	ocupacion=request.form.get("ocupacion")
	email=request.form.get("email")
	telefono=request.form.get("phone")
	nacionalidad=request.form.get("nacionalidad")
	ingles=request.form.get("ingles")
	lenguaje=request.form.get("python")
	aptitudes=request.form.get("Aptitudes")
	perfil=request.form.get("perfil")
	return render_template("Curriculum.html", 
		newname=name,
		newfecha=fecha,
		newocupacion=ocupacion,
		newemail=email,
		newtelefono=telefono,
		newnacionalidad=nacionalidad,
		newingles=ingles,
		newlenguaje=lenguaje,
		newaptitudes=aptitudes,
		newperfil=perfil)
