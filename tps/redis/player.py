import random
import json

def random_color():
    return [random.randint(0, 255) for _ in range(3)]

def random_move():
    moves = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if abs(x+y) == 1]
    return random.choice(moves)



class Player:
    """
    manage the local player, and broadcast
    its position to the redis server
    """

    def __init__(self, name, width, height, redis_server):
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
        self.redis_server = redis_server


    def join(self):
        """
        add local name to database
        with a random color
        """
        self.redis_server.hmset(
            self.name,
            {'color' : json.dumps(self.color),
             'position': json.dumps(self.position),
            })


    def leave(self):
        """
        remove local name from database
        """
        self.redis_server.delete(self.name)


    def random_move(self):
        self.move(*random_move())

    def move(self, dx, dy):
        self.position[0] += dx
        self.position[0] %= self.width
        self.position[1] += dy
        self.position[1] %= self.height
        self.redis_server.hset(self.name, 'position',
                               json.dumps(self.position))
