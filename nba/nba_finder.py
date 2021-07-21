import requests
import sys
# SO, lets create a function to access the API
# Also lets create a function to find pairs of players
# Finally create a summoning function

def accessAPI():
    # Gets a request summoning
    # returns the list of NBA Players
    response = requests.get('https://mach-eight.uc.r.appspot.com/')
    data = response.json()
    return data["values"]

def findPairs(listOfPlayers, height: int):
    # Navigate the list of players
    # Take current player, go to each next player after him
    # sum both players, if sum of heights is equal to value, add pair to return list
    # repeat for each player after selected player
    i = 0
    result = []
    while i < len(listOfPlayers) - 1:
        j = i + 1
        while j < len(listOfPlayers):
            player_a = listOfPlayers[i]
            player_b = listOfPlayers[j]
            value = int(player_a["h_in"]) + int(player_b["h_in"])
            if value == height:
                result.append({
                    "player_a": player_a,
                    "player_b": player_b
                })
            j = j + 1
        i = i + 1
    if len(result) > 0: 
        return result 
    else:
        return "No matches found" 


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) < 2:
        print("::Error:: height is required. Use python nba_finder.py _height_")
    else:
        players = accessAPI()
        expected_height = int(sys.argv[1])
        print(f"Getting players with height of {expected_height}:", findPairs(players, expected_height))
 