from flask import Flask, render_template, Response, request, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/carbon')
def carbon():
    return render_template('carbon.html')

@app.route('/news')
def news():
    return render_template('news.html')
  
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)