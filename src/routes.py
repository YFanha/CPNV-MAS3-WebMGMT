import json
from flask import Flask, render_template, request, redirect
import subprocess

DATA_FILE = "data.json"

app = Flask(__name__,static_folder="static")
# app.config.from_object('config')

@app.route('/')
def index():
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    return render_template('index.html', clients=data['clients'])


@app.route('/edit/', methods=['GET', 'POST'])
def edit_data():
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    return render_template('edit.html', clients=data['clients'])

@app.route('/about/')
def about():
    return render_template('about.html')

def error(error):
    return render_template('error.html', error=error)

@app.route('/save/', methods=['POST'])
def save_data():
    try:
        names = request.form.getlist('name')
        nbrs = request.form.getlist('nbr')
        client_id = request.form.getlist('id')

        data = {
            "clients" : [
                {"id": client_id, "name": name, "nbr_vms": nbr}
                for client_id, name, nbr in zip(client_id, names, nbrs)
            ]
        }

        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        subprocess.run(["terraform", "apply", "--auto-approve"], check=True)
        return redirect("/")
    except Exception as e:
        return error(str(e))