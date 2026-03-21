import pygame

pygame.init()
screen = pygame.display.set_mode((1400, 1300))

cover_fairy_tale = pygame.image.load('cover_fairy_tale.png').convert_alpha()  # Ensure alpha is handled

def recolor_image(image, color):
    """Recolors an image with a given color, using BLEND_MULT."""
    colored_image = image.copy()
    colored_image.fill(color, special_flags=pygame.BLEND_MULT)
    return colored_image

golden_image = recolor_image(cover_fairy_tale, (255, 215, 0))  # Golden color

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(cover_fairy_tale, (50, 50))  # Original image
    screen.blit(golden_image, (200, 50))  # Golden image
    pygame.display.flip()

pygame.quit()
