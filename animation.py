import pygame
from gtts import gTTS
import os
import nltk
from nltk.corpus import cmudict
import openai
# Initialize Pygame
api_key = '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'
openai.api_key = api_key

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
        'HH1': viseme_images[0],
        'AA1': viseme_images[0],
        'AH1': viseme_images[0],
        'AO1': viseme_images[8],
        'AW1': viseme_images[9],
        'AY1': viseme_images[4],
        'B1': viseme_images[1],
        'CH1': viseme_images[3],
        'D1': viseme_images[2],
        'DH1': viseme_images[2],
        'EH1': viseme_images[0],
        'ER1': viseme_images[2],
        'EY1': viseme_images[4],
        'F1': viseme_images[5],
        'G1': viseme_images[2],
        'IH1': viseme_images[0],
        'IY1': viseme_images[4],
        'JH1': viseme_images[3],
        'K1': viseme_images[2],
        'NG1': viseme_images[7],
        'OW1': viseme_images[8],
        'OY1': viseme_images[9],
        'P1': viseme_images[1],
        'R1': viseme_images[3],
        'S1': viseme_images[2],
        'SH1': viseme_images[3],
        'T1': viseme_images[2],
        'TH1': viseme_images[10],
        'UH1': viseme_images[11],
        'UW1': viseme_images[11],
        'V1': viseme_images[5],
        'W1': viseme_images[9],
        'Y1': viseme_images[2],

   
        'HH': viseme_images[0],
        'AA': viseme_images[0],
        'AH': viseme_images[0],
        'AO': viseme_images[8],
        'AW': viseme_images[9],
        'AY': viseme_images[4],
        'B': viseme_images[1],
        'CH': viseme_images[3],
        'D': viseme_images[2],
        'DH': viseme_images[2],
        'EH': viseme_images[0],
        'ER': viseme_images[2],
        'EY': viseme_images[4],
        'F': viseme_images[5],
        'G': viseme_images[2],
        'IH': viseme_images[0],
        'IY': viseme_images[4],
        'JH': viseme_images[3],
        'K': viseme_images[2],
        'NG': viseme_images[7],
        'OW': viseme_images[8],
        'OY': viseme_images[9],
        'P': viseme_images[1],
        'R': viseme_images[3],
        'S': viseme_images[2],
        'SH': viseme_images[3],
        'T': viseme_images[2],
        'TH': viseme_images[10],
        'UH': viseme_images[11],
        'UW': viseme_images[11],
        'V': viseme_images[5],
        'W': viseme_images[9],
        'Y': viseme_images[2],

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
        pygame.time.delay(500)  # Adjust the delay to control animation speed
# Create a function to spea0k text, convert to phonemes, and animate visemes
def speak_and_animate(text):
    tts = gTTS(text, lang='en')    # Generate speech using gTTS
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
text_to_speak = "Hello my name is Eco Buddy"
speak_and_animate(text_to_speak)