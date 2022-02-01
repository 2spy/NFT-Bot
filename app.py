from os import system
try:
    from flask import Flask, render_template, url_for, request
except:
    system("pip install flask")

import webbrowser
from threading import Timer
import json


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        pseudo = request.form.get("pseudo")
        mdp = request.form.get("mdp")
        clientid = request.form.get("clientid")
        clientsecret = request.form.get("clientsecret")
        webhook = request.form.get('webhook')
        metakey = request.form.get("metakey")
        spykey = request.form.get("spykey")

        with open('config.json', "r") as confg:
            config = json.load(confg)
        with open('config.json', 'w+') as confg:
            config["pseudo"] = pseudo
            config["mdp"] = mdp
            config["clientid"] = clientid
            config['clientsecret'] = clientsecret
            config['webhook'] = webhook
            config['metakey'] = metakey
            config["spykey"] = spykey
            config["phrase"] = ["done.", "lets go !", "nice NFT !", "I have do all steps !", ":)"]
            json.dump(config, confg, indent=4)
        system("python nftbot.py")
    return render_template("accueil.html")





@app.route('/home')
def home():
    return render_template("accueil.html")


@app.route('/start', methods=['POST', 'GET'])
def start():
    return render_template('start.html')


@app.route('/dash', methods=['POST', 'GET'])
def dash():
    return render_template('dash.html')


def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')


if __name__ == "__main__":
    Timer(1, open_browser).start();
    app.run(port=5000)
