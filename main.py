from flask import Flask, request, render_template, redirect
import db_operations

app = Flask(__name__)

@app.route('/', methods=['POST', 'get'])
def index():
    text = db_operations.get_text()
    if text is None:
        text=[]
    if request.method == 'POST':
        text = request.form.get('text')
        text = db_operations.added(text)

        return render_template('index.html', text=text, prod=db_operations.get_text())

    return render_template('index.html', prod=text)

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    delete = db_operations.delete(id)
    return redirect('/')

@app.route('/galka/<int:id>/<int:bolev>', methods=['POST', 'GET'])
def galka(id, bolev):
    db_operations.galka(id, bolev)
    return redirect('/')
app.run()
