from flask import Flask, request, render_template
from app import app
import time
from app.controllers import detection
from werkzeug.utils import secure_filename
import os
from flask import flash, redirect, url_for
from flask import Response, jsonify, send_from_directory, abort
from zipfile import ZipFile

UPLOAD_FOLDER = './app/static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            userimage = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            return redirect(url_for('darknetdetections', image_name=filename))
    return render_template('inicio.html')

@app.route('/darknetdetections/<image_name>', methods=['GET','POST'])
def darknetdetections(image_name):

    numero_defeitos, tempo = detection.detect(image_name)

    alerta = " "
    files = []

    files.append(os.path.join(app.config['UPLOAD_FOLDER'], str.split(image_name, ".")[0]+".txt"))
    files.append(os.path.join(app.config['UPLOAD_FOLDER'], str.split(image_name, ".")[0]+'_defeitos.jpg'))

    with ZipFile(os.path.join(app.config['UPLOAD_FOLDER'], 'resultados.zip'),'w') as zip:
        for file in files:
            zip.write(file)

    print('🦖 arquivos compactados 🦖')

    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], str.split(image_name, ".")[0]+".txt"))
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], str.split(image_name, ".")[0]+'_defeitos.jpg'))
    if str.split(image_name, "-")[0] != '161803399':
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], image_name))

    if numero_defeitos > 0:
        alerta = "Detecção feita em {:.2f}".format(tempo) + " segundos! 🦖 Foram encontrados " + str(numero_defeitos) + " defeitos."
        try:
            return render_template('uploaded_file.html', image_name='temp.jpg', alerta=alerta)
        except FileNotFoundError:
            abort(404)
    else:
        alerta = "Detecção feita em {:.2f}".format(tempo) +" segundos! 🦆 Nenhum defeito foi encontrado pela rede neural."
        try:
            return render_template('uploaded_file_no_results.html', image_name='temp.jpg', alerta=alerta)
        except FileNotFoundError:
            abort(404)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, public, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0') #, port=port)
