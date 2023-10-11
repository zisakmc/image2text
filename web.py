from flask import Flask, send_from_directory
from flask import render_template, request
from werkzeug.utils import secure_filename
import textfromimage
import os

app = Flask(__name__)
obj = textfromimage.TextFromImage()

app.config['UPLOAD_FILE'] = os.getcwd() + '/uploads'

@app.route('/')
def index():
    return render_template("index.html") 


@app.route('/extract', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        # print(request.files['image'])
        file = request.files['image']
        filepath = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FILE'], filepath))
        image = os.path.join(app.config['UPLOAD_FILE'], filepath)
        text = obj.extract(image)
        return render_template('extract.html', image=file.filename, text=text)

@app.route('/uploads/<filename>')
def file(filename=''):
    return send_from_directory(app.config['UPLOAD_FILE'], filename)

if __name__ == "__main__":
   app.run() 
