from flask import Flask, render_template, request, redirect, flash, url_for
from enums.status import Status
import services, secrets

app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

@app.route('/', methods=['GET'])
def index():
    todos = services.get_todos()
    return render_template('todos/index.html',todos=todos)

@app.route('/create', methods=['GET'])
def create():
    todo = {}
    return render_template('todos/form.html', todo=todo, statuses=Status)

@app.route('/save', methods=['POST'])
def save():
    id = request.form['id']
    title = request.form['title']
    description = request.form['description']
    status = request.form['status']
    errorMessages = [];
    if(not title):
        errorMessages.append('Title field is required')
    if (not description):
        errorMessages.append('Description field is required')
    if (not status):
        errorMessages.append('Status field is required')

    if errorMessages:
        for error in errorMessages:
            flash(error)
        if(id):
            return redirect(url_for('edit',id=id))
        else:    
            return redirect('/create')
    else:
        if id:
            services.update_todo(id, title, description, status)
        else:
            services.create_todo(title, description, status)
        return redirect('/')
    
@app.route('/edit/<int:id>', methods=['GET'])  
def edit(id):
    todo = services.find_todo(id)
    return render_template('todos/form.html', todo=todo, statuses=Status)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    services.delete_todo(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)