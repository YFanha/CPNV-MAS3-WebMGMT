import json
from flask import Flask, render_template, request, redirect
from .ssh_commands import run_terraform_over_ssh
import os
import subprocess

DATA_FILE = "data.json"
HOST = os.environ["HOST"]
TERRAFORM_DIR = os.environ["TERRAFORM_DIR"]
USERNAME = os.environ["USERNAME"]
PRIVATE_KEY_PATH = "/etc/ssh/id_ssh_key"
SOPS_KEY_FILE = os.environ["SOPS_AGE_KEY_FILE"]

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

        # Build the SSH command
        ssh_command = [
            "ssh",
            f"{USERNAME}@{HOST}",
            "-i", PRIVATE_KEY_PATH,
            f"cd {TERRAFORM_DIR} && SOPS_AGE_KEY_FILE={SOPS_KEY_FILE} terraform apply --auto-approve" 
        ]

        # Execute the command using subprocess
        subprocess.run(
            ssh_command,
            text=True,
            capture_output=True
        )
        return redirect("/")
    except Exception as e:
        return error(str(e))