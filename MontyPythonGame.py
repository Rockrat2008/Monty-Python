#  AUTHOR:  Michael O'Brien
#  CREATED:  05 April 2018
#  MODIFIED:  30 April 2018
#  DESCRIPTION:  Monty Python text games


#  Load the dictionary with the episodes from season 11
episodes = {"It's Wolfgang Amadeus Mozart":1,"Famous Deaths":1,"Italian Lesson":1,"Whizzo Butter":1,"It's the Arts":1,"Arthur 'Two-Sheds' Jackson":1,"Picasso/Cycling Race":1,"The Funniest Joke in the World":1,"Flying Sheep":2, "French Lecture on Sheep-Aircraft":2,"A Man with Three Buttocks":2,"A Man with Two Noses":2,"Musical Mice":2,"Marriage Guidance Councellor":2,"The Wacky Queen":2,"Working-Class Playwright":2,"A Scotsman on a Horse":2,"the Wrestling Epilogue":2,"The Mouse Problem":2,"Court Scene":3,"The Larch":3,"Bicycle Repairman":3,"Children's Stories":3,"Restaurant Sketch":3,"Seduced Milkmen":3,"Stolen Newsreader":3,"Children's Interview":3, "Nudge, Nudge":3,"Song":4,"Art Gallery":4,"Art Critic":4,"It's a Man's Life in the Modern Army":4,"Undressing in Public":4,"Self-Defense Against Fresh Fruit":4,"Secret Service Dentists":4,"Confuse-a-Cat":5,"The Smuggler":5,"A Duck, a Cat and a Lizard":5,"Vox Pops on Smuggling":5,"Police Raid":5,"Letters and Vox Pops":5,"Newsreader Arrested":5,"Erotic Film":5,"Silly Job Interview":5,"Careers Advisory Board":5,"Burglar/Encyclopaedia Salesman":5,"Johann Gombolputty.... von Hautkopf of Ulm":6,"Non-illegal Robbery":6,"Vox Pops":6,"Crunchy Frog":6,"The Dull Life of a City Stockbroker":6,"Red Indian in Theatre":6,"Policemen Make Wonderful Friends":6,"A Scotsman on a Horse":6,"Twentieth-Century Vole":6,"Camel Spotting":7,"You're No Fun Anymore":7,"The Audit":7,"Science Fiction Sketch":7,"Man Turns Into Scotsman":7,"Police Station":7,"Blancmanges Playing Tennis":7,"Army Protection Racket":8,"Vox Pops":8,"Art Critic - the Place of the Nude":8,"Buying a Bed":8,"Hermits":8,"Dead Parrot (Petshop)":8,"The Flasher":8, "Hell's Grannies":8,"Llamas":9,"A Man with a Tape Recorder up His Nose":9,"Kilimanjaro Expedition":9,"A Man with a Tape Recorder up His Brother's Nose":9,"Homicidal Barber":9,"Lumberjack Song":9,"Gumby Crooner":9, "The Refreshment Room at Bletchley":9,"Hunting Film":9,"The Visitors":9,"Walk-on-Part in Sketch":10,"Bank Robber":10,"Trailer":10,"Arthur Tree":10,"Vocational Guidance Counsellor":10,"The First Man to Jump the Channel":10,"Tunnelling from Godalming to Java":10,"Pet Conversions":10,"Gorilla Librarian":10,"Letters to 'Daily Mirror'":10,"Strangers in the Night":10,"Letters":11,"Interuptions":11,"Agatha Christie Sketch":11, "Undertakers File 1 Literary Football Discussion":11,"Interesting People":11,"Eighteenth-Century Social Legislation":11,"The Battle of Trafalgar":11,"Batley Townswomens' Guild Presents the Battle of Pearl Harbour":11, "Undertakers Film 2":11,"Falling From Buildings":12,"'Spectrum' -  Talking About Things":12,"Visitors from Coventry":12,"Mr Hitler":12,"The North Minehead By-Election":12,"Police Station":12,"Upperclass Twit of the Year":12, "Ken Shabby":12,"How Far Can a Minister Fall?":12,"Intermissions":13,"Restaurant":13,"Advertisments":13,"Albatross":13,"Come Back to My Place":13,"Me Doctor":13,"Historical Impersonations":13,"Quiz Programme - 'Wishes'":13, "'Probe-Around' on Crime":13,"Stonehenge":13,"Mr Attila the Hun":13,"Psychiatry - Silly Sketch":13,"Operating Theatre":13}


#  Global variablees to be used by the adventure RPG to track success
book = False
glasses = False
key = False
matches = False
papers = False


#  Import the random function to generate a random number for the guessing game
import random


#  Import the date and time module for the output to the text file scoring of the skit guessing game
from datetime import datetime


#  Function to clear the screen
def cls():
    print ('\n')*80


#  Function to dispaly the user menu for searching, displaying, and adding to the dictionaly
def menu():
    print (' ')
    print ('MONTY PYTHON GAME CHOICE MENU')
    print (' ')
    print ('1.  Skit guessing game')
    print ('2.  Go on an adventure to find the Holy Grail')
    print ('3.  Hangman')
    print ('4.  Exit')
    print (' ')
    choice = input('What would you like to do?(Enter the number)  ')
    while len(choice) != 1:
        choice = input('Please make a valid selection:  ')
    if int(choice) == 1:
        skit_guess_instructions()
    elif int(choice) == 2:
        rpg()
    elif int(choice) == 3:
        hangman()
    elif int(choice) == 4:
        print (' ')
        print ('Thank you for playing these Monty Python games.  I hope you had fun!')
    else:
        print (' ')
        print ('Please make a valid selection')
        print (' ')
        menu()


#  Function with instructions for the SKIT GUESSING GAME
def skit_guess_instructions():
    print (' ')
    print ('SKIT GUESSING GAME')
    print (' ')
    print ('In this game I will give you the name of a skit and you have to guess the episode number that the skit aired in')
    print(' ')
    print ('1 - Play the game')
    print ('2 - See current scores of players')
    print ('3 - Return to the Monty Python game choice menu')
    print(' ')
    choice = input ('What would you like to do?  ')
    while len(choice) != 1:
        choice = input ('Please make a choice on what you want to do:  ')
    if int(choice) == 1:
        player_name = input('Enter your name to test your knowledge in the Monty Python skit guessing game:  ')
        while len(player_name) < 1:
            player_name = input('If you want to test your knowledge of Monty Python skits you must enter your name:  ')
        number_correct = 0
        number_incorrect = 0
        skit_guess_game(player_name, number_correct, number_incorrect)
    elif int(choice) == 2:
        print ('PREVIOUS SCORES')
        print (' ')
        scoresFile = open ('scores.txt', 'r')
        highScores = scoresFile.read()
        print (highScores)
        scoresFile.close()
        skit_guess_instructions()
    elif int(choice) == 3:
        menu()
    else:
        print ('Please make a valid selection')
        skit_guess_instructions()


#  Function to play the SKIT GUESSING GAME
def skit_guess_game(player_name, number_correct, number_incorrect):
    episode_name, episode_number = random.choice(list(episodes.items()))
    print (' ')
    print ('What episode did skit ' + episode_name + ' appear in?')
    print (' ')
    player_guess = input('Enter an episode number between 1-13 or 14 to exit:  ')
    while (player_guess) < 1:
        player_guess = input('You must enter an episode number between 1-13 or 14 to exit:  ')
    if int(player_guess) in range(1,15):
        if int(episode_number) == int(player_guess):
            print ("CORRECT!  " + episode_name + ' appeared in episode ' + str(episode_number))
            print (' ')
            number_correct = number_correct + 1
            skit_guess_game(player_name, number_correct, number_incorrect)
        elif int(player_guess) != 14:
            print ('Wrong, ' + episode_name + ' appeared in episode ' + str(episode_number))
            print (' ')
            number_incorrect = number_incorrect + 1
            skit_guess_game(player_name, number_correct, number_incorrect)
        elif int(player_guess) == 14:
            save_scores = open('scores.txt','a')
            number_correct = player_name + ':  ' + str(number_correct) + ' correct'
            print (number_correct)
            number_incorrect = player_name + ':  ' + str(number_incorrect) + ' incorrect'
            print (number_incorrect)
            print (' ')
            date_played = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_scores.write(date_played+'\n')
            save_scores.write(number_correct+'\n')
            save_scores.write(number_incorrect+'\n')
            save_scores.close()
            menu()
    else:
        print('Please make a valid selection between 1-14')
        skit_guess_game(player_name, number_correct, number_incorrect)


#  Function to start the adventure RPG
def rpg():
    print (' ')
    print ('ADVENTURE ROLEPLAYING GAME TO FIND THE HOLY GRAIL')
    print (' ')
    rpg_instructions = open('rpg_instructions.txt','r')
    rpgInstructions = rpg_instructions.read()
    print (rpgInstructions)
    rpg_instructions.close()
    print (' ')
    play = input('Enter "P" to play the game or "Q" to return to the game menu:  ')
    while len(play) != 1:
        play = input('Please enter "P" to paly or "Q" to return to the game menu:  ')
    if play.upper() == "Q":
        menu()
    elif play.upper() == "P":
        print (' ')
        player_name = input('Enter your name brave adventurer to begin the quest:  ')
        while len(player_name) < 1:
            player_name = input('If you are brave enough to take on the quest you must enter your name:  ')
        enter_building(player_name)
    else:
        print ('You need to make a valid selection')
        rpg()


#  Function to see if the user enters the building
def enter_building(player_name):
    print (' ')
    print ('As you are walking through the village you see a decrepit building with a dusty sign hanging loosely in front of it.  Through the dust you can make out "Those who seek the Holy Grail may enter if they feel worthy."')
    print ('1 - Walk through the door?')
    print ('2 - Continue through the village?')
    print (' ')
    choice = input('What do you do ' + player_name +'?  ')
    while len(choice) != 1:
        choice = input(player_name + ' you must decide what to do!  ')
    if choice == '2':
        print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
        menu()
    elif choice == '1':
        print (' ')
        print ('The door creaks open, scraping the floor from disuse as you enter the building.  In a moment you eyes adjust to the dimly lit room:')
        print ('1 - Look around the room?')
        print ('2 - Leave?')
        print (' ')
        choice = input('What do you do ' + player_name + '?  ')
        while len(choice) != 1:
            choice = input(player_name + ' you must decide what to do!  ')
        if choice == '2':
            print (player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
            rpg()
        elif choice == '1':
            room(player_name)
        else:
            print ('Please make a valid selection')
            enter_building(player_name)
    else:
        print('Pleae make a valid selection')
        enter_building(player_name)
        

#  Function to look around the room
def room(player_name):
    print (' ')
    print ('As you gaze around the room you see a bookcase against the wall, writing table in the corner, an end table next to the bookcase, a dining table, and a chair partially pulled out from the dining table')
    print ('You can see objects scattered around the room but are too far away to tell what any of them are')
    print ('1 - Look at the end table')
    print ('2 - Look at the dining table')
    print ('3 - Look at the writing desk')
    print ('4 - Look at the bookcase')
    print ('5 - Sit in the chair')
    print ('6 - Exit the room')
    print (' ')
    choice = input('What do you do ' + player_name + '?  ')
    while len(choice) != 1:
        choice = input(player_name + ' you must decide what to do!  ')
    if choice == '6':
        print (player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
        rpg()
    elif choice == '1':
        end_table(player_name,book,glasses,key,matches,papers)
    elif choice == '2':
        dining_table(player_name,book,glasses,key,matches,papers)
    elif choice == '3':
        writing_desk(player_name,book,glasses,key,matches,papers)
    elif choice == '4':
        bookcase(player_name,book,glasses,key,matches,papers)
    elif choice == '5':
        chair(player_name,book,glasses,key,matches,papers)
    else:
        print ('you didn not make a valid selection')
        room(player_name)


#  Function for the user to look at the bookcase for the book
def bookcase(player_name,book,glasses,key,matches,papers):
    print(' ')
    if(papers):
        print ('As you approach the bookcase you see shelves of books on the shelves covered in dust and cobwebs.  Scanning the titles you see one titled "The song of the Grail".')
        print ('1 - Take the book')
        print ('2 - Look at the end table')
        print ('3 - Look at the dining table')
        print ('4 - Look at the writing_desk')
        print ('5 - Sit in the chair')
        print (' ')
        choice = input('What do you do ' + player_name + '?  ')
        while len(choice) != 1:
            choice = input(player_name + ' you must decice what to do!  ')
        if choice == '1':
            print ('You now have the book titled "The song of the Grail".')
            book = True
            bookcase(player_name,book,glasses,key,matches,papers)
        elif choice == '2':
            end_table(player_name,book,glasses,key,matches,papers)
        elif choice == '3':
            dining_table(player_name,book,glasses,key,matches,papers)
        elif choice == '4':
            writing_desk(player_name,book,glasses,key,matches,papers)
        elif choice == '5':
              chair(player_name,book,glasses,key,matches,papers)
        else:
            print ('Please make a valid selection')
            bookcase(player_name,book,glasses,key,matches,papers)
    else:
        print ("As you approach the bookcase you see shelves of books on the shelves covered in dust and cobwebs.  You read some of the titles but don't know which book to choose.")
        print ('1 - Look at the end table')
        print ('2 - Look at the dining table')
        print ('3 - Look at the writing desk')
        print ('4 - Sit in the chair')
        print (' ')
        choice = input('What do you do ' + player_name + '?  ')
        while len(choice) != 1:
            choice = input(player_name + ' you must decice what to do!  ')
        if choice == '1':
            end_table(player_name,book,glasses,key,matches,papers)
        elif choice == '2':
            dining_table(player_name,book,glasses,key,matches,papers)
        elif choice == '3':
            writing_desk(player_name,book,glasses,key,matches,papers)
        elif choice == '4':
            chair(player_name,book,glasses,key,matches,papers)
        else:
            print ('Please make a valid selection')
            bookcase(player_name,book,glasses,key,matches,papers)


#  Function for the user to look at the writing desk and find the glasses
def writing_desk(player_name,book,glasses,key,matches,papers):
	print (' ')
	print ('When you get to the writing desk you see a pair of glasses lying on the desk')
	print ('1 - Take the glasses')
	print ('2 - Look at the end table')
	print ('3 - Look at the dining table')
	print ('4 - Look at the bookcase')
	print ('5 - Sit in the chair')
	print ('6 - Exit the room')
	print (' ')
	choice = input('What do you do ' + player_name + '?  ')
	while len(choice) != 1:
		choice = input(player_name + ' you must decide what to do!  ')
	if choice == '6':
		print (player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
		rpg()
	elif choice == '1':
		print ('You pick up the glasses')
		glasses = True
		writing_desk(player_name,book,glasses,key,matches,papers)
	elif choice == '2':
		end_table(player_name,book,glasses,key,matches,papers)
	elif choice == '3':
		dining_table(player_name,book,glasses,key,matches,papers)
	elif choice == '4':
		bookcase(player_name,book,glasses,key,matches,papers)
	elif choice == '5':
		chair(player_name,book,glasses,key,matches,papers)
	else:
		print ("You didn't make a valid selection")
		writing_desk(player_name,book,glasses,key,matches,papers)


#  Function for the user to look at the dining table
def dining_table(player_name,book,glasses,key,matches,papers):
	print (' ')
	print ('As you approach the table you see some papers lying on the corner of the table and a candle in the center of the table')
	print ('1 - Look at the documents')
	print ('2 - Light the candle')
	print ('3 - Look at the end table')
	print ('4 - Look at the writning desk')
	print ('5 - Look at the bookcase')
	print ('6 - Sit in the chair')
	print ('7 - Exit the room')
	print (' ')
	choice = input('What do you do ' + player_name + '?  ')
	while len(choice) != 1:
		choice = input(player_name + ' you must decide what to do!  ')
	if choice == '7':
		print (player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
		rpg()
	elif choice == '1':
		if (glasses):
			print ('The papers say "Guide to Finding the Holy Grail"')
			print ('As you read the guide it tells you "Whiile I haven\'t figured out everything yet in my search I have determined that I need to light a candle to reveal a hidden door.  I\'m not sure how all of this ties together bue apparantly there is also a music box, a key, and a book called "The song of the Grail" that will also aid in my quest.')
			papers = True
			dining_table(player_name,book,glasses,key,matches,papers)
		else:
			print ('The documents appear blurry and you are unable to read them right now.')
			dining_table(player_name,book,glasses,key,matches,papers)
	elif choice == '2':
		if(matches) and (key):
			print ('You light the candle.  As the flame from the candle illuminates the wall next to the bookcase you see a shadow flickering in the flame that looks like a keyhole. ')
			print (' ')
			print ('1 - Go to the secret door')
			print ('2 - keep looking around')
			choice = input('What do you do ' + player_name +'?  ')
			while len(choice) != 1:
				choice = input(player_name + 'you must decide what to do!  ')
			if choice == '1':
				secret_room(player_name)
			elif choice == '2':
				dining_table(player_name,book,glasses,key,matches,papers)
			else:
				print ('Please make a valid selection')
				dining_table(player_name,book,glasses,key,matches,papers)
		else:
			print ('You feel you need the matches and something else before you light the candle')
			dining_table(player_name,book,glasses,key,matches,papers)
	elif choice == '3':
		end_table(player_name,book,glasses,key,matches,papers)
	elif choice == '4':
		writing_desk(player_name,book,glasses,key,matches,papers)
	elif choice == '5':
		bookcase(player_name,book,glasses,key,matches,papers)
	elif choice == '6':
		chair(player_name,book,glasses,key,matches,papers)
	else:
		print ('you didn not make a valid selection')
		dining_table(player_name,book,glasses,key,matches,papers)


#  Function for the user to sit in the chair and find the matches
def chair(player_name,book,glasses,key,matches,papers):
    print (' ')
    print ('As you pull the chair out sit in the chair you notice something on the floor.  Looking closer you see a box of matches.')
    print ('1 - Take the matches')
    print ('2 - Go to the end table')
    print ('3 - Go to the dining table')
    print ('4 - Go to the writing desk')
    print ('5 - Go to the bookcase')
    print ('6 - Exit the room')
    print (' ')
    choice = input('What do you do ' + player_name + '?  ')
    while len(choice) != 1:
        choice = input(player_name + ' you must decide what to do!  ')
    if choice == '6':
        print (player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
        rpg()
    elif choice == '1':
        print ('You lean down and pick up the matches off of the floor')
        matches = True
        chair(player_name,book,glasses,key,matches,papers)
    elif choice == '2':
        end_table(player_name,book,glasses,key,matches,papers)
    elif choice == '3':
        dining_table(player_name,book,glasses,key,matches,papers)
    elif choice == '4':
        writing_desk(player_name,book,glasses,key,matches,papers)
    elif choice == '5':
        bookcase(player_name,book,glasses,key,matches,papers)
    else:
        print ('Please make a valid selection')
        chair(player_name,book,glasses,key,matches,papers)


#  Function for the user to look at the end table
def end_table(player_name,book,glasses,key,matches,papers):
	if(book):
		print(' ')
		print ('As you look at the end table you see a music box.  As you look closer you see what appears to be the outline of a book around it in the dust.  You think you could place the book "The song of the Grail" under the music box in that spot')
		print ('1 - Place "The Song of the Grail" book under the music box')
		print ('2 - Go to the dining table')
		print ('3 - Go to the writing desk')
		print ('4 - Go to the bookcase')
		print ('5 - Sit in the chair')
		print ('6 - Exit the room')
		print (' ')
		choice = input('What do you do ' + player_name + '?  ')
		while len(choice) != 1:
			choice = input(player_name + ' you must decide what to do!  ')
		if choice == '6':
			print (player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
			menu()
		elif choice == '1':
			print(' ')
			print ('As you set the music box on top of the book you hear something like it starts to try playing, but something is stopping		it')
			print ('1 - Open the music box and see if you can figure out how to make it play')
			print ('2 - Go to the dining table')
			print ('3 - Go to the writing desk')
			print ('4 - Go to the bookcase')
			print ('5 - Sit in the chair')
			print ('6 - Exit the room')
			print (' ')
			choice = input('What do you do ' + player_name + '?  ')
			while len(choice) != 1:
				choice = input(player_name + ' you must decide what to do!  ')
			if choice == '6':
				print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
				rpg()
			elif choice == '1':
				print('When you open the lid of the music box you see a small key jammed into the gears.  As you pull the key out it starts playing "The Knights Who Say Ni".  You keep the key wondering if it might be useful later')
				key = True
				end_table(player_name,book,glasses,key,matches,papers)
			elif choice == '2':
				dining_table(player_name,book,glasses,key,matches,papers)
			elif choice == '3':
				writing_desk(player_name,book,glasses,key,matches,papers)
			elif choice == '4':
				bookcase(player_name,book,glasses,key,matches,papers)
			elif choice == '5':
				chair(player_name,book,glasses,key,matches,papers)
		elif choice == '2':
			dining_table(player_name,book,glasses,key,matches,papers)
		elif choice == '3':
			writing_desk(player_name,book,glasses,key,matches,papers)
		elif choice == '4':
			bookcase(player_name,book,glasses,key,matches,papers)
		elif choice == '5':
			chair(player_name,book,glasses,key,matches,papers)
	else:
		print(' ')
		print('As you look at the end table you see a music box.  AS you look closer you see what appears to be the outline of a book around it in the dust.  You wonder if there is a book somewhere that was moved for some reason.')
		print ('1 - Go to the dining table')
		print ('2 - Go to the writing desk')
		print ('3 - Go to the bookcase')
		print ('4 - Sit in the chair')
		print ('5 - Exit the room')
		print (' ')
		choice = input('What do you do ' + player_name + '?  ')
		while len(choice) != 1:
			choice = input(player_name + ' you must decide what to do!  ')
		if choice == '5':
			print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
			rpg()
		elif choice == '1':
			dining_table(player_name,book,glasses,key,matches,papers)
		elif choice == '2':
			writing_desk(player_name,book,glasses,key,matches,papers)
		elif choice == '3':
			bookcase(player_name,book,glasses,key,matches,papers)
		elif choice == '4':
			chair(player_name,book,glasses,key,matches,papers)
		else:
			print ('Please make a valid selection')
			end_table(player_name,book,glasses,key,matches,papers)


#  Function to go into the secret room
def secret_room(player_name):
    print(' ')
    print('As you walk through the door and look around you see King Arthur\'s sword hanging in a weapons rack and THe Holy Grail sitting on a table')
    print('1 - Take King Arthur\'s Sword')
    print('2 - Take The Holy Grail')
    print('3 - Exit the room')
    print(' ')
    choice = input('What do you do ' + player_name + '?  ')
    while len(choice) != 1:
        choice = input(player_name + ' you must decide what to do!  ')
    if choice == '3':
        print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
        menu()
    elif choice == '1':
        print('You pick up King Arthur\'s sword and feel magic course through your veins urging you onward.  Come back tomorrow to continue your quest brave adventurer.')
        menu()
    elif choice == '2':
        print('Congratulations ' + player_name + '!  You have completed the quest and proven yourself to be a brave adventurer!  Bards will sing your praises for years to come!')
        menu()

menu()
