import pygame
from gtts import gTTS
import os
import nltk
from nltk.corpus import cmudict

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((800, 800))

# Load viseme images
viseme_dir = 'visemes'  # Directory containing viseme images
viseme_images = [pygame.image.load(os.path.join(viseme_dir, filename)) for filename in sorted(os.listdir(viseme_dir)) if filename.endswith(".png")]

# Load CMU Pronouncing Dictionary
cmu_dict = cmudict.dict()

# Define a function to map phonemes to viseme images
def map_phoneme_to_viseme(phoneme):
    # Define your mapping logic here
    # Example: 'AA' maps to the first viseme image
    viseme_mapping = {
        'HH': viseme_images[0],
        
        'AH0': viseme_images[0],
        'L': viseme_images[7],
        'OW1': viseme_images[6],
        'M': viseme_images[1],
        'AY1': viseme_images[0],
        'N': viseme_images[7],
        'EY1': viseme_images[0],
        'IH1' : viseme_images[0],
        'Z' : viseme_images[2],
        'AE': viseme_images[0],
        'MBP': viseme_images[1],
        'TS': viseme_images[2],
        'WR': viseme_images[3],
        'UQ': viseme_images[4],
        'FV': viseme_images[5],
        'O': viseme_images[6],
        'LN': viseme_images[7],
        # Add more mappings as needed
    }
    # Return the corresponding viseme image or a default image if not found
    return viseme_mapping.get(phoneme, viseme_images[0])


# Create a function to display a viseme image
def display_viseme(viseme_image):
    print(viseme_image)
    resized_image = pygame.transform.scale(viseme_image, (800, 800))  # Resize the image
    screen.fill((255, 255, 255))  # Clear the screen
    screen.blit(resized_image, (0, 0))  # Display the resized image
    pygame.display.flip()

# Create a function to animate the face based on phonemes
def animate_face(phoneme_sequence):
    for phoneme in phoneme_sequence:
        # Map phoneme to viseme and display corresponding viseme image
        print("phoneme" + phoneme)
        viseme_image = map_phoneme_to_viseme(phoneme)
        display_viseme(viseme_image)
        pygame.time.delay(155)  # Adjust the delay to control animation speed
# Create a function to speak text, convert to phonemes, and animate visemes
def speak_and_animate(text):
    # Generate speech using gTTS
    tts = gTTS(text)
    tts.save("output.mp3")

    # Play the audio
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    # Convert text to phonemes
    phoneme_sequence = text_to_phonemes(text)

    # Animate the face based on phonemes
    animate_face(phoneme_sequence)

    # Wait for the speech to finish
    pygame.mixer.music.queue("output.mp3")

    pygame.quit()

# Define a function to convert text to phonemes
def text_to_phonemes(text):
    text = text.lower()  # Convert text to lowercase
    words = nltk.word_tokenize(text)
    phoneme_sequence = []

    for word in words:
        if word in cmu_dict:
            phonemes = cmu_dict[word][0]
            phoneme_sequence.extend(phonemes)
    print("sequenc" + str(phoneme_sequence))
    return phoneme_sequence

# Example usage:
text_to_speak = "Hello, my name is EcoBuddy! Nice to meet you"
speak_and_animate(text_to_speak)