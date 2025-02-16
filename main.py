# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  game_clock = pygame.time.Clock()
  dt = 0
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
      
    screen.fill((0, 0, 0))

    updatable.update(dt)
    for item in drawable:
      item.draw(screen)

    pygame.display.flip()
    dt = game_clock.tick(60)
    dt = dt / 1000

if __name__ == "__main__":
    main()