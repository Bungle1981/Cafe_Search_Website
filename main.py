from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import NewCafeForm, SearchForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #prevents some warnings
db = SQLAlchemy(app)
Bootstrap(app)
app.secret_key = "BlahBlahBlah"

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_toilet = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    can_take_calls = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Cafe {self.name}>'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST", "GET"])
def addCafe():
    AddCafeForm = NewCafeForm(Price="£")
    if request.method == "POST":
        Sockets = 0
        Toilets = 0
        Wifi = 0
        Calls = 0
        if AddCafeForm.Socket.data == "Yes":
            Sockets = 1
        if AddCafeForm.Toilet.data == "Yes":
            Toilets = 1
        if AddCafeForm.WiFi.data == "Yes":
            Wifi = 1
        if AddCafeForm.Calls.data == "Yes":
            Calls = 1
        new_cafe = Cafe(name=AddCafeForm.Cafename.data,
                        map_url=AddCafeForm.Mapurl.data,
                        img_url=AddCafeForm.Imageurl.data,
                        location=AddCafeForm.Location.data,
                        has_sockets=Sockets,
                        has_toilet=Toilets,
                        has_wifi=Wifi,
                        can_take_calls=Calls,
                        seats=AddCafeForm.Seats.data,
                        coffee_price=AddCafeForm.Price.data)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('Newcafe.html', form=AddCafeForm)

@app.route('/search', methods=["GET", "POST"])
def SearchCafe():
    search_form = SearchForm()
    if request.method == "POST":
        # search_form.Location.data != "":
        print(search_form.Location.data)
        cafes = db.session.query(Cafe).filter_by(location=search_form.Location.data).all()
        for cafe in cafes:
            print (cafe)
        return render_template('Results.html', cafes=cafes)
    return render_template('Search.html', form=search_form)

@app.route('/all')
def showAll():
    all_cafes = db.session.query(Cafe)
    return render_template('Results.html', cafes=all_cafes)

@app.route('/Delete')
def DeleteCafe():
    cafeid = request.args.get("id")
    cafetodelete = Cafe.query.get(cafeid)
    db.session.delete(cafetodelete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
