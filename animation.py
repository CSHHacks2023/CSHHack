import pygame
from gtts import gTTS
import os

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((800, 600))

# Load viseme images
viseme_images = []
viseme_dir = 'visemes'  # Directory containing viseme images
for filename in sorted(os.listdir(viseme_dir)):
    if filename.endswith(".png"):
        viseme_image = pygame.image.load(os.path.join(viseme_dir, filename))
        print(f"Loaded image: {filename}")
        viseme_images.append(viseme_image)
        print(viseme_images)


# Create a function to display a viseme image
def display_viseme(viseme_image):
    print("Displaying viseme image")
    resized_image = pygame.transform.scale(viseme_image, (800, 600))  # Resize the image
    screen.fill((255, 255, 255))  # Clear the screen
    screen.blit(resized_image, (0, 0))  # Display the resized image
    pygame.display.flip()
# Create a function to animate the face
def animate_face(viseme_images):
    for viseme_image in viseme_images:
        display_viseme(viseme_image)
        pygame.time.delay(500)  # Adjust the delay to control animation speed

# Create a function to speak text and animate visemes
def speak_and_animate(text):
    # Generate speech using gTTS
    tts = gTTS(text)
    tts.save("output.mp3")

    # Play the audio
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    # Animate the face
    animate_face(viseme_images)

    # Wait for the speech to finish
    pygame.mixer.music.queue("output.mp3")

    pygame.quit()

# Example usage:
text_to_speak = "Hello, I am a talking face!"
speak_and_animate(text_to_speak)

# viseme_mapping = {
#     'Open': pygame.image.load('images/AE.png'),
#     'FFFF': pygame.image.load('images/FV.png'),
#     'Em': pygame.image.load('images/MBP.png'),
#     'Ow': pygame.image.load('images/O.png'),
#     'ST': pygame.image.load('images/TS.png'),
#     'Cute': pygame.image.load('images/UQ.png'),
#     'Were': pygame.image.load('images/WR.png')
#     # Add more mappings as needed
# }


