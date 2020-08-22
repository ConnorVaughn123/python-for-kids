# adventure game
import time
print('Welcome to the Santa Cruz Mountain Adventure Game!')
print('**************************************')
print('You are visiting Santa Cruz, California.')
print('You go on an evening hike in the mountains.')
print('It is dark.')
print('You can pick one item to take with you -  ')
print('map, flashlight, chocolate, rope, jetpack(with enough fuel to use once), or gokart: ')
item = input('What do you choose?: ')
print('You hear a loud humming noise. It gets even louder! You are scared.')
choice1 = input('Do you follow the sound? Enter y or n: ')
if choice1 == 'y':
    print('After all, this is an adventure. You\'ll be fine.')
    print('A nagging voice in your head disagrees.')
    print('Too late to change now.')
    print('You slowly inch closer to the sound, holding your', item, 'out like a weapon.')
    print('The sound suddenly stops. Something is wrong here.')
    print('You look for the starting point.')
    print('...')
    print('Where is it?')
    print('You are now LOST ... ')
    print('You try to call on your phone, but there is no signal.')
    print('Aimlessly, you walk around.')
    print('Suddenly, the sound starts up again!')
    print('You run away quickly!')
    print('You are running fast. The sound gets really loud!')
    print('Panting, you duck behind a tree and the sound stops.')
    print('You have to get out of here!')
else:
    print('You won\'t follow it.')
    print('You\'re not taking risks.')
    print('You want to go home.')
    print('You walk to the starting point.')
    print('Huh?')
    print('Where is the starting point?')
    print('You realize that you are LOST ... ')
    print('You try to call on your phone, but there is no signal.')
    print('You walk around aimlessly.')
    print('All of a sudden you hear the sound again.')
    print('You can\'t give up now.')
    print('So you run away like a little sissy baby.')
    print('You hide in a bush, exhausted.')
    print('The sound stops.')
    print('You have to get out of here!')
direction = input('Which direction do you go? north, south, east, or west?: ')
if direction == 'north':
    print('You reach an abandoned cabin.')
    if item = 'map':
        print('You use the map to find your way back home from the calm setting of the cabin.')
        print('You win the game!')
    elif item = 'gokart':
        print('You use your gokart to drive down a big hill.')
        print('After a few more minutes of travel, you come to an empty gas station.')
        print('You stick out your thumb for a lift.')
        print('After a while, a bus spewing gas comes to the station.')
        print('You pump your fist!')
        print('But...')
        trust = input('Will you trust him?: ')
        if trust == 'yes':
            print('You ask if you can get a ride.')
            print'The driver says sure.')
            
        

    
       
       
      
