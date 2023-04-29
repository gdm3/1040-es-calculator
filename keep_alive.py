from flask import Flask, render_template
from threading import Thread
import discord
app = Flask('')
@app.route('/')
def main():
    return render_template('board.html')
@app.route('/rip', methods=['GET', 'POST'])
def rip():
  return "shutdown is not yet supported"
def run():
    app.run(host="0.0.0.0", port=8080)
def keep_alive():
    server = Thread(target=run)
    server.start()