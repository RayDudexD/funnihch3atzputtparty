from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# change this to your path with zip file ez as fug
GAME_FILES_PATH = r'C:\yourpath\smth\smth\.zip'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    return send_file(GAME_FILES_PATH, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
