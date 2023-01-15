import configparser
from time import sleep

from flask import Flask, redirect, render_template
from .cloud import CloudMachine

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
machine = CloudMachine(
    project=config['DEFAULT']['Project'],
    instance=config['DEFAULT']['Instance'],
    zone=config['DEFAULT']['Zone'],
    )
code_domain = config['DEFAULT']['Domain']

@app.route("/")
def get_home():
    status = machine.get_status()
    return render_template("homepage.html", status=status)


@app.route("/turn-on")
def get_turnon():
    try:
        wait_time = machine.turn_on()
        sleep(wait_time)
        return redirect(f"https://{code_domain}", code=302)
    except Error as e:
        return e


@app.route("/turn-off")
def get_turnoff():
    machine.turn_off()
    return "Success"
