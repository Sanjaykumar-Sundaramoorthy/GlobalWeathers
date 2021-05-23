import requests
from flask import Flask , render_template,request

app = Flask(__name__)
 

def getWeather(city):
    r = requests.get(f"https://goweather.herokuapp.com/weather/{city}")
    return r.json()
@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        weather = getWeather(city)
        return render_template('index.html',weather=weather,city=city)

    return render_template("index.html")

    
if __name__ == '__main__':
    app.debug = True
    app.run()


