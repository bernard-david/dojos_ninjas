from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def read_all():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route("/dojos/create", methods=["POST"])
def create_dojo():
    Dojo.create(request.form)
    return redirect("/")

@app.route("/dojo/<int:dojo>")
def show(dojo):
    data = {"id": dojo}
    dojo = Dojo.get_one_dojo(data)
    dojo_name = Dojo.get_dojo(data)
    return render_template("show_dojo.html", dojo = dojo, dojo_name = dojo_name)

@app.route("/ninjas")
def new_ninja():
    dojos = Dojo.get_all()
    return render_template("create_ninja.html", dojos = dojos)

@app.route("/ninja/create", methods=["POST"])
def create_ninja():
    dojo_id = request.form['dojo_name']
    Ninja.create_ninja(request.form)
    return redirect(f"/dojo/{dojo_id}")


