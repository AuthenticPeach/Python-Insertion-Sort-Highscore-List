class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def insertion_sort_ranking(players, new_player):
    # Add the new player to the end of the list
    players.append(new_player)
    
    # Perform Insertion Sort to maintain the ranking
    for i in range(1, len(players)):
        key = players[i]
        j = i - 1
        
        while j >= 0 and key.score > players[j].score:
            players[j + 1] = players[j]
            j -= 1
        
        players[j + 1] = key

# Initialize an empty list for the player ranking
players_ranking = []

# Prompt the user to input player names and scores
num_players = int(input("Enter the number of players: "))

for i in range(num_players):
    name = input(f"Enter the name of Player {i + 1}: ")
    score = int(input(f"Enter the score of Player {i + 1}: "))
    player = Player(name, score)
    insertion_sort_ranking(players_ranking, player)

# Display the updated player ranking
print("\nPlayer Ranking:")
for player in players_ranking:
    print(f"{player.name}: {player.score}")
