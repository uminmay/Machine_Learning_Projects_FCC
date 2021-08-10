track = {}

def player(prev_play, opponent_history=[]):
    global track

    num = 5

    if prev_play in ["R","P","S"]:
      opponent_history.append(prev_play)

    guess = "R"
    
    if len(opponent_history) > num:
      theinput = "".join(opponent_history[-num:])

      if "".join(opponent_history[-(num+1):]) in track.keys():
        track["".join(opponent_history[-(num+1):])] += 1
      else:
        track["".join(opponent_history[-(num+1):])] = 1
      
      probable = [theinput+"R", theinput+"P", theinput+"S"]

      for i in probable:
        if not i in track.keys():
          track[i] = 0

      prevguess = max(probable, key=lambda key: track[key])

      if prevguess[-1] == "P":
        guess = "S"
      if prevguess[-1] == "R":
        guess = "P"
      if prevguess[-1] == "S":
        guess = "R" 
    return guess
