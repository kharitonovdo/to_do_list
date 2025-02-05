from flask import Flask, request, render_template
import db_operations

app = Flask(__name__)

@app.route('/', methods=['POST', 'get'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        db_operations.added(text)
        print(text)
        return render_template('index.html', text=text)
    return render_template('index.html')

app.run()
