import random
import json

import redis

def random_color():
    return [random.randint(0, 255) for _ in range(3)]

def random_move():
    moves = [ (x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x * y]
    return random.choice(moves)



class Player:
    
    def __init__(self, name, width, height):
        """
        name is the name of the local player
        """
        self.name = name
        self.width = width
        self.height = height
        self.position = [ random.randint(0, self.width-1),
                          random.randint(0, self.height-1)]
        self.color = random_color()
        #
        self._redis = redis.Redis()


    def join(self):
        """
        add local name to database
        with a random color
        """
        position = 0, 0
        self._redis.hmset(self.name, 
                         {'color' : json.dumps(self.color),
                          'position': json.dumps(position),
                         })


    def leave(self):
        """
        remove local name from database
        """
        self._redis.delete(self.name)
        
    
    def random_move(self):
        self.move(*random_move())
    
    def move(self, dx, dy):
        self.position[0] += dx
        self.position[0] %= self.width
        self.position[1] += dy
        self.position[1] %= self.height
        self._redis.hset(self.name, 'position',
                        json.dumps(self.position))
        

    def all_players(self):
        # xxx need to optimize these multiple round trips
        player_names = self._redis.keys()
        players = []
        for player_name in player_names:
            player = self._redis.hgetall(player_name)
            for k, v in player.items():
                player[k] = json.loads(v)
            players.append(player)
        return players

