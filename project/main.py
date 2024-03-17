from flask import Blueprint, redirect, render_template, request, url_for

from . import db
from .models import Car, User

main = Blueprint('main', __name__)



@main.route("/")
def carlist():
    cars = Car.query.all()
    return render_template("main/carlist.html",cars=cars)



@main.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        model = request.form['model']
        producer = request.form['producer']
        production_year = int(request.form['production_year'])
        horsepower = int(request.form['horsepower'])
        drive = request.form['drive']
        fuel = request.form['fuel']
        color = request.form['color']
        gearbox = request.form['gearbox']
        owner = request.form['owner']
        car = Car(model=model,
                  producer=producer,
                  production_year=production_year,
                  horsepower=horsepower,
                  drive=drive,
                  fuel=fuel,
                  color=color,
                  gearbox=gearbox,
                  owner=owner)

        db.session.add(car)
        db.session.commit()

        return redirect(url_for('main.carlist'))  
    return render_template('main/create.html')


# @main.route('/create_owner/', methods=('GET', 'POST'))
# def create_owner():
#     if request.method == 'POST':
#         name = request.form['name']
#         surname = request.form['surname']
#         email = request.form['email']

#         new_owner = Owner(name=name, surname=surname, email=email)

#         db.session.add(new_owner)
#         db.session.commit()

#         return redirect(url_for('main.carlist'))  # Redirect to the owner list page after adding the owner
#     return render_template('main/create_owner.html')


@main.route('/details/<int:car_id>/')
def details(car_id):
    car = Car.query.get_or_404(car_id)
    return render_template('main/details.html', car=car)







@main.route('/details/<int:car_id>/edit/', methods=('GET', 'POST'))
def edit(car_id):
    car = Car.query.get_or_404(car_id)

    if request.method == 'POST':
        model = request.form['model']
        producer = request.form['producer']
        production_year = int(request.form['production_year'])
        horsepower = int(request.form['horsepower'])
        drive = request.form['drive']
        fuel = request.form['fuel']
        color = request.form['color']
        gearbox = request.form['gearbox']
        owner = int(request.form['owner'])
        car = Car(model=model,
                  producer=producer,
                  production_year=production_year,
                  horsepower=horsepower,
                  drive=drive,
                  fuel=fuel,
                  color=color,
                  gearbox=gearbox,
                  owner=owner)
        db.session.add(car)
        db.session.commit()
        return redirect(url_for('main.carlist'))

    return render_template('main/edit.html', car=car)


@main.post('/details/<int:car_id>/delete/')
def delete(car_id):
    car = Car.query.get_or_404(car_id)
    print(car)
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for('main.carlist'))



# @app.route("/details/<int:car_id>/share/")
# def share(car_id):
#     car = Car.query.get_or_404(car_id)
#     owner = Owner.query.get_or_404(car_id)
#     msg = Message('Check out this Car!', sender = owner.email, recipients = ['tony.j.kamisnki.work@gmail.com'])
#     msg.body = f"{car.model} , {car.producer}"
#     mail.send(msg)
#     return "Message sent!"