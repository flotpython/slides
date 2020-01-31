#!/usr/bin/env python
from argparse import ArgumentParser

import pygame
from pygame.locals import QUIT

import redis

from screen import Screen
from player import Player
from others import Others


# xxx need to separate player speed and frame rate
FRAME_RATE = 10

def main():
    
    parser = ArgumentParser()
    parser.add_argument("-s", "--server", default=None,
                        help="IP adddress for the redis server")
    parser.add_argument("name")
    args = parser.parse_args()
    
    local_player_name = args.name
    
    screen = Screen()
    W, H = screen.size()
    
    clock = pygame.time.Clock()

    redis_server = redis.Redis(args.server)
    
    player = Player(local_player_name, H, W, redis_server)
    others = Others(redis_server)
    player.join()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                player.leave()
                return
        clock.tick(FRAME_RATE)
        player.random_move()
        players = others.all_players()
        screen.display(players)
                    
        
if __name__ == '__main__':
    main()