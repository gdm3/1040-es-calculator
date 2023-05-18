from gevent import monkey
monkey.patch_all()
from flask import Flask, render_template, request, redirect, jsonify
from gevent.pywsgi import WSGIServer

from taxCalc import taxCalc

app = Flask(__name__)

@app.route('/')
def start():
  return redirect("/taxes")
@app.route('/news')
def news():
  return render_template("news.html")
@app.route('/contact')
def contact():
  return render_template("contact.html")
 
@app.route('/taxes', methods=('GET', 'POST'))
def index():
  if request.method == 'GET':
    return render_template("index.html")
  elif request.method == 'POST':
    #Validate Info + Ensure purchase met later
    data = request.get_json()

    QuartIncome = float(data[0]['QuartIncome'])
    QuartDeduction = float(data[1]['QuartDeduction'])
    AltMinTax = float(data[2]['AltMinTax'])
    Credits = float(data[3]['Credits'])
    OthTaxes = float(data[4]['OthTaxes'])
    IncTaxWith = float(data[5]['IncTaxWith'])
    
    taxesInfo = taxCalc(QuartIncome, QuartDeduction, AltMinTax, Credits, OthTaxes, IncTaxWith)
    
    results = {'processed': str(taxesInfo)}
    return jsonify(results)


http_server = WSGIServer(('0.0.0.0', 8080), app)
http_server.serve_forever()
