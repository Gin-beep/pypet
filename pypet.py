print ('Welcome to Pypet!')

fish = {
  'name': 'Sir Patrick',
  'age': 112,
  'weight': 5.3,
  'hungry': True,
  'bored': True,
  'photo': '<`)))><'
}

mouse = {
    'name': 'Mouse',
    'age': 6,
    'weight': 1.5,
    'hungry': False,
    'bored': True,
    'photo': '<:3 )~~~~',
}

print ('Hello '+fish['name'])
print (fish['photo'])

def feed(pet):
  if pet['hungry'] == True:
    pet['hungry'] = False
    pet['weight'] = pet['weight'] +1
  else: print('The Pypet is not hungry!')

def play(pet):
  if pet['bored'] == True:
    pet['bored'] = False
    pet['weight'] = pet['weight'] -.5
  else: print('The Pypet is tired! ' + pet['photo'])

pets =[fish, mouse]

play(fish)
play(fish)
play(mouse)
play(mouse)
