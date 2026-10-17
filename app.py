from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# База данных в виде списка (пока в памяти)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    name = request.form.get('name')
    text = request.form.get('text')
    if name and text:
        messages.append({'name': name, 'text': text})
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Этот блок сработает при локальном запуске
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)