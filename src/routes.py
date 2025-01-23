import json
from flask import Flask, render_template, request, redirect
from .ssh_commands import run_terraform_over_ssh
import os

DATA_FILE = "data.json"
HOST = os.environ["HOST"]
TERRAFORM_DIR = os.environ["TERRAFORM_DIR"]
USERNAME = os.environ["USERNAME"]
PRIVATE_KEY_PATH = "/etc/ssh/id_ssh_key"

app = Flask(__name__,static_folder="static")

@app.route('/')
def index():
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    
    return render_template('index.html', clients=data['clients'], host=HOST)


@app.route('/edit/', methods=['GET', 'POST'])
def edit_data():
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    return render_template('edit.html', clients=data['clients'])

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

        run_terraform_over_ssh(HOST, PRIVATE_KEY_PATH, TERRAFORM_DIR, USERNAME)
        return redirect("/")
    except Exception as e:
        return error(str(e))