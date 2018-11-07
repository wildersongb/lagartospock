def rps(p1, p2):
    hand = {
      'piedra':['tijera','lagarto'], 
      'papel':['spock','piedra'],
      'tijera':['lagarto','papel'],
      'lagarto':['spock','papel'],
      'spock':['tijera','piedra'],
    }
    if p1 and p2 in hand:
      if p1==p2:
        return 'Draw'
      else:
        if p1 in hand[p2]:
          return'Player 2 won!'
        else:
          return'Player 1 won'
    else:
      return rps(input('Player 1 '), input('Player 2 '))

print(rps(input('Player 1 '), input('Player 2 ')))
