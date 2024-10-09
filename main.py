import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import * 

def main():
    #initilization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    #Asteroid
    Asteroid.containers = (asteroids, updatable, drawable)

    #Asteroid Field
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    #Shots
    Shot.containers = (shots, updatable, drawable)

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("#000000")
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game Over!")
                sys.exit()
                
            for shot in shots:
                if asteroid.detect_collision(shot):
                    shot.kill()
                    asteroid.split()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()