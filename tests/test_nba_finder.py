import pytest

from nba.nba_finder import accessAPI, findPairs

# Prepare players to use
players = accessAPI()

# Get the pair of Tallest stars at 177 Inches combined.
# ----------------------------------------------------
def test_get_really_tall_stars():
    results = findPairs(players, 177)
    assert len(results) == 1
    
# Verify Yao ming is one of the tallest stars
# ----------------------------------------------------
def test_verify_yao_ming_is_one_of_the_two_tallest_stars():
    results = findPairs(players, 177)
    assert results[0]["player_b"]["last_name"] == "Ming"
    assert results[0]["player_b"]["first_name"] == "Yao"
    
# Get the pair of Shortest stars at 139 Inches combined.
# ----------------------------------------------------
def test_get_really_short_stars():
    results = findPairs(players, 139)
    assert len(results) == 2
    
# Verify Brevin Knight is one of the Shortest players
# ----------------------------------------------------
def test_verify_nate_robinson_is_one_of_the_shortest_stars():
    results = findPairs(players, 139)
    assert results[0]["player_b"]["last_name"] == "Robinson"
    assert results[0]["player_b"]["first_name"] == "Nate"
    