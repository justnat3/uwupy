from uwuhttp import HttpUwU
from flask import Flask
import json


app = Flask(__name__)
err = HttpUwU()

if __name__ == "__main__":
    yeet = json.loads(err.uwuHttpError(500))
    print(yeet)
