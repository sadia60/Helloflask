# Flask is class that represents a flask application
# render_template function processes flask template and returns the page as response
# jsonify function converts "python dict" into "json string"
from flask import Flask, render_template, jsonify, request

# __name__ is filename and it is being set as application name
app = Flask(__name__)
app.foo = 0


# this is one endpoint defined on route "/"
# handler function can have any name "hello_world" in this case
@app.route('/')
def hello_world():
    # return the homepage
    return render_template('hello.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def registerPost():
    name = request.form['name']
    email = request.form['email']
    i = 1
    info = []
    while 'info' + str(i) in request.form:
        info.append(request.form['info' + str(i)])
        i += 1
    app.user = {'name': name, 'email': email, 'info': info}
    return jsonify({'name': name, 'email': email, 'info': info})


@app.route('/deadpool')
def deadpool():
    return render_template('task.html')


@app.route('/get_data')
def get_data():
    # return json response to be consumed by frontend
    return jsonify({'name': 'Asim', 'title': 'Software Engineer'})


@app.route('/get_info')
def get_user_info():
    app.foo = app.foo + 1
    # return json response to be consumed by frontend
    return jsonify(app.user)
