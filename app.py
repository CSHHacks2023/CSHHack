from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tab1')
def tab1():
    return render_template('tab1.html')

@app.route('/tab2')
def tab2():
    return render_template('tab2.html')

@app.route('/tab3')
def tab3():
    return render_template('tab3.html')

if __name__ == '__main__':
    app.run(debug=True)
