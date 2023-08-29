from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Создаем cookie
        response = make_response(redirect('/welcome'))
        response.set_cookie('user_name', name)
        response.set_cookie('user_email', email)
        return response

    return render_template('index.html')


@app.route('/welcome')
def welcome():
    user_name = request.cookies.get('user_name')
    return render_template('welcome.html', user_name=user_name)


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
