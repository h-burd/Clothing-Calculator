from flask import Flask, render_template, request
import model

app = Flask(__name__)

result = " "

@app.route('/', methods=('GET', 'POST'))
def home():
    result = " "
    if request.method == 'POST':
        temp = request.form['tempRng']
        wind = request.form['windRng']
        result = model.predict(int(temp), int(wind))
        
    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)