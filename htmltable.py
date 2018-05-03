from flask import Flask, render_template
app= Flask(__name__)

users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi', 'number' : '1'},
   {'first_name' : 'John', 'last_name' : 'Supsupin', 'number' : '2'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen', 'number' : '3'},
   {'first_name' : 'KB', 'last_name' : 'Tonel', 'number' : '4'}
);

@app.route('/')
def table():
	return render_template("index.html",users=users)

app.run(debug=True)