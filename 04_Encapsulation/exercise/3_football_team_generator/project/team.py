from project.player import Player


class Team:

    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        pass

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)

        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str) -> str or Player:
        try:
            player = next(filter(lambda p: p.name == player_name, self.__players))
        except StopIteration:
            return f"Player {player_name} not found"

        self.__players.remove(player)

        return player

