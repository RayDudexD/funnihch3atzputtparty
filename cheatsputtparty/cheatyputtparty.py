from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Use a raw string for the path or replace backslashes with double backslashes
GAME_FILES_PATH = r'C:\Users\RayDude\Documents\Projekty\cheatsputtparty\CHEATSPUTPARTY.zip'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    return send_file(GAME_FILES_PATH, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
