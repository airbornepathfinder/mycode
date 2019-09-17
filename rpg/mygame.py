#!/usr/bin/env python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]

  You will begin in the Hall.  
  You have the ability to go north, south, east, or west. 
  You can pick up the item in each room.  Hint some will keep you safe!
  The Attic is as far North as it goes, DUE NORTH!
  The Basemanet is a far South as it gets, WEST and SOUTH!
  As for the rest give it try I am sure you will find the Garden!
  Don't miss the Kitchen :)

  You can exit any time by typing either:
  quit
  exit
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#winnermessage
winnermessage = ''

#a dictionary linking a room to other rooms
rooms = {

            'Attic' : {
                  'south' : 'Hall',
                  'item' : 'poolfloat'
                 },
            'Hall' : {
                  'north' : 'Attic',
                  'south' : 'Kitchen',
                  'west' : 'Study',
                  'east' : 'Dining Room',
                  'item' : 'key'
                },
            'Study' : {
                  'south' : 'Living Room',
                  'east' : 'Hall',
                  'item' : 'book'
                },
            'Living Room' : {
                  'south' : 'Basement',
                  'north' : 'Study',
                  'item' : 'remotecontrol'
                },
            'Basement' : {
                  'north' : 'Living Room',
                  'item' : 'lightsaber'
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'west' : 'Living Room',
                  'item' : 'monster'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south' : 'Garden'
                },
            'Garden' : {
                'north' : 'Dining Room'
                }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  if move[0] == 'exit' or move[0] == 'quit':
      print("Thank you for playing come back soon! Our monster is waiting :)")
      break

  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'lightsaber' in inventory:
      print("Monster destroyed by lightsaber attack")
      del rooms[currentRoom]['item']  
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
      print("A monster has got you!... GAME OVER!")
      break

  # define how a player can win
  if currentRoom == 'Garden' :
     for i in inventory:
         if (i == 'key') and (currentRoom == 'Garden') :
             winnermessage = '\nYou have the key to the poolhouse! Enjoy the water!\n'
             print(winnermessage)
         if (i == 'book') and (currentRoom == 'Garden') :
             winnermessage = '\nYou can read your book leaders are readers\n'
             print(winnermessage)
         if (i == 'poolfloat') and (currentRoom == 'Garden') :
             winnermessage = '\nYou can float in the pool!\n'
             print(winnermessage)
         if (i == 'remotecontrol') and (currentRoom == 'Garden') :
             winnermessage = '\nBe sure to change the channel\n'
             print(winnermessage)
         if (i == 'lightsaber') and (currentRoom == 'Garden') :
             winnermessage = '\nPractice your lightsaber tactics\n'
             print(winnermessage)
     break

 #  if currentRoom == 'Garden' and ['key', 'book', 'poolfloat', 'remotecontrol', 'lightsaber'] in inventory:
 #     print('You escaped the house with all items to ! YOU WIN!')
 #     break
