# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  game_clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  AsteroidField.containers = (updatable,)
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  Shot.containers = (shots, updatable, drawable)

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
  asteroidfield = AsteroidField()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
      # elif event.type == pygame.KEYDOWN:  # Add this check
      #   if event.key == pygame.K_SPACE:
      #       player.shoot()
      
    screen.fill((0, 0, 0))

    updatable.update(dt)
    for item in drawable:
      item.draw(screen)

    for asteroid in asteroids:
       if player.collision(asteroid) == True:
          print("Game over!")
          sys.exit()

    for shot in shots:
       shot.draw(screen)
          
    pygame.display.flip()
    dt = game_clock.tick(60)
    dt = dt / 1000

if __name__ == "__main__":
    main()