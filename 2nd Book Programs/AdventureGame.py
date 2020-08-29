# adventure game
print('Welcome to the Santa Cruz Mountain Adventure Game!')
print('**************************************')
print('You are visiting Santa Cruz, California.')
print('You go on an evening adventure in the mountains.')
print('It is dark.')
print('You can pick one item to take with you -  ')
print('map, flashlight, rope, grappling hook, or gokart: ')
item = input('What do you choose?: ')
print('You hear a loud humming noise. It gets even louder! You are scared.')
choice1 = input('Do you follow the sound? Enter yes or no: ')
if choice1 == 'yes':
    print('After all, this is an adventure. You\'ll be fine.')
    print('A nagging voice in your head disagrees.')
    print('Too late to change now.')
    if item == 'gokart':
        print('You warily inch toward the sound.')
    else:
        print('You slowly inch closer to the sound, holding your', item, 'out like a weapon.')
    print('The sound suddenly stops. Something is wrong here.')
    print('You look for the starting point.')
    print('...')
    print('Where is it?')
    print('You are now LOST.')
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
    print('You realize that you are LOST.')
    print('You try to call on your phone, but there is no signal.')
    print('You walk around aimlessly.')
    print('All of a sudden you hear the sound again.')
    print('You can\'t give up now.')
    print('So you run away fast.')
    print('You hide in a bush, exhausted.')
    print('The sound stops.')
    print('You have to get out of here!')
direction = input('Which direction do you go? north, south, east, or west?: ')
if direction == 'north':
    print('You reach an abandoned cabin.')
    if item == 'map':
        print('You use the map to find your way back home from the cabin.')
        print('You win the game!')
        print('But it seems there could be more to your adventure.')
        print('You can try again...')
    elif item == 'gokart':
        print('Here is a good place to rest.')
        print('If only you had food...')
        print('You rest for an hour here.')
        print('Now you are ready to go.')
        print('You use your gokart to drive down a big hill.')
        print('After a few more minutes of travel, you come to an empty gas station.')
        print('You stick out your thumb for a lift.')
        print('After a while, a bus spewing gas comes to the station.')
        print('You pump your fist!')
        print('But...')
        trust = input('Will you trust him?: ')
        if trust == 'yes':
            print('You ask if you can get a ride.')
            print('The driver says sure.')
            print('"Where do you want to go?", he asks.')
            print('You tell him your address.')
            print('He asks you if you\'re hungry.')
            print('You realize you haven\'t ate in hours.')
            print('He asks where you want to go to eat.')
            fav_restaurant = input('Enter your favorite restaurant: ')
            print('He takes you to', fav_restaurant, 'and you order a ton of food and gobble it up.')
            print('You thank him a lot and he takes you home.')
            print('You have won the game!')
        elif trust == 'no':
            print('You won\'t trust him.')
            print('He does look kind of shady.')
            print('He drives by.')
            print('You wait...')
            print('...')
            print('...')
            print('Suddenly, you see a flying minivan arc though the air!')
            print('You are at a loss for words.')
            print('The minivan is beat up and has poorly drawn flames on the side, but there are propellers where the wheels are supposed to be.')
            print('It crash lands, hitting a gas pump and a gas can.')
            print('They fly through the air(bump, bump, bump, bump, KABOOM!)')
            print('There is a huge explosion, and the mininvan lands next to you.')
            print('A woman gets out.')
            print('"Sorry about that.", she says.')
            print('You manage to gasp out, "Who are you?"')
            print('She introduces herself as just Melinda. She doesn\'t give a last name.')
            print('"This is a flying car I made.", she continues.')
            print('"I was driving to the Guiness World Records Office to show them I made a flying car.", she explains.')
            print('"But I saw you and you look like you need a lift."')
            print('You gape at her in disbelief.')
            print('"Oh, the flames? My kids painted those."')
            print('"Me and my husband have a company called Cars of the Future."')
            print('She hands you a business card. It reads, Cars of the Future in a flaming font.')
            print('She asks where you want to go.')
            print('You tell her your address.')
            print('You fly there, people marveling at the minivan.')
            print('"T-thanks.", you tell her.')
            print('"No problem.", she says.')
            print('She flies off.')
            print('You have won the game!')
    else:
            print('If you had a map, you could find your way. If you had a gokart, you could have rode home without getting tired.')
            print('You have lost the game.')
            print('Try again...')
elif direction == 'south':
    print('You come to a river with a broken bridge.')
    print('How could this be fixed...?')
    if item == 'flashlight' or item == 'cheeseburger' or item == 'batteries' or item == 'gokart':
        print('You have nothing that can help you fix the bridge, so you walk as far as you can.')
        print('You don\'t know where you are going.')
        print('Nowhere to go...')
        print('You have lost the game.')
        print('If you had a map, you could find your way.')
        print('Or, if you had a rope, you could fix the bridge.')
        print('Try again...')
    else:
        if item == 'map':
            print('You have nothing that can help you fix the bridge, so you walk as far as you can.')
            print('You suddenly realize have a map, so you look at the map.')
            print('It looks like the town of White Gold Creek, California is near.')
            print('Unfortunately, it\'s across the bridge!')
            print('Need to go somewhere else.')
            print('You walk through the woods.')
            print('You come across some batteries.')
            print('Might need those...')
            print('In your pocket they go.')
            print('You walk until you are all tired out.')
            print('But, you see a little banged up pink Barbie car for kids.')
            print('It\'s lying on its side.')
            print('Hmm, what if...?')
            print('Yes, it takes double a\'s!')
            print('You take the old batteries out and cross your fingers it works.')
            print('You hit the gas and it goes.')
            print('It\'s uncomfortable, but at least it\'s a ride.')
            print('You drive around, looking for civilization.')
        elif item == 'rope':
            print('Oh yeah, you have a rope.')
            print('You can fix the bridge.')
            print('After working for a while, you fix the bridge.')
            print('You walk across...')
            print('Almost there...')
            print('Suddenly, a purple bus appears out of nowhere.')
            print('Graffiti on the side of it identifies it as "The Knight Bus"')
            print('It rumbles by, rocking from side to side dangerously.')
            print('You realize it\'s coming toward you!')
            print('You run back where you came as fast as you can.')
            print('It\'s coming closer!')
            print('Suddenly, it disappears. You hear glass shattering and a cat meowing.')
            print('That was crazy!')
            print('You pick yourself up and keep on going.')
        print('Soon, you come to the town of White Gold Creek, California.')
        if item == map:
            print('You know it\'s called that from your map and the dusty sign.')
        else:
            print('You know it\'s called that from the paint-peeling sign.')
            print('You ditch the Barbie car and go inside.')
        print('This is a good place to rest.')
        print('You walk through the town.')
        print('It looks like a ghost town.')
        print('Nobody is here.')
        print('You find a penny on the ground.')
        pick_up = input('Will you pick it up?: ')
        if pick_up == 'yes':
            print('You pick up the coin.')
            print('Suddenly, you hear a rumbling noise.')
            print('All of a sudden, the ground opens up and a shiny Lamborghini with a rocket attached to it comes out.')
            print('What is that...?')
            print('And why is it here?')
            print('You decide to go in the Lamborghini.')
            print('You sit in the seat. It is in perfect condition.')
            print('The key is in the ignition.')
            drive = input('Will you drive it?: ')
            if drive == 'yes':
                print('You drive it, crashing into a saloon and stirring up debris.')
                print('Wow, it\'s fast!')
                print('But luckily, you and the car are ok.')
                print('From now on you\'ll drive it more carefully.')
                print('Off in the distance, you see an abandoned airport.')
                print('It looks like the runways would be a great place to drive this.')
                print('You drive over to the airport.')
                print('Then you start at the beginning of a runway.')
                print('You hit the gas and keep stepping on it.')
                print('It accelerates and keeps going.')
                print('Suddenly, you hear a computerized voice.')
                print('3...')
                print('2...')
                print('1...')
                print('The rocket goes off!')
                print('The Lamborghini gets launched into the sky!')
                print('You are flying!')
                print('It does a loop the loop and goes really fast, and the rocket falls off and keeps going. It then crash lands in a tree.')
                print('Shaking, you climb down the tree,')
                print('You see a scared cat on one of the branches.')
                print('You want to help it, so you grab it.')
                print('You continue climbing down.')
                print('You get down.')
                print('You see your house!')
                print('You run there and give the cat some milk.')
                print('You have won the game!')
                print('But I wonder where that rocket went.')
                print('In other news, a runaway rocket has hit the town of White Gold Creek!')
            else:
                print('This is probably someone else\'s.')
                print('You shouldn\'t take it.')
                print('You scramble out.')
                print('What now?')
                print('You go into the inn.')
                print('You sleep on a bed and raid the minibar.')
                print('You wake up refreshed.')
                print('You see a road in the distance.')
                print('You walk there and wait.')
                print('You see an SUV driving up the road, and you know what you have to do.')
                print('You jump on the bar on the back and ride the SUV.')
                print('Your arms are getting tired, so you jump off.')
                print('You see your house!')
                print('You have won the game!')
        else:
            print('You leave the coin there for someone else to find.')
            print('You see an inn, so you decide to rest there.')
            print('You find the biggest bed there, and rest there.')
            print('In the morning, you wake up ready to find your way back home.')
            if item == 'map':
                print('You go back to the Barbie car and drive out of there, making sure to load it with snacks.')
                print('You keep driving until you come to a big hill.')
                print('At the bottom, there is the top of a waterslide.')
                print('You look closer, and there is a whole waterpark.')
                print('You decide to drive down it because it looks like the bumps aren\'t too big.')
                print('You drive down..')
                print('Your car goes very fast, hits a small bump, and the engine sputters and dies.')
                print('However, the car is still going.')
                print('The car rolls over itself, ripping open the snack packs and banging you up.')
                print('Crunch! The steering wheel falls off. You have no control!')
                print('It keeps going, you try to stop it but fail, and then it starts driving right side up.')
                print('You hold on tight, and the car sets itself on a crash course with the top of the slide.')
                print('The car hits the lip of the slide and flips on its side.')
                print('It goes down the slide -')
                print('With you in it!')
                print('You wake up, dizzy.')
                print('What happened?')
                print('You are in shallow water, and there is orange dust all over you.')
                print('The bags and pieces of the snacks are floating around you.')
                print('The car is smashed against a wall a few yards away from you, and pieces of it are floating in the water too.')
                print('You see people looking at you, but only a few are there.')
                print('They ask if you\'re ok.')
                print('Suddenly, the manager comes running.')
                print('You know because of the tag on his shirt. "Manager John".')
                print('He looks angry!')
                print('You run out of the waterpark, through the open gates.')
                print('You see a pickup truck pulling out, and scramble into the bed.')
                print('They drive for a while, and then you see your house!')
                print('You jump out and run inside.')
                print('You have won the game!')
            else:
                print('You sleep here for a while.')
                print('Soon, you feel like you are ready for a journey back home.')
                print('You find an old backpack, some batteries in a bag that says "Fresh Batteries", and take all the snacks in the minibar.')
                print('You put the batteries and food in the backpack, and put it on your back.')
                print('You are ready to go!')
                print('You walk out of White Gold Creek, and walking through the woods you see a battery-powered skateboard.')
                print('You put your batteries in it, and it works!')
                print('You ride it for a long time, and you get to the town where you live.')
                print('You keep riding, and you see your house!')
                print('You have won the game!')
                print('And now you can eat your snacks. Yummy!')
elif direction == 'west':
    print('The ground is slick from rain.')
    print('You are walking down a hill and trip over a log slippery from the rain.')
    print('You slide down the hill and hit your head on a stone.')
    print('You see stars, then rub your eyes.')
    print('You look up and you see a statue of what looks like a stone Toad from Mario games.')
    print('There is a button made out of a darker stone on its jacket.')
    press = input('Will you press it?: ')
    if press == 'yes':
        print('You hear a sound of stone on stone, and the statue sinks into the ground.')
        print('You look into the hole, and see lights and hear music.')
        print('Suddenly, you slip and fall in.')
        print('The music stops and the lights turn off.')
        print('It is dark, even more then outside.')
        if item == 'flashlight':
            print('You turn on your flashlight.')
            print('You shine it around, and you see an abandoned dance floor.')
            print('There is a DJ\'s table in the middle of the room.')
            print('A broken sign reads "Temple of Shrooms".')
            print('Suddenly, the sign falls off and crumbles to dust.')
            print('You see a figure lurking in the darkness.')
            print('You shine your flashlight there, and it is just a statue of a Shy Guy.')
            print('You remember these guys from a video game you played a few months before your adventure.')
            print('It was called Paper Mario Origami King.')
            print('You finished the yellow streamer, then stopped playing.')
            print('Come to think of it, you recognize this place!')
            print('This is the Temple of Shrooms!')
            print('You are in the Paper Mario Origami King universe!')
            print('You fall over with surprise!')
            print('On the floor, you think about your situation.')
            print('This is bad, because how will you get back to real life?')
            print('But wait...')
            print('This could be fun!')
            print('Maybe you can find Mario and Olivia and go on an adventure with them!')
            print('Then, Olivia can float you out of here.')
            print('You see a pipe, so you try to go down it.')
            print('Miraculously, it works!')
            print('You fold through the pipe and come out. You recognize the area you come out in.')
            print('Wait...')
            print('FOLD?!?!?!?!?')
            print('You look down at your hands.')
            print('They are flat. You are flat!')
            print('You fall backwards into some spikes, and you wake up, drenched in sweat.')
            print('You are in your own bed.')
            print('You check your hands. They are normal.')
            print('Phew.')
            print('But that doesn\'t count as winning! Try again!')
            print('What\'s that? You\'ve been through enough?')
            print('Fine, I guess...') 
            print('You have won the game!')
        else:
            print('You can\'t see.')
            print('You feel your way along the walls into another room.')
            print('You feel a railing, which you hold onto.')
            print('You walk sideways, but then your hands touch thin air!')
            print('You walk forward right into nothingness!')
            print('But, you get stuck in something sticky.')
            print('Suddenly, you can see.')
            print('You see you are caught in a giant spiderweb, and there are people with little mushroom shaped heads without faces.')
            print('You scream, but one of them claps their hand over your mouth.')
            print('You are stuck here.')
            print('It could be a while until help arrives, if they even can find you.')
            print('You have lost the game!')
            print('If you had a flashlight you could see, but maybe you just shouldn\'t have pressed that button.')
            print('Try again...')
            
    else:
        print('You don\'t press the button.')
        print('You shouldn\'t go around pressing buttons like that.')
        print('Who knows what they do?')
        print('You have a headache from hitting your head.')
        print('You lie there and wait for it to pass.')
        print('After a while, you fall asleep.')
        print('You wake up and rub your eyes.')
        print('You are just in a normal clearing.')
        print('Wasn\'t the statue there though?')
        print('Oh well.')
        print('You continue on.')
        print('You hear a river trickling.')
        follow_it = input('Will you follow the river?: ')
        if follow_it == 'no':
            print('You walk away from the river.')
            print('You are LOST.')
            print('You look for somewhere to go, but find only a rusty, abandoned pickup truck.')
            print('There is food in there, but it all looks stale and dusty, except for one big bag of chips.')
            print('You break the window to  get the chips.')
            print('You eat them all quickly, but it makes you super thirsty.')
            print('You can\'t find water.')
            print('You have lost the game!')
            print('Maybe if you had followed the river...')
        if follow_it == 'yes':
            print('You decide to follow it.')
            print('You walk along the bank.')
            print('While you are walking, you spot a familiar wrapper from McDonalds.')
            print('Maybe there is food inside...')
            print('You look inside...')
            print('There is a bright orange key.')
            print('What is the key for?')
            print('You don\'t know, but wish it was actual food.')
            print('You put it in your pocket.')
            print('You keep following the river, not so hungry anymore.')
            print('After a while, the river expands into a lake.')
            print('You see a boat floating in the water and jump on.')
            print('You need a ride.')
            print('There is no one on the boat.')
            print('You look at the controls.')
            print('There is a keyhole in the middle and an owner\'s manual on top of the controls.')
            print('What if the orange key turns on the boat?')
            print('You try the key, and sure enough, it starts up.')
            print('You turn it off and read the owner\'s manual.')
            print('You think you understand how to drive it.')
            print('So you turn it back on.')
            print('You keep driving forward for a while, and the lake flows back into a river.')
            print('After a while, you come to the ocean.')
            print('This boat is really fast.')
            print('The ocean is a completely different world than where you just were.')
            print('It is sunny and warm, and you can see lots of islands.')
            print('This sight inspires you to go for an adventure at sea.')
            print('You live right next to the ocean, so when your adventure is over, you can go home.')
            print('Genius! Or is it...?')
            print('You don\'t want to think about that.')
            print('The manual has a sea chart, and you decide to write down and draw which islands you visit.')
            print('You decide to explore the sea.')
            print('This will be fun.')
            print('You go full speed ahead, and after a while, you come to an island swith a skull on it.')
            print('On the sea chart, you sketch a skull and decide to call the island Skull Island.')
            print('You park your boat and get off, leaving the sea chart in your cabin.')
            print('You decide to explore the island and look for food and water.')
            print('On the mainland outside the skull, you spot a black bag with a hole in it.')
            print('You look in and see a frozen pizza, bubble gum, a half-eaten BLT, and some more things.')
            print('There is a smiley sticker on the bag.')
            print('On the sticker it says "take what you need".')
            print('You look in the bag again, and you also see a Hot Wheels Car, one french fry, a doll, an empty water bottle, and a thermos of hot chocolate.')
            print('There is also a bag of marshmallows and a Ziploc of cooked rice.')
            print('You decide to take what\'s useful.')
            print('You take an uneaten bit of bacon, the empty water bottle, and the rice.')
            print('In the sand you write what you took.')
            print('You eat the bacon and half of the rice, and put the rest of the rice and the empty water bottle on the boat.')
            print('You decide to explore the skull.')
            print('It looks like you can enter through the ears... or where the ears would be.')
            print('You scramble in.')
            print('A rock drops over the entrance. You hear another rock drop somewhere.')
            print('In here there are four flames.')
            print('The order is: on, on, off, on.')
            print('There is a doorway, so you go in.')
            print('There is another room, the same as the last room, but the order is off, on, on, off.')
            print('There are buttons in front of the flames.')
            print('When you press one, the flame above changes from off to on.')
            flame_order = input('What order will you put the flames in?: ')
            if flame_order == 'off, off, on, off':
                print('You are a smart one.')
                print('You hear the rocks slide back up, and you run out before they close.')
                print('You flee to the boat and drive full speed until you feel safe.')
                print('That was close!')
                print('You look at the mainland on the sea chart, and see your city marked with a dot.')
                print('This is enough adventuring for you.')
                print('You plan to go home now.')
                print('You find your way to the mainland.')
                print('You get off.')
                print('You walk for a while, eating your rice for a snack.')
                print('You begin to recognize the buildings, and go to your house.')
                print('You go inside and take a nice bath.')
                print('You have won the game!')
            else:
                print('You are stuck here. The flames sink into the ground, so you must have gotten the combo wrong.')
                print('You have lost the game!')
                print('Hint: opposites.')
                print('Try again...')
                

elif direction == 'east':
    print('You have chosen the right way!')
    print('You can get home fast, as long if you have the right item...')
    print('You walk through the woods, looking for a place to go.')
    if item == 'grappling hook':
        print('You find an abandoned skateboard.')
        print('You skate down the hill, and keep skating until you come to the side of the highway.')
        print('You wait for a car to come.')
        print('While you wait, you practice using your grappling hook.')
        print('At first, you are not good at it.')
        print('But after a while, you start to get better.')
        print('Soon, you are an expert at throwing your grappling hook.')
        print('You spot a bag of chips slightly shaking on the ground.')
        print('You are shaking too, but you ignore it.')
        print('The shaking gets stronger, and you feel the ground rumble.')
        print('This is an earthquake!')
        print('You need food, so you aim for the chips with your grappling hook.')
        print('Steady...')
        print('Perfect!')
        print('Fire!')
        print('The grappling hook arcs through the air...')
        print('In these few milliseconds, a lot of stuff happens.')
        print('First, the shaking gets much stronger, and you stumble backward.')
        print('While you are stumbling, you see a orange flaming thing heading straight for you!')
        print('Your feet touch the skateboard, and you get tangled in the line from the grappling hook.')
        print('You see the flaming thing shoot past, a few inches away from you.')
        print('And this is where things get crazy.')
        print('You see that the flaming thing is actually a race car with a huge spoiler.')
        print('Your grappling hook gets caught on the end of the spoiler, and your arm almost get pulled out of its socket, but you begin to skateboard behind it.')
        print('You are going super fast!')
        print('The car goes so fast, it starts to FLY!')
        print('The line breaks, and you get flung through the air.')
        print('Your life flashes before your eyes.')
        print('But you hit a mattress.')
        print('You fly up gently, and land on the roof of your house, undamaged!')
        print('You remember that you put the mattress there to watch a movie outside, and now it has saved you.')
        print('You see the car hit a billboard advertising McDonalds, and fireworks burst over it.')
        print('Oh no, who was in there?')
        print('You see a flaming body fly out of the car.')
        print('It lands on the lawn of the house next to you, and you see it\'s actually a barrel.')
        print('Phew.')
        print('You have won the game!')
        print('This is the secret ending!')
        print('Great job finding it!')
    else:
        print('There\'s nowhere to go.')
        print('You have lost the game!')
