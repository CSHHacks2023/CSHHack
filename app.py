from flask import Flask, render_template, Response, request, jsonify


app = Flask(__name__)

# Initialize Pygame
# pygame.init()

# Create a Pygame window and surface
# screen = pygame.display.set_mode((800, 800))

# Route to serve the web page
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

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')
# Route to display the Pygame component on a web page
# @app.route('/pygame.html')
# def pygame_component():
#     animation.run_pygame_logic()
#     return "Pygame logic executed successfully"  # Customize the response as needed

if __name__ == '__main__':
    app.run(debug=True)