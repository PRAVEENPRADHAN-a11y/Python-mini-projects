import random
# roll generator
def roll():
  min=1
  max=6
  roll=random.randint(min,max)
  return roll
# no of players 
while True:
  players=input("enter number of players(2-4)")
  if players.isdigit():
    players=int(players)
    if 2<=players<=4:
      break
    else:
      print("players should be in between (2-4)")
  else:
    print("invalid input for players")
# the whole pig game logic
max_score=20
player_scores=[0 for _ in range(players)]
while max(player_scores)<max_score:
  for player_idx in range(players):
    current_score=0
    print(f"player {player_idx+1} its your turn!")
    print("your current score is",player_scores[player_idx])
    while True:
      iroll=input("wanna roll a dice(y/n)?")
      if iroll.lower()=='n':
        break
      value=roll()
      if value==1:
        print("you got a 1 sorry you lost!")
        current_score=0
        break
      else:
        print("yo! you got a ",value)
        current_score+=value
    print("you current score was", current_score)
    player_scores[player_idx]+=current_score
    print(f"your total score is {player_scores[player_idx]}")
winning_idx=player_scores.index(max(player_scores))
print(f"congratulations ðŸŽ‰ player {winning_idx+1} has won this game with a total score of {player_scores[winning_idx]} ")