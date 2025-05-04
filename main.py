import pygame

pygame.init()

window = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()
background_img = pygame.image.load("background2.png.")
background_img = pygame.transform.scale(background_img, [700, 500])


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill([104, 1, 14])
    window.blit(background_img, [0, 0])
    pygame.display.flip()


    clock.tick(60)


