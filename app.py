from flask import Flask, render_template, request, redirect
from random import randint

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


class AddUser():
    grade = 0
    def __init__(self, login, password1, password2, email):
        self.login = self.check_login(login)
        self.password1 = self.check_password(password1, password2)
        self.password2 = self.password1
        self.email = self.check_email(email)

    def check_login(self, login):
        import string
        flag = False
        if len(login) > 5:
            for s in login:
                if s in string.ascii_letters:
                    flag = True
                else:
                    flag = False
                    break
        else:
            print('Логин меньше 5 символов')
        if flag:
            return login

    def check_password(self, password1, password2):
        if len(password1) > 5:
            if password1 == password2:
                return password1
            else:
                print('Пароли не совпадают')
        else:
            print('Пароль меньше 5 символов')
            raise ValueError

    def check_email(self, email):
        if email.count('@') == 1:
            return email
        else:
            print('Емейл не содержит @')
            return False

    def check(self):
        if self.login != False and self.password1 != False and self.email != False:
            return True

    def setGrade(self):
        if len(self.password1) > 6:
            from random import randint
            self.grade = randint(0, 100)
        return self.grade



@app.route('/registration-user', methods=['POST', 'GET'])
def registration():
    if request.method == "POST":
        try:
            login = request.form['login']
            password1 = request.form['password1']
            password2 = request.form['password2']
            email = request.form['email']
            user = AddUser(login, password1, password2, email)
            dataUser = {}
            dataUser['login'] = user.login
            dataUser['password'] = user.password1
            dataUser['email'] = user.email
            if user.setGrade():
                dataUser['grade'] = user.grade
            print(dataUser)
            if user.check():
                return redirect('/select')
        except ValueError:
            print('Данные не получены от формы лого/пасс')
    return render_template('registration-user.html')


@app.route('/select', methods=['POST', 'GET'])
def select():
    if request.method == 'POST':
        try:
            archives = request.form['archiv']
            # С чек боксом не разобрался
            # Если ставим галочку, то все ок
            # А если не ставим, то падает программа... Надо как-то ошибку вызвать, пока не знаю как
            checkbox_download = request.form['download']
            print(archives, checkbox_download)
        except ValueError:
            print('что то пошло не хорошо')
    return render_template('select.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)
