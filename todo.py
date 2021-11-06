from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Karabey TECH/Desktop/VSCODE/TodoApp/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos = todos)

@app.route("/complite/<string:id>")
def compliteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    todo.complite = not todo.complite
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/add", methods = ["POST"])
def addTodo():
    #başlıksız eklememe ekle
    title =  request.form.get("title")
    newTodo = Todo(title = title, complite = False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))




class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String (80))
    complite = db.Column(db.Boolean)


if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
