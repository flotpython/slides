import json

class Others:
    """
    fetch the status of all other players
    """
    def __init__(self, redis_server): 
        # a handle to the redis server
        self.redis_server = redis_server
        
    def all_players(self):
        # xxx need to optimize these multiple round trips
        player_names = self.redis_server.keys()
        players = []
        for player_name in player_names:
            player = self.redis_server.hgetall(player_name)
            for k, v in player.items():
                player[k] = json.loads(v)
            players.append(player)
        return players
