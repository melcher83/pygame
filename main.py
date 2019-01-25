import pygame

pygame.init()

s_width=500
s_height=500

win = pygame.display.set_mode((s_width,s_height))

pygame.display.set_caption("First Game")

x=50
y=50

width = 40
height = 60
vel = 5

run=True

isJump=False
jumpCount =  10

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()



    if keys[pygame.K_a] and x > vel:
        x -= vel

    if keys[pygame.K_d] and x < s_width - width - vel:
        x += vel

    if not (isJump):
        if keys[pygame.K_w] and y > vel:
            y -= vel

        if keys[pygame.K_s] and y < s_height - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg=1
            if jumpCount < 0:
                neg =-1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount=10




    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()



pygame.quit()



