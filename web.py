from flask import Flask, request
from werkzeug.utils import secure_filename
import os
from read import read

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'upload')


@app.route('/file', methods=["POST"])
def upload():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.mkdir(app.config['UPLOAD_FOLDER'])
    if request.method == "POST":
        f = request.files['file']
        file_name = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        file = os.path.splitext(os.path.basename(file_name))[0]
        result_file = os.path.join(app.config['UPLOAD_FOLDER'], file + '.txt')
        read(os.path.join(app.config['UPLOAD_FOLDER'], file_name),
             result_file)
    return result_file


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
