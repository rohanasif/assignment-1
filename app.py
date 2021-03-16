from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))  # path for the app.py file to put the db file here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')  # creating the db file with
# its file name passed as parameter
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '323bc35fe8e7d1'
app.config['MAIL_PASSWORD'] = 'fd8caf8b268449'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)  # database object of the app
ma = Marshmallow(app)  # to make everything json deserializable
jwt = JWTManager(app)  # for token management
mail = Mail(app)  # for mail sending


@app.cli.command('db_create')  # making a command to create database. Use with flask command.
def db_create():
    db.create_all()
    print('Database created!')


@app.cli.command('db_drop')  # same for deleting database
def db_drop():
    db.drop_all()
    print('Database dropped!')


@app.cli.command('db_seed')  # same for seeding database
def db_seed():
    # Creating the planets
    mercury = Planet(planet_name='Mercury',
                     planet_type='Class D',
                     home_star='Sol',
                     mass=3.258e23,
                     radius=1516,
                     distance=35.98e6)

    venus = Planet(planet_name='Venus',
                     planet_type='Class K',
                     home_star='Sol',
                     mass=4.867e24,
                     radius=3760,
                     distance=67.24e6)

    earth = Planet(planet_name='Earth',
                     planet_type='Class M',
                     home_star='Sol',
                     mass=5.972e24,
                     radius=3959,
                     distance=92.96e6)

    # Adding the planets to database
    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)

    # Creating a test user
    test_user = User(first_name='William',
                     last_name='Herschel',
                     email='test@test.com',
                     password='password')

    # Adding users
    db.session.add(test_user)
    db.session.commit()
    print('Database seeded!')


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the API, boo yah')


@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')  # 'name' is the parameter in URL, name is just used as python variable
    age = int(request.args.get('age'))  # same case for 'age' and age
    if age < 18:
        return jsonify(message="Sorry " + name + " you are not old enough")
    else:
        return jsonify(message="Welcome " + name + " you are old enough")


@app.route('/url_variables/<string:name>/<int:age>')  # Direct passing of 'name' and 'age' with their types into URL
def url_variable(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + " you are not old enough")  # no need to create variables!
    else:
        return jsonify(message="Welcome " + name + " you are old enough")


@app.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()  # stores a list of all planets from fetched from the database
    result = planets_schema.dump(planets_list)  # serialized list of planets
    return jsonify(result)


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']  # Store the 'email' entered on the registration form in a variable
    test = User.query.filter_by(email=email).first()  # check if entered email is in database
    if test:
        return jsonify(message='That email already exists.'), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)  # add user to database
        db.session.commit()
        return jsonify(message='User created successfully.'), 201


@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']
    test = User.query.filter_by(email=email, password=password).first()
    if test:
        access_token = create_access_token(identity=email)
        return jsonify(message="Login succeeded", access_token=access_token)
    else:
        return jsonify(message="Bad email or password"), 401


@app.route('/retrieve_password/<string:email>', methods=['GET'])
def retrieve_password(email: str):
    user = User.query.filter_by(email=email).first()
    if user:
        msg = Message('Your password is ' + user.password,
                      sender="admin@planetary-api.com",
                      recipients=[email])
        mail.send(msg)
        return jsonify(message="Password sent to " + email)
    else:
        return jsonify(message="That email doesn't exist"), 401


@app.route('/planet_details/<int:planet_id>', methods=["GET"])
def planet_details(planet_id: int):
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        result = planet_schema.dump(planet)
        return jsonify(result)
    else:
        return jsonify(message="That planet doesn't exist"), 404


@app.route('/add_planet', methods=['POST'])
@jwt_required()
def add_planet():
    planet_name = request.form['planet_name']
    test = Planet.query.filter_by(planet_name=planet_name).first()
    if test:
        return jsonify("There is already a planet by that name"), 409
    else:
        planet_type = request.form['planet_type']
        home_star = request.form['home_star']
        mass = float(request.form['mass'])
        radius = float(request.form['radius'])
        distance = float(request.form['distance'])

        new_planet = Planet(planet_name=planet_name, planet_type=planet_type, home_star=home_star, mass=mass, radius=radius, distance=distance)
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(message="You added a planet"), 201


@app.route('/update_planet', methods=['PUT'])
@jwt_required()
def update_planet():
    planet_id = int(request.form['planet_id'])
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        planet.planet_name = request.form['planet_name']
        planet.planet_type = request.form['planet_type']
        planet.home_star = request.form['home_star']
        planet.mass = request.form['mass']
        planet.radius = request.form['radius']
        planet.distance = request.form['distance']
        db.session.commit()
        return jsonify(message="You updated a planet"), 202
    else:
        return jsonify(message="That planet doesn't exist"), 404


@app.route('/remove_planet/<int:planet_id>', methods=['DELETE'])
@jwt_required()
def remove_planet(planet_id: int):
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return jsonify(message="You deleted a planet."), 202
    else:
        return jsonify(message="That planet doesn't exist"), 404


# database models:
class User(db.Model):  # users table
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Planet(db.Model):  # planets table
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class PlanetSchema(ma.Schema):
    class Meta:
        fields = ('planet_id', 'planet_name','planet_type', 'home_star', 'mass', 'radius', 'distance')


user_schema = UserSchema()  # deserialize a single user object
users_schema = UserSchema(many=True)  # deserialize a collection of users

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)


if __name__ == '__main__':
    app.run(debug=True)