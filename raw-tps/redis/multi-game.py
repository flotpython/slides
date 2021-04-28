#!/usr/bin/env python
from argparse import ArgumentParser

import pygame as pg
from pygame.locals import QUIT

import redis

from screen import Screen
from player import Player
from others import Others


# xxx need to separate player speed and frame rate
FRAME_RATE = 4

def main():

    parser = ArgumentParser()
    parser.add_argument("-s", "--server", default=None,
                        help="IP adddress for the redis server")
    parser.add_argument("name")
    args = parser.parse_args()

    # player's name as provided on the command line
    local_player_name = args.name
    pg.display.set_caption(f"multi-game: {local_player_name}")


    screen = Screen()
    W, H = screen.size()

    clock = pg.time.Clock()

    redis_server = redis.Redis(args.server)

    player = Player(local_player_name, H, W, redis_server)
    player.join()

    others = Others(redis_server)

    # ask the redis server where the other players are
    players = others.all_players()
    screen.display(players)

    # type 'a' to toggle auto move
    auto_move = False

    while True:
        clock.tick(FRAME_RATE)
        if auto_move:
            player.random_move()
        for event in pg.event.get():
            if (event.type == QUIT or
                (event.type == pg.KEYDOWN and event.key == pg.K_q)):
                player.leave()
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    player.move(0, -1)
                elif event.key == pg.K_DOWN:
                    player.move(0, 1)
                elif event.key == pg.K_RIGHT:
                    player.move(1, 0)
                elif event.key == pg.K_LEFT:
                    player.move(-1, 0)
                elif event.key == pg.K_a:
                    auto_move = not auto_move
        # again, refresh the position of other players
        players = others.all_players()
        # and redisplay accordingly
        screen.display(players)


if __name__ == '__main__':
    main()
