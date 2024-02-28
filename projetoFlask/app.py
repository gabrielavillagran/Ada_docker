from flask_bootstrap import Bootstrap5
from flask import Flask, request,json,jsonify, url_for,render_template
import requests
import flask_mysqldb
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["DEBUG"] = True

app.config["MYSQL_HOST"] = "mysql_api_container"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "minhasenha"
app.config["MYSQL_DB"] = "flaskdocker"

bootstrap = Bootstrap5(app)
mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
    fact = requests.get("https://catfact.ninja/fact")
    return render_template("index.html",
                            data_json = fact.json())


@app.route("/inserthost", methods=["POST","GET"])
def inserthost():
    data = requests.get("https://catfact.ninja/fact").json()
    data = data["fact"]
    cur = mysql.connect.cursor()
    cur.execute("""INSERT INTO facts(fact) VALUES(%s)""", (data,))
    mysql.connection.commit()
    cur.close()

    return render_template("post.html",
                            data_json_post = data)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True, port=5000)
