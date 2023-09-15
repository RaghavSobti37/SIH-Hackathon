import pygame
import random
import string

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT_SIZE = 72
MAX_ALPHABETS = 5

# Create a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alphabet Typing Game")

# Function to generate a random alphabet and color
def generate_random_alphabet_color():
    random_alphabet = random.choice(string.ascii_uppercase)
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return random_alphabet, random_color

# Initialize variables
alphabet_list = [generate_random_alphabet_color() for _ in range(MAX_ALPHABETS)]
font = pygame.font.Font(None, FONT_SIZE)
correct_count = 0

# Main game loop
running = True
current_index = 0  # Index of the current alphabet in the list

# Instruction text
instruction_font = pygame.font.Font(None, 36)
instruction_text = instruction_font.render("Type the displayed alphabet (uppercase) on your keyboard.", True, WHITE)
instruction_rect = instruction_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if current_index < len(alphabet_list):
                current_alphabet, current_color = alphabet_list[current_index]
                typed_alphabet = event.unicode.upper()
                if typed_alphabet == current_alphabet:
                    correct_count += 1
                    current_index += 1

    screen.fill(WHITE)

    if current_index < len(alphabet_list):
        current_alphabet, current_color = alphabet_list[current_index]

        # Render the current alphabet with randomized color
        text = font.render(current_alphabet, True, current_color)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        # Display the correct count
        correct_text = font.render(f"Score: {correct_count}", True, WHITE)
        screen.blit(correct_text, (10, 10))

        # Render instruction text
        screen.blit(instruction_text, instruction_rect)

    else:
        # Display game over message
        game_over_text = font.render(f"Game Over! Your Score: {correct_count}", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)

    pygame.display.flip()

# Quit pygame
pygame.quit()
