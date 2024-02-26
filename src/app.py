from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from config import config
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required





#Modelos
from models.ModelUser import ModelUser
from models.ModelPotreros import ModelPotreros
from models.ModelLote import ModelLote
#ENTITIES
from models.entities.user import User
from models.entities.potreros import Potrero
from models.entities.lote import Lote

app = Flask(__name__, template_folder='templates')

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


""" Code User """
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        """ print(request.form['username'])
        print(request.form['password']) """
        user = User(0, request.form['username'],request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash('Invalid Password...')  
                return render_template('auth/login.html')
        else:
            flash('User not found...')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/registraruser')
def registeruser():
    return render_template('auth/register.html')

@app.route('/guardaruser', methods=['POST'])
def guardaruser():
    userName = request.form['username']
    fullname = request.form['fullname']
    password = request.form['password']
    if userName and fullname and password:
        user = User(0, request.form['username'], request.form['password'], request.form['fullname'])
        registrado = ModelUser.register(db, user)

    return redirect(url_for('registeruser'))
""" End Code User """
""" Code Potreros Create """
@app.route('/registerpotrero')
def registerpotrero():
    return render_template('auth/registrarpotrero.html')

@app.route('/listapotreros')
def listapotreros():
    return render_template('listar_potreros.html')

@app.route('/lotes')
def lotes():
    return render_template('lotes.html')


@app.route('/nuevopotrero', methods=['GET', 'POST'])
def nuevopotrero():
    if request.method == 'POST':
        """ print(request.form['username'])
        print(request.form['password']) """
        potrero = Potrero(0, request.form['nombrepotrero'].strip(),request.form['zonapotrero'],request.form['areapotrero'],request.form['diaspotrero'],request.form['paturapotrero'],request.form['estadopotrero'], request.form['coordenadapotrero'],request.form['observacionpotrero'])
        result = ModelPotreros.nuevo(db, potrero)
        return render_template('gestion.html')
    else:
        return render_template('gestion.html')

@app.route('/rmostrar')
def rmostrar():
    opcionesP = ModelPotreros.mostrarOpcionesPotreros(db)                                         
    opcionesL = ModelPotreros.mostrarOpcionesLotes(db)
    return render_template('gestionar_rotacion.html', opcionesP=opcionesP, opcionesL=opcionesL)

@app.route('/rotarlote', methods=['POST'])
def rotarlote():
    try:
        opcion_seleccionada = request.form.get('lote')
        opcion_seleccionadap = request.form.get('potrero')
        print("Opción seleccionada:", opcion_seleccionada)
        print("Opción seleccionada:", opcion_seleccionadap)


        consulta = ModelPotreros.mostrar(db, opcion_seleccionada)
        print("Consulta:", consulta)

        # Verificar si hay resultados en la consulta
        if consulta:
            idpotrero = opcion_seleccionadap
            idlote = opcion_seleccionada

            cursor = db.connection.cursor()
            sql = '''SELECT idpotrero FROM lotes WHERE idpotrero = %s '''
            cursor.execute(sql, (idpotrero,))
            tubo = cursor.fetchone()
            print(tubo)

            if tubo:
                flash('El potrero esta Ocupado revisa las salidas')
                return render_template('gestionar_rotacion.html')
            else:
                sqlall = "SELECT * FROM potreros WHERE idpotrero = %s"
                cursor.execute(sqlall, (idpotrero,))
                potrerosel = cursor.fetchall()
                sqlidpotreroocupante = '''SELECT idpotrero FROM lotes WHERE idlote = %s '''
                cursor.execute(sqlidpotreroocupante, (idlote,))
                ptrocu = cursor.fetchone()
                if ptrocu:
                    potreroid = ptrocu[0]  
                    potrero = potreroid
                    sqls = 'UPDATE `potreros` SET `estado`= "Descanso/Recuperacion" WHERE idpotrero = %s'
                    cursor.execute(sqls, (potrero,))
                    print(potrero)
                else:
                    print("No se encontraron resultados para la consulta.")

                rt = ModelLote.rotar(db, idpotrero, idlote)
                flash('potrero en consumo')
                return render_template('gestionar_rotacion.html', potrerosel=potrerosel)

        else:
            return jsonify({"error": "No se encontraron resultados para la opción seleccionada"}), 404
       

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500  # Devuelve un código de estado 500 para indicar un error interno del servidor
@app.route('/mostrarinfo', methods=['GET', 'POST'])
@login_required
def mostrarinfo():
    potreroselec = request.args.get('potrero')
    holi = potreroselec
    obtdatos = ModelPotreros.mostrar(db, holi)
    if obtdatos:
        zona = obtdatos[0][0]
        estado = obtdatos[0][1]
        print(f"Esti misti xini¡{zona} , {estado}")
        return jsonify({'zona': zona, 'estado': estado})
    else:
        print("No mostrar")
        return jsonify({'error': 'No se encontraron datos'})

@app.route('/info_gestion')
@login_required
def info_gestion():
    return render_template('gestion.html')


""" End Code Potreros Create """



@app.route('/home')
@login_required
def home():
    return render_template('admin.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada Por favor Vuelve</h1>", 404



if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(host='0.0.0.0', port=5000)