import json
from flask import Flask, render_template, request, redirect

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

@app.route('/save/', methods=['POST'])
def save_data():
    names = request.form.getlist('name')
    nbrs = request.form.getlist('nbr')
    client_id = request.form.getlist('id')

    # print(f"=======>{request}")

    data = {
        "clients" : [
            {"id": client_id, "name": name, "nbr_vms": nbr}
            for client_id, name, nbr in zip(client_id, names, nbrs)
        ]
    }

    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return redirect("/")