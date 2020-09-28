from ohhttp import HttpUwU
from flask import Flask

app = Flask(__name__)
err = HttpUwU()


@app.route('/')
def InternalErro():
    return err.uwuHttpError(500)


if __name__ == "__main__":
    app.run()
