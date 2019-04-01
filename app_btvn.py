from flask import *
from services_bike import services
from random import randint, choice
app = Flask(__name__)

#Create document
for i in range(10):
  new_bike_update = {
    "model": "honda",
    "daily_fee": randint(10000, 50000),
    "image": "",
    "year": "",
  }
  services.insert_one(new_bike_update)
  # print(new_bike_update)

@app.route('/new_bike', methods=["GET", "POST"])
def new_bike():
  if request.method == "GET":
    return render_template('update_bike.html')
  elif request.method == "POST":
    form = request.form
    model = form["model"]
    daily_fee = form["daily_fee"]
    image = form["image"]
    year = form["year"]

    new_bike_value = {
      'model': model,
      'daily_fee': daily_fee,
      'image': image,
      'year': year,
    }
    services.insert_one(new_bike_value)
    # print(new_bike_value)
    return redirect('/new_bike')

if __name__ == '__main__':
  app.run(debug=True)
 