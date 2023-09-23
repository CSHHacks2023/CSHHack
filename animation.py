from gtts import gTTS
import pygame

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((800, 600))

# Define a dictionary mapping visemes to their corresponding image filenames
viseme_images = {
    'Closed': pygame.image.load('closed_mouth.png'),
    'Open': pygame.image.load('open_mouth.png'),
    'Smile': pygame.image.load('smile.png'),
    # Add more mappings as needed
}

# Define a basic phoneme-to-viseme mapping (you should expand this dictionary)
phoneme_to_viseme = {
    'HH': 'Closed',
    'EH': 'Open',
    'L': 'Smile',
    'OW': 'Open',
    # Add more mappings as needed
}

# Create a function to map phonemes to visemes
def map_phonemes_to_visemes(phonemes):
    visemes = []
    for phoneme in phonemes.split():
        if phoneme in phoneme_to_viseme:
            visemes.append(phoneme_to_viseme[phoneme])
    return visemes

# Create a function to animate the face based on visemes
def animate_face(visemes):
    running = True
    clock = pygame.time.Clock()
    current_frame = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the current viseme image on the screen
        current_viseme = visemes[current_frame]
        screen.blit(viseme_images[current_viseme], (0, 0))

        pygame.display.flip()
        pygame.time.delay(500)  # Adjust the delay to control animation speed

        current_frame += 1
        if current_frame >= len(visemes):
            current_frame = 0

        clock.tick(10)  # Limit the frame rate

    pygame.quit()

# Create a function to speak text and animate visemes
def speak_and_animate(text):
    # Generate speech using gTTS
    tts = gTTS(text)
    tts.save("output.mp3")

    # Load the audio
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")

    # Map phonemes to visemes
    phonemes = tts.phonemes
    visemes = map_phonemes_to_visemes(phonemes)

    # Start audio playback
    pygame.mixer.music.play()

    # Animate the face
    animate_face(visemes)

    # Wait for the speech to finish
    pygame.mixer.music.queue("output.mp3")  # Ensure that the audio finishes playing

    pygame.quit()

# Example usage:
text_to_speak = "Hello, I am a talking face!"
speak_and_animate(text_to_speak)
