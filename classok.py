class Player:
    def __init__(self, playerName, kills, deaths):
        self.name = playerName
        self.kills = kills
        self.deaths = deaths

    def record(self, type, amount:int=0):
        if type == "kill":
            self.kills += amount 
        elif type == "death":
            self.deaths += 1
        

player_1 = Player('KrumplisSrác', 0, 0)
print(player_1.name)

player_1.record("kill", 4)

print(type(player_1))
