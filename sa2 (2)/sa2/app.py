from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User
from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey, Numeric, Text
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)
app.secret_key = '235689' # нужно для управления сессиями ползователей и шифрования
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORRECT_ANSWERS = {'name': 'admin', 'password': 'admin'}
db.init_app(app)

login_manager = LoginManager() # или без app ?
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
initialized = False  # если инициализация в первый раз и базы данных почему-то нет(

@app.before_request  # если файла с базой данных в папке instance нет, то он в первый раз содаётся заново! В след раз не создавать! 
def initialize_once():
    global initialized
    if not initialized:
        initialized = True
        db.create_all()

@app.context_processor
def inject_user_status():
#   Это нужно для вставки статуса пользователя в шаблоны templates
    return {"Текущий пользователь": current_user}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
@app.route("/amin", methods=["GET"])
def admin():
    return render_template("results.html")
@app.route("/user", methods=["GET"])
def user():
    return render_template("results_fall.html")

@app.route("/zavki", methods=["GET"])
def zavki():
    return render_template("zavki.html")
# @app.route("/class", methods=["POST"])
# def class_selection():
#     name = request.form.get("name")
#     password = request.form.get("password")
#
#     if name == CORRECT_ANSWERS['name'] and password == CORRECT_ANSWERS['password']:
#         return render_template("results.html")
#     else:
#         return render_template("results_fall.html")


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        login = request.form['login']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if len(username) < 3 or len(username) > 100:
            flash('Имя пользователя должно быть длиной от 3 до 100 символов')
            return render_template('registration.html')
        if len(login) < 3 or len(login) > 25:
            flash('Логин пользователя должен быть длиной от 3 до 25 символов')
            return render_template('registration.html')
        if len(password) < 3 or len(password) > 25:
            flash('Пароль пользователя должен быть длиной от 3 до 25 символов')
            return render_template('registration.html')

        if password != confirm_password:
            flash('Пароли не совпадают!')
            return render_template('registration.html')
        
        if User.query.filter_by(login=login).first():
            flash('Пользователь с таким логином уже существует!')
            return render_template('registration.html')

        #hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, login=login, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Регистрация прошла успешно!')
        return redirect(url_for('login'))

    return render_template('registration.html')    


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = User.query.filter_by(login=login).first()
        if user and user.password == password:
            login_user(user)
            if login == "admin":
                return redirect(url_for('admin')) # если админ , то сюда)
            else:
                return redirect(url_for('user'))
        else:
            flash(f'Неверные данные!')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


'''
Base = declarative_base()


class User(Base):
    tablename = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum('admin', 'user'), nullable=False)


class Inventory(Base):
    tablename = 'inventory'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    condition = Column(Enum('new', 'used', 'broken'), nullable=False)


class Request(Base):
    tablename = 'requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    status = Column(Enum('pending', 'approved', 'rejected'), default='pending')


class Purchase(Base):
    tablename = 'purchases'

    id = Column(Integer, primary_key=True)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    supplier = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)


class RepairRequest(Base):
    tablename = 'repair_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    description = Column(Text, nullable=False)


DATABASE_URL = "postgresql://username:password@localhost:5432/inventory_db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_user(username: str, password: str, role: str):
    session = SessionLocal()
    new_user = User(username=username, password=password, role=role)

    session.add(new_user)
    session.commit()
    session.refresh(new_user) 
    session.close()

    return new_user


if __name__ == 'main':
    user = create_user("admin", "securepassword", "admin")
    print(f"Created user: {user.username} with role {user.role}")
'''

if __name__ == '__main__':
    app.run(debug=True)

