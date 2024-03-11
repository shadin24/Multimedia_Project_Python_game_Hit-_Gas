import pygame

# Initialize Pygame and Pygame mixer
pygame.init()
pygame.mixer.init()

# Load the background music
pygame.mixer.music.load("gas.mp3")

# Set up the window
WIDTH, HEIGHT = 820, 800  # Adjust these values as needed
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome")

# Font for the buttons
font = pygame.font.SysFont("comicsans", 48)

# Button colors
button_color = (0, 0, 0)
button_text_color = (255, 255, 0)

# Load the background image
background_image = pygame.image.load("imgs/home.png")

# Create button surfaces
start_button = font.render("Start Game", True, button_text_color, button_color)
start_button_rect = start_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
exit_button = font.render("Exit", True, button_text_color, button_color)
exit_button_rect = exit_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

# Play the background music on loop
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                exec(open("main.py").read())  # Run the game script
            elif exit_button_rect.collidepoint(event.pos):
                running = False

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    # Draw the buttons
    screen.blit(start_button, start_button_rect)
    screen.blit(exit_button, exit_button_rect)

    pygame.display.flip()

pygame.quit()