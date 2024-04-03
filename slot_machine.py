import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define symbols
SYMBOLS = ["Cherry", "Orange", "Plum", "Bell", "Melon", "Bar", "Seven"]

# Load symbol images
symbol_images = {symbol: pygame.transform.scale(pygame.image.load(f"{symbol.lower()}.png"), (50, 50)) for symbol in SYMBOLS}

# Initialize font
pygame.font.init()
font = pygame.font.SysFont(None, 24)

class SlotMachine:
    def __init__(self):
        self.balance = 1000
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Slot Machine Game")
        self.font = pygame.font.SysFont(None, 24)  # Font for displaying messages

    def pull_lever(self):
        if self.balance < 5:
            self.display_message("Insufficient balance to play.")
            return

        self.balance -= 5

        symbols = [random.choice(SYMBOLS) for _ in range(3)]
        self.display_symbols(symbols)

        if symbols.count(symbols[0]) == 3:
            self.display_message("Jackpot! You won $100.")
            self.balance += 100
        elif symbols.count(symbols[0]) == 2:
            self.display_message("Two of a kind! You won $10.")
            self.balance += 10
        else:
            self.display_message("Try again! You didn't win anything.")

        print(f"Balance: ${self.balance}")

    def display_message(self, message):
        text_surface = self.font.render(message, True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        time.sleep(2)  # Display the message for 2 seconds


    def display_symbols(self, symbols):
        print("Spinning...")
        print("Symbols:", symbols)
        print("Symbol images keys:", symbol_images.keys())

        # Create three surfaces for each symbol
        symbol_surfaces = [symbol_images[symbol] for symbol in symbols]
        symbol_positions = [(SCREEN_WIDTH // 4 * (i + 1), SCREEN_HEIGHT // 2) for i in range(3)]

        # Define spin duration and frame delay
        spin_duration = 2  # seconds
        frame_delay = 0.1  # seconds

        # Spin animation loop
        start_time = time.time()
        frame_index = 0
        while time.time() - start_time < spin_duration:
            # Clear the screen
            self.screen.fill(BLACK)

            # Blit the symbols onto the screen with an offset
            for i in range(3):
                symbol_surface = symbol_surfaces[(frame_index + i) % len(symbol_surfaces)]
                self.screen.blit(symbol_surface, (symbol_positions[i][0] - symbol_surface.get_width() // 2,
                                                  symbol_positions[i][1] - symbol_surface.get_height() // 2))

            pygame.display.update()  # Update the display
            time.sleep(frame_delay)
            frame_index += 1

        # Display the final result
        self.screen.fill(BLACK)  # Clear the screen
        for i in range(3):
            symbol_surface = symbol_images[symbols[i]]
            self.screen.blit(symbol_surface, (symbol_positions[i][0] - symbol_surface.get_width() // 2,
                                               symbol_positions[i][1] - symbol_surface.get_height() // 2))
        pygame.display.flip()  # Update the display


def main():
    slot_machine = SlotMachine()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    slot_machine.pull_lever()
                elif event.key == pygame.K_q:
                    running = False

if __name__ == "__main__":
    main()
