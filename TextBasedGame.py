#Pasco Logan
#7-3 Project 2
intro = '''There has been a murder at the brooks manor. The killer is still inside
You are a young detective trying to collect clues to solve the case before 
you are the next victim.You will be starting in the grand hall try to find all the 
clues before the killer finds you!'''
print(intro)
print('1. Use commands north, south, east, west to explore the manor.')
print('2. To pick up clues use the command get.')
print('3. Collect 6 clues to win.')
print('4. Type quit at anytime to exit')
rooms = {'grand hall': {'name': 'an grand hall', 'east': 'kitchen', 'north': 'office','west':'library',
                        'south': 'bathroom','contents':[],
        'text': 'A long dark hallway with a spiral staircase.'},
    'office': {'name': 'a office', 'east': 'cellar', 'south': 'grand hall',
        'text': 'A large wooden desk with stacks of papers everywhere.',
    'contents':['A glass with lipstick on it']},
    'cellar': {'name': 'a cellar', 'west': 'office','clue': 'Bloody Fingerprints',
        'text': 'large wooden door with pad a lock.',
    'contents':['Bloody fingerprints']},
    'library': {'name': 'a library', 'east': 'grand hall',
        'text': 'Walls are line with old books with a desk in the middle.',
    'contents':['Love letter']},
    'bathroom': {'name': 'a bathroom','north':'grand hall','east':'bedroom',
        'text': 'Free standing tube and a medicine cabinet.',
    'contents':['Broken mirror']},
    'dining room': {'name': 'a dining room',
        'text': 'A large set table with bay windows and ripped curtains.',
    'contents': ['A large shadowy figure holding something']},
    'kitchen' : {'name': 'a kitchen','west': 'grand hall','north': 'dining room',
        'text': 'Old fashioned with a bare and sordid feel',
    'contents':['A Bloody knife']},
    'bedroom': {'name': 'a bedroom','west':'bathroom',
        'text': 'A king size canopy bed with a missing post.',
    'contents':['A empty pill bottle'] }}

directions = ['north', 'south', 'east', 'west']
current_room = rooms['grand hall']
carrying=[]

while True:
    print()
    print('You are in {}.'.format(current_room['name']))
    print(current_room['text'])
    if current_room['contents']:
        print('In the room are:{}'.format(','.join(current_room['contents'])))
        print('Clues found: {}'.format(carrying))
    command = input('\nWhat do you do? ').strip().lower()
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
            if current_room['name'] == 'a dining room':
                print('Game Over!')
                print('''You are in a dining room.
A large set table with bay windows and ripped curtains.
In the room there is a large shadowy figure holding a axe!''')
                break
        else:
            print("You can't go that way.")
    elif command.lower() in ('q', 'quit'):
        print('Thanks for playing!' )
        break
    elif command =='get':
        item=current_room['contents']
        carrying.append(item)
        if item in current_room['contents']:
            current_room['contents'].remove(item)
            carrying.append(item)
        if len(carrying) == 6:
            print('Congratulations You Won!')
            print('You have found all the clues')
            print('and the killer has been caught')
            break
    else:
        print("I don't understand that command.")







