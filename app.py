from flask import Flask, render_template, request, url_for, redirect
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/predict', methods=['GET','POST'])
def predict():
    model = pickle.load(open('model.pkl','rb'))
    if request.method == "POST":
        name = request.form['tweet']
        

        features = np.array([])
        tweet_status = model.predict([features])
        msg = ""
        print(type(tweet_status))
        return render_template('index.html', tweet_status = tweet_status, f_name=name)
    else: 
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)