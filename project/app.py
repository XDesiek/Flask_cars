# import os

# from flask import Flask, redirect, render_template, request, url_for
# from flask_bootstrap import Bootstrap
# from flask_mail import Mail, Message
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func

# # main confing & everything
# #---------------------------------------------------------------------------------------
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# bootstrap = Bootstrap(app)
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'cars_database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'testflask8@gmail.com'
# app.config['MAIL_PASSWORD'] = 'aoil nuek myvn nnuc'
# app.config['MAIL_USE_TLS'] = True


# db = SQLAlchemy(app)
# mail = Mail(app)
# migrate = Migrate(app, db)
# #---------------------------------------------------------------------------------------
# # models
# class Car(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     owner = db.Column(db.Integer, db.ForeignKey("owner.id") ,nullable  = False)
#     model= db.Column(db.String(100), nullable  = False)
#     producer= db.Column(db.String(100), nullable  = False)
#     production_year = db.Column(db.Integer, nullable  = False)
#     horsepower = db.Column(db.Integer, nullable  = False)
#     drive= db.Column(db.String(100), nullable  = False)
#     fuel= db.Column(db.String(100), nullable  = False)
#     color= db.Column(db.String(100), nullable  = False)
#     gearbox= db.Column(db.String(100), nullable  = False)


#     def __repr__ (self):
#         return f"{self.producer} {self.model}"


# class Owner(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(100), nullable  = False)
#     surname = db.Column(db.String(100), nullable  = False)
#     email= db.Column(db.String(100), nullable  = False)
#     def __repr__ (self):
#         return f"{self.name} {self.surname}"
    

# #---------------------------------------------------------------------------------------
# # urls
# @app.route("/")
# def carlist():
#     cars = Car.query.all()
#     return render_template("carlist.html",cars=cars)



# @app.route('/create/', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         model = request.form['model']
#         producer = request.form['producer']
#         production_year = int(request.form['production_year'])
#         horsepower = int(request.form['horsepower'])
#         drive = request.form['drive']
#         fuel = request.form['fuel']
#         color = request.form['color']
#         gearbox = request.form['gearbox']
#         owner = request.form['owner']
#         car = Car(model=model,
#                   producer=producer,
#                   production_year=production_year,
#                   horsepower=horsepower,
#                   drive=drive,
#                   fuel=fuel,
#                   color=color,
#                   gearbox=gearbox,
#                   owner=owner)

#         db.session.add(car)
#         db.session.commit()

#         return redirect(url_for('carlist'))  
#     return render_template('create.html')


# @app.route('/create_owner/', methods=('GET', 'POST'))
# def create_owner():
#     if request.method == 'POST':
#         name = request.form['name']
#         surname = request.form['surname']
#         email = request.form['email']

#         new_owner = Owner(name=name, surname=surname, email=email)

#         db.session.add(new_owner)
#         db.session.commit()

#         return redirect(url_for('carlist'))  # Redirect to the owner list page after adding the owner
#     return render_template('create_owner.html')


# @app.route('/details/<int:car_id>/')
# def details(car_id):
#     car = Car.query.get_or_404(car_id)
#     return render_template('details.html', car=car)







# @app.route('/details/<int:car_id>/edit/', methods=('GET', 'POST'))
# def edit(car_id):
#     car = Car.query.get_or_404(car_id)

#     if request.method == 'POST':
#         car.model = request.form['model']
#         car.producer = request.form['producer']
#         car.production_year = int(request.form['production_year'])
#         car.horsepower = int(request.form['horsepower'])
#         car.drive = request.form['drive']
#         car.fuel = request.form['fuel']
#         car.color = request.form['color']
#         car.gearbox = request.form['gearbox']
#         car.owner = int(request.form['owner'])
#         db.session.add(car)
#         db.session.commit()
#         return redirect(url_for('carlist'))

#     return render_template('edit.html', car=car)


# @app.post('/details/<int:car_id>/delete/')
# def delete(car_id):
#     car = Car.query.get_or_404(car_id)
#     print(car)
#     db.session.delete(car)
#     db.session.commit()
#     return redirect(url_for('carlist'))



# @app.route("/details/<int:car_id>/share/")
# def share(car_id):
#     car = Car.query.get_or_404(car_id)
#     owner = Owner.query.get_or_404(car_id)
#     msg = Message('Check out this Car!', sender = owner.email, recipients = ['tony.j.kamisnki.work@gmail.com'])
#     msg.body = f"{car.model} , {car.producer}"
#     mail.send(msg)
#     return "Message sent!"
# ##---------------------------------------------------------------------------------------
# # startapp
# if __name__ == "__main__":
#     app.run(debug=True)












# # baza danych o samochodach 
# # postac tabeli
# # w pierrw szym wierszu dane rozpoznawcze  (id nazwa)
# # maja byc przyciski do detali samochodow
# # przyciski delete i edit




# #    from app import db, Car,Owner

# #    # Create three instances of the Car model
# # car1 = Car(model='A4', producer='Audi', production_year=2020, horsepower=150, drive='Front-wheel drive', fuel='Gasoline', color='Red', gearbox='Automatic', owner='1')

# # car2 = Car(model='3 Series', producer='BMW', production_year=2020, horsepower=150, drive='Front-wheel drive', fuel='Gasoline', color='Red', gearbox='Automatic', owner='1')

# # car3 = Car(model='E-Class', producer='Mercedes-Benz', production_year=2020, horsepower=150, drive='Front-wheel drive', fuel='Gasoline', color='Red', gearbox='Automatic', owner='1')

# # car4 = Car(model='Corolla', producer='Toyota', production_year=2020, horsepower=150, drive='Front-wheel drive', fuel='Gasoline', color='Red', gearbox='Automatic', owner='1')

# # car5 = Car(model='Mustang', producer='Ford', production_year=2020, horsepower=150, drive='Front-wheel drive', fuel='Gasoline', color='Red', gearbox='Automatic', owner='1')

# #    # Add the cars to the database session and commit the changes
# #    db.session.add(car1)
# #    db.session.add(car2)
# #    db.session.add(car3)
# #    db.session.add(car4)
# #    db.session.add(car5)
# #    db.session.commit()
