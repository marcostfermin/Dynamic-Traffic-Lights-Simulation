# -*- coding: utf-8 -*-.
"""
Created on Sun Oct 17 13:15:32 2021.

@author: Marcos Tulio Fermin Lopez
"""

import pygame


def get_traffic_maker():
    # sam = test()
    # print(sam)
    pygame.init()

    # window properties
    WIDTH = 1400
    HEIGHT = 922
    BACK_COLOR = (0, 0, 0)

    default_road = pygame.image.load('images/roads/road1.jpg')
    default_road = pygame.transform.smoothscale(default_road, (1400, 922))

    light_road = pygame.image.load('images/roads/road2.jpg')
    light_road = pygame.transform.smoothscale(light_road, (1400, 922))

    medium_road = pygame.image.load('images/roads/road3.jpg')
    medium_road = pygame.transform.smoothscale(medium_road, (1400, 922))

    heavy_road = pygame.image.load('images/roads/road4.jpg')
    heavy_road = pygame.transform.smoothscale(heavy_road, (1400, 922))

    ring3 = pygame.Rect(600, 290, 220, 70)
    clr3 = (255, 0, 0)

    ring4 = pygame.Rect(600, 420, 220, 70)
    clr4 = (255, 0, 0)

    ring5 = pygame.Rect(600, 550, 220, 70)
    clr5 = (255, 0, 0)

    # -------------------Texts---------------------------------
    table_font = pygame.font.SysFont('timesnewroman', 25, bold=pygame.font.Font.bold)

    light = table_font.render("Light Traffic", True, (255, 255, 255))
    medium = table_font.render("Medium Traffic", True, (255, 255, 255))
    heavy = table_font.render("Heavy Traffic", True, (255, 255, 255))

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # frame rate
    Clock = pygame.time.Clock()

    # convert table to desired size and remove bg

    # ------------------Traffic-------------------------------
    light_traffic = [100, 200, 225, 250]
    medium_traffic = [200, 400, 450, 500]
    heavy_traffic = [400, 800, 900, 1000]

    run = True
    # game starts
    while run:
        # Display screen
        screen.fill((BACK_COLOR))
        # Display table

        if ring3.collidepoint(pygame.mouse.get_pos()):
            screen.blit(light_road, (0, 0))
            clr3 = (0, 255, 0)
        elif ring4.collidepoint(pygame.mouse.get_pos()):
            screen.blit(medium_road, (0, 0))
            clr4 = (0, 255, 0)
        elif ring5.collidepoint(pygame.mouse.get_pos()):
            screen.blit(heavy_road, (0, 0))
            clr5 = (0, 255, 0)
        else:
            screen.blit(default_road, (0, 0))
            clr3 = clr4 = clr5 = (255, 0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        pygame.draw.rect(screen, clr3, ring3, 2, 10)
        pygame.draw.rect(screen, clr4, ring4, 2, 10)
        pygame.draw.rect(screen, clr5, ring5, 2, 10)

        screen.blit(light, (640, 315))
        screen.blit(medium, (620, 440))
        screen.blit(heavy, (630, 570))

        if pygame.mouse.get_pressed()[0] and ring3.collidepoint(pygame.mouse.get_pos()):
            print('light tapped')
            return light_traffic
        if pygame.mouse.get_pressed()[0] and ring4.collidepoint(pygame.mouse.get_pos()):
            print('medium tapped')
            return medium_traffic
        if pygame.mouse.get_pressed()[0] and ring5.collidepoint(pygame.mouse.get_pos()):
            print('heavy tapped')
            return heavy_traffic

        pygame.display.flip()
        Clock.tick(60)


if __name__ == '__main__':
    #    pass
    get_traffic_maker()
