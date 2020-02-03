from flask import Flask, redirect, render_template, request

app = Flask(__name__)

todos = []          #global variable for storing the todo list
 
@app.route('/')
def home():
    return render_template('index.html', tasks = todos)

@app.route('/add', methods=["GET", "POST"])
def create_tasks():
    if request.method == "GET":
        return render_template('new_task.html')
    else:
        todo = request.form.get('tasks')
        todos.append(todo)
        return redirect('/')

if __name__ == '__main__':
    app.run(port=5000)
