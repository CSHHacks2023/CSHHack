from flask import Flask, render_template, Response
import pygame
import animation
import io

app = Flask(__name__)

# Initialize Pygame
pygame.init()

# Create a Pygame window and surface
screen = pygame.display.set_mode((800, 800))

# Route to serve the web page
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

# Route to display the Pygame component on a web page
@app.route('/pygame.html')
def pygame_component():
    animation.run_pygame_logic()
    return "Pygame logic executed successfully"  # Customize the response as needed

if __name__ == '__main__':
    app.run(debug=True)