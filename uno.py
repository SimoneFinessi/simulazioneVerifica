from flask import Flask , render_template#libreria che permette di ostare siti web
import datetime
app = Flask(__name__)
adesso = datetime.datetime.now()

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html",ora=adesso)

@app.route('/mappa', methods=['GET'])
def map():
    return render_template("indexmappa.html",ora=adesso)

@app.route('/mappa600', methods=['GET'])
def mappa600():
    return render_template("indexmappa.html",ora=adesso,mappa=600)

@app.route('/mappa800', methods=['GET'])
def mappa800():
    return render_template("indexmappa.html",ora=adesso,mappa=800)

@app.route('/mappa1000', methods=['GET'])
def mappa1000():
    return render_template("indexmappa.html",ora=adesso,mappa=1000)

@app.route('/template', methods=['GET'])
def temp():
    return render_template("/Arsha/index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)