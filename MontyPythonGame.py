#  AUTHOR:  Michael O'Brien
#  CREATED:  05 April 2018
#  MODIFIED:  10 May 2018
#  DESCRIPTION:  Monty Python text games


#  Import the random function to generate a random number for the guessing game
import random


#  Import the date and time module for the output to the text file scoring of the skit guessing game
from datetime import datetime


#  Load the dictionary with the season1Episodes from season 11
season1Episodes = {"It's Wolfgang Amadeus Mozart":1, "Famous Deaths":1, "Italian Lesson":1, "Whizzo Butter":1, "It's the Arts":1, "Arthur 'Two-Sheds' Jackson":1, "Picasso/Cycling Race":1, "The Funniest Joke in the World":1, "Flying Sheep":2, "French Lecture on Sheep-Aircraft":2, "A Man with Three Buttocks":2, "A Man with Two Noses":2, "Musical Mice":2, "Marriage Guidance Councellor":2, "The Wacky Queen":2, "Working-Class Playwright":2, "A Scotsman on a Horse":2,"the Wrestling Epilogue":2, "The Mouse Problem":2, "Court Scene":3, "The Larch":3, "Bicycle Repairman":3, "Children's Stories":3, "Restaurant Sketch":3, "Seduced Milkmen":3, "Stolen Newsreader":3, "Children's Interview":3, "Nudge, Nudge":3, "Song":4, "Art Gallery":4, "Art Critic":4, "It's a Man's Life in the Modern Army":4, "Undressing in Public":4, "Self-Defense Against Fresh Fruit":4, "Secret Service Dentists":4, "Confuse-a-Cat":5, "The Smuggler":5, "A Duck, a Cat and a Lizard":5, "Vox Pops on Smuggling":5, "Police Raid":5, "Letters and Vox Pops":5, "Newsreader Arrested":5, "Erotic Film":5, "Silly Job Interview":5, "Careers Advisory Board":5, "Burglar/Encyclopaedia Salesman":5, "Johann Gombolputty.... von Hautkopf of Ulm":6, "Non-illegal Robbery":6, "Vox Pops":6, "Crunchy Frog":6, "The Dull Life of a City Stockbroker":6, "Red Indian in Theatre":6, "Policemen Make Wonderful Friends":6, "A Scotsman on a Horse":6, "Twentieth-Century Vole":6, "Camel Spotting":7, "You're No Fun Anymore":7, "The Audit":7, "Science Fiction Sketch":7, "Man Turns Into Scotsman":7, "Police Station":7, "Blancmanges Playing Tennis":7, "Army Protection Racket":8, "Vox Pops":8, "Art Critic - the Place of the Nude":8, "Buying a Bed":8, "Hermits":8, "Dead Parrot (Petshop)":8, "The Flasher":8, "Hell's Grannies":8, "Llamas":9, "A Man with a Tape Recorder up His Nose":9, "Kilimanjaro Expedition":9, "A Man with a Tape Recorder up His Brother's Nose":9, "Homicidal Barber":9, "Lumberjack Song":9, "Gumby Crooner":9, "The Refreshment Room at Bletchley":9, "Hunting Film":9, "The Visitors":9, "Walk-on-Part in Sketch":10, "Bank Robber":10, "Trailer":10, "Arthur Tree":10, "Vocational Guidance Counsellor":10, "The First Man to Jump the Channel":10, "Tunnelling from Godalming to Java":10, "Pet Conversions":10, "Gorilla Librarian":10, "Letters to 'Daily Mirror'":10, "Strangers in the Night":10, "Letters":11, "Interuptions":11, "Agatha Christie Sketch":11, "Undertakers File 1 Literary Football Discussion": 11, "Interesting People":11, "Eighteenth-Century Social Legislation":11, "The Battle of Trafalgar":11, "Batley Townswomens' Guild Presents the Battle of Pearl Harbour":11, "Undertakers Film 2":11, "Falling From Buildings":12, "'Spectrum' -  Talking About Things":12, "Visitors from Coventry":12, "Mr Hitler":12, "The North Minehead By-Election":12, "Police Station":12, "Upperclass Twit of the Year":12, "Ken Shabby":12, "How Far Can a Minister Fall?":12, "Intermissions":13, "Restaurant":13, "Advertisments":13, "Albatross":13, "Come Back to My Place":13, "Me Doctor":13, "Historical Impersonations":13, "Quiz Programme - 'Wishes'":13, "'Probe-Around' on Crime":13, "Stonehenge":13, "Mr Attila the Hun":13, "Psychiatry - Silly Sketch":13, "Operating Theatre":13}
season2Episodes ={"Face the Press":1, "New Cooker Sketch":1, "Tobacconist's (Prostitute Advert)":1, "The Ministry of Silly Walks":1, "La March Futile":1, "Ethel the Frog/Piranha Brothers":1, "Man-Powered Flight":2, "The Spanish Inquisition":2, "Jokes and Novelties Salesman":2, "Tax on Thingy":2, "Vox Pops on Taxation":2, "Photos of Uncle Ted":2, "The Spanish Inquisition (continued)":2, "The Semaphore Version of Wuthering Heights":2, "Julius Caesar on an Aldis lamp":2, "Gunfight at the O.K. Corral in Morse Code":2, "Smoke signal version of Gentlemen Prefer Blondes":2, "Court Charades":2, "Race Against the Credits":2, "A Bishop Rehearsing":3, "Flying Lessons":3, "Hijacked Plane":3, "The Poet Ewan McTeagle":3, "Hand Trees (Animation)":3, "Psychiatrist Milkman":3, "Complaints":3, "Déjà Vu":3, "An apology":4, "Gumby announcement":4, "Architects Sketch":4, "How to Recognize a Mason":4, "An apology/Another Gumby announcement":4, "Motor Insurance Sketch":4, "The Bishop":4, "Living Room on Pavement":4, "Poets":4, "A Choice of Viewing":4, "An Interview with a Nude Man":4, "The Bishop...Again?!":4, "An apology":4, "Gumby Frog Curse/Another Another Gumby Announcement":4, "Chemist Sketch":4, "An Apology/Words Not to be Used Again":4, "A Less Naughty Chemist's":4, "A Not At All Naughty Chemist's":4, "Vox Pops on After-shave":4, "Police Constable Pan-Am":4, "Another Apology":4, "End Credits":4, "Last Gumby announcement (The end)":4, "Live From the Grill-o-Mat":5, "The First Item...":5, "Blackmail":5, "Society for Putting Things on Top of Other Things":5, "Escape from Film":5, "The Next Item (or dish)...":5, "Current Affairs":5, "Continued from the Escape from Film":5, "The Next Item (...Prawn Salad...?)...":5, "Accidents Sketch (Prawn Salad Ltd.)":5, "Interruption":5, "Seven Brides for Seven Brothers":5, "The Butcher Who is Alternately Rude and Polite":5, "The Last Item (coffee)...":5, "Ken Clean-Air System":5, "On the Bus (end credits)":5, '"It\'s a Living"':6, "The Time on BBC 1":6, "School Prize-Giving":6, '"if...."':6, '"Rear Window"':6, '"Finian\'s Rainbow"':6, "The Foreign Secretary and Other News":6, 'Free Dung from the "Book of the Month" Club':6, "Dead Indian":6, "Timmy Williams interview":6, "Raymond Luxury Yacht":6, "Marriage Registry office":6, "Election Night Special":6, '"The Attila the Hun Show"':7, "Attila the Nun":7, "Secretary of State Striptease":7, "Vox Pops on Political Groupies":7, "Ratcatcher":7, "Wainscotting":7, "Killer Sheep":7, "The News for Parrots":7, "The News for Gibbons":7, "Today in Parliament":7, "The News for Wombats":7, "Attila the Bun":7, "The Idiot in the Rural Society":7, "Test Match Against Iceland":7, "The Epsom Furniture Race":7, '"Spot The Braincell"':7, "Trailer":8, '"Archaeology Today"':8, "Silly Vicar and Leapy Lee":8, "Registrar (wife swap)":8, "Silly doctor sketch (immediately abandoned)":8, "Mr. and Mrs. Git":8, "Roy and Hank Spim – Mosquito hunters":8, "Poofy Judges":8, "Mrs. Thing and Mrs. Entity":8, "Beethoven's Mynah Bird":8, "Shakespeare":8, "Michelangelo":8, 'Colin "Chopper" Mozart (ratcatcher)':8, "Judges":8, 'How to Recognise Different Parts of the Body"':9, "Bruces sketch":9, "Naughty Bits":9, "The Man who Contradicts People":9, "Cosmetic Surgery":9, "Camp Square-Bashing":9, "Killer Cars (Animation)":9, "Cut-Price Airline":9, "Batley Townswomen's Guild Presents the First Heart Transplant":9, "The First Underwater Production of Measure for Measure":9, "The Death of Mary Queen of Scots":9, "Exploding Penguin on the TV Set":9, "There's Been a Murder":9, "Sgt. Duckie's Song":9, '"Bing Tiddle Tiddle Bong"':9, "French Subtitled Film":10, "Scott of the Antarctic":10, "Scott of the Sahara":10, "Conrad Poohs and His Dancing Teeth":10, "Fish Licence":10, "Derby Council v. All Blacks Rugby Match":10, "Long John Silver Impersonators v. Bournemouth Gynaecologists":10, "Conquistador Coffee Campaign":11, "Repeating Groove":11, "Ramsay MacDonald Striptease":11, "Job Hunter":11, "International Chinese Communist Conspiracy": 11, "Crelm Toothpaste / Shrill Petrol":11, "Agatha Christie Sketch (railway timetables)":11, "Mr Neville Shunte-Railroad Playwright":11, "Gavin Millarrrrrrrrr Writes":11, "Film Director/Dentist Martin Curry (teeth)":11, "City Gents Vox Pops":11, "Crackpot Religions Ltd":11, "How Not to Be Seen":11, "Crossing the Atlantic on a Tricycle":11, "Interview in Filing Cabinet":11, '"Yummy Yummy Yummy, I\'ve Got Love in My Tummy"':11, "Monty Python's Flying Circus Again in Thirty Seconds":11, '"The Black Eagle"':12, "Dirty Hungarian Phrasebook":12, "Court (phrasebook)":12, "World Forum – Communist Quiz":12, '"Ypres 1914" (abandoned)':12, "Art Gallery Strikes":12, '"Ypres 1914"':12, "Hospital for Over-Actors":12, "Gumby Flower Arranging":12, "Spam":12, "The Queen Will Be Watching":13, "Coal Mine in Llanddarog Carmarthen":13, "The Man Who Says Things in a Very Roundabout Way":13, "Commercials":13, "How to Feed a Goldfish":13, "The Man Who Collects Birdwatcher's Eggs":13, "Insurance Sketch":13, "Hospital Run by RSM":13, "Mountaineer":13, 'Exploding Version of "The Blue Danube"':13, "Girls Boarding School":13, "Submarine":13, "A Man with a Stoat Through His Head":13, "Lifeboat (cannibalism)":13, "Undertakers sketch":13}
season3Episodes ={"Njorl's Saga/Opening Credits":1, "Multiple Murderer Court Scene":1, "Investigating the body":1, "Njorl's Saga – part II":1, "A Terrible Mess":1, "Njorl's Saga – part II: North Malden?":1, "Starting Over":1, "Njorl's Saga – part II: Invest in Malden?":1, "Phone conversation about the word 'Maiden' in the saga":1, "Eric Njorl Court Scene (Njorl's Saga – part III)":1, "Stock Exchange Report":1, "Mrs. Premise and Mrs. Conclusion at the Launderette":1, "Mrs. Premise and Mrs. Conclusion at North Malden":1, "Back to the saga":1, "Njorl's Saga – part IV: Mrs. Premise and Mrs. Conclusion visit Sartre in Paris":1, "Whicker's World":1, "Emigration from Surbiton to Hounslow":2, "Schoolboys' Life Assurance Company":2, "How to Do It":2, "Mrs. Niggerbaiter Explodes":2, "Vicar/Salesman":2, "Farming Club":2, '"Life of Tschaikowsky"':2, "Trim-Jeans Theatre":2, "The Fish-Slapping Dance":2, "World War II":2, "Titanic Sinking":2, "The BBC is Short of Money":2, "SS Mother Goose":2, "It's Man Show":2, "The Money Programme":3, "Money Song":3, "Erizabeth L":3, "Fraud Film Director Squad":3, "Hands Up":3, "Dead Bishop, AKA Church Police or Salvation Fuzz":3, "Jungle Restaurant":3, "Apology for Violence and Nudity":3, 'Ken Russell\'s "Gardening Club"':3, "The Lost World of Roiurama":3, "Six More Minutes of Monty Python's Flying Circus":3, "The Argument Skit":3, "Hitting on the Head Lessons":3, "Inspector Flying Fox of the Yard":3, "One More Minute of Monty Python's Flying Circus":3, "Blood, Devastation, Death, War and Horror":4, "The Man Who Speaks in Anagrams":4, "Anagram Quiz":4, "Merchant Banker":4, "Pantomime Horses":4, "Life and Death Struggles":4, "Househunters":4, "Mary Recruitment Office":4, "Bus Conductor Sketch":4, "The Man Who Makes People Laugh Uncontrollably":4, "Army Captain as Clown":4, "Gestures to Indicate Pauses in a Televised Talk":4, "Neurotic Announcers":4, "The News with Richard Baker":4, "The Pantomime Horse is a Secret Agent":4, "Summarize Proust Competition":5, "Hairdressers Climb Up Mount Everest":5, "A Magnificent Festering":5, "Fire Brigade":5, "Our Eamonn":5, '"Party Hints"':5, "Language Laboratory":5, "Travel Agent":5, "Watney's Red Barrel":5, "Anne Elk's Theory on Brontosauruses":5, "Tory Housewives Clean-up Campaign":6, "Gumby Brain Specialist":6, "Molluscs":6, "Report on the Minister reports":6, "Tuesday Documentary":6, "Children's Story":6, "Match of the Day":6, "An Apology":6, "Expedition to Lake Pahoe":6, "The Silliest Interview We've Ever Had":6, "The Silliest Sketch We've Ever Done":6, "Biggles Dictates a Letter":7, "Climbing the North Face of the Uxbridge Road":7, "Lifeboat":7, "Old lady snoopers":7, "Storage Jars":7, "TV is Bad For Your Eyes":7, "The Show so Far":7, "Cheese Shop sketch":7, "Philip Jenkinson on Cheese Westerns":7, 'Sam Peckinpah\'s "Salad Days"':7, "Apology":7, "The News with Richard Baker":7, "Seashore Interlude Film":7, "Mr. Pither":8, "Mr. Gulliver (who thinks he is Clodagh Rodgers)":8, "Trotsky":8, "Smolensk":8, "Bingo-Crazed Chinese":8, "Not Secret Police":8, "Trotsky / Eartha Kitt":8, "Firing Squad":8, "Eartha Kitt / Edward Heath":8, "Narrow Escape/Credits":8, 'Monsters dance to "Jack in the Box"':8, "Bomb on Plane":9, "A Naked Man":9, "Ten Seconds of Sex":9, "Housing Project Built by Characters from Nineteenth-century English Literature":9, "M1 Interchange Built by Characters from 'Paradise Lost'":9, "Mystico and Janet – Flats Built by Hypnosis":9, "Mortuary Hour":9, "The Olympic Hide-and-seek Final":9, "The Cheap-Laughs":9, "Bull-fighting":9, "The British Well-Basically Club":9, "Prices on the Planet Algon":9, "Mr. Badger Reads the Credits":9, "Tudor Jobs Agency":10, "Pornographic Bookshop":10, "Elizabethan Pornography Smugglers":10, "Silly Disturbances":10, "The Free Repetition of Doubtful Words Sketch":10, "'Is There?'... Life after Death?":10, "The Man Who Says Words in the Wrong Order":10, "Thripshaw's Disease":10, "Silly Noises":10, "Sherry-drinking Vicar":10, '"Boxing Tonight"':11, "Dennis Moore":11, "What the Stars Foretell":11, "Doctor":11, "TV4 or Not TV4 Discussion":11, "Lupins":11, "Ideal Loon Exhibition":11, "Off-Licence":11, "Dennis Moore Rides Again":11, "Prejudice":11, "Redistribution of Wealth":11, "Party Political Broadcast":12, 'A Book at Bedtime – "Redgauntlet"':12, "Kamikaze Scotsmen":12, "No Time to Lose":12, "Frontiers of Medicine – Penguins":12, "BBC programme planners":12, "Unexploded Scotsmen":12, "Spot the Looney":12, "Rival Documentaries":12, "Dad's Doctors, Dad's Pooves and Other Interesting Stories":12, "Thames TV Introduction, with (the real) David Hamilton":13, '"Light Entertainment Awards" with Dickie Attenborough':13, "Dickie Attenborough":13, "The Oscar Wilde Sketch":13, "Charwoman":13, "David Niven's Fridge":13, 'Pasolini\'s Film "The Third Test Match"':13, "New Brain from Currys":13, "Blood Donor":13, "International Wife-Swapping":13, "Credits of the Year":13, "The Dirty Vicar Sketch":13 }
season4Episodes ={"The Montgolfier Brothers":1, "Montgolfier Brothers in Love":1, "Louis XVI":1, "The Court of George III":1, "Party Political Broadcast on Behalf of the Norwegian Party":1, "Zeppelin":1, "The Golden Age of Colonic Irrigation":1, "Department Store":2, "Buying an Ant":2, "At Home with the Ant and Other Pets":2, "Documentary on Ants":2, "Ant Complaints":2, "Ant Poetry Reading":2, "Toupee Deparment":2, "Different Endings":2, "Up Your Pavement":3, "RAF Banter":3, "Trivializing the War":3, "Court-Martial":3, "Basingstoke in Westphalia":3, "Anything Goes":3, "Film Trailer":3, "The Public Are Idiots":3, "Programme Titles Conference":3, "The Last Five Miles":3, "Wooday and Tinny Words":3, "Show-Jumping":3, "Newsflash":3, "When Does a Dream Begin?":3, "Bogus Psychiatrists":4, "Nationwide":4, "Police helmets":4, "Father-in-Law":4, "Hamlet and Ophelia":4, "Boxing Match Aftermath":4, "Boxing Commentary":4, "Piston Engine (a Bargain)":4, "A Room in Polonius's House":4, "Dentists":4, "Live from Epsom – Jockey Interviews":4, "Queen Victoria Handicap":4, "And then...":4, "Post-Box Ceremony":5, "Mr. Neutron":5, "F.E.A.R. / Mr. Neutron Is Missing!":5, "Teddy Salad":5, "Secretary of State and Prime Minister":5, "Bombing":5, "Mrs. Scum":5, "Teddy Salad Explodes":5, "Mr. Neutron Escapes":5, "Conjuring Today":5, "Most Awful Family in Britain":6, "Icelandic Honey Week":6, "Patient Abuse":6 "Brigadier and Bishop":6, "Appeal on Behalf of Extremely Rich People":6, "The Man Who Finishes Other People's Sentences":6, "David Attenborough":6, "The Walking Trees of Dahomey":6, "Batsmen of the Kalahari":6, "Cricket Match (assegais)":6, "BBC News (handovers)":6}

#  Global variables to be used by the adventure RPG to track success
book = False
glasses = False
key = False
matches = False
papers = False


#  Function to clear the screen
def cls():
    print('\n')*80


# -----  BEGINNING 0F SKIT GUESSING GAME  ----- #

#  Function with instructions for the SKIT GUESSING GAME
def skit_guess_instructions():
    print(' ')
    print('SKIT GUESSING GAME')
    print(' ')
    print('In this game I will give you the name of a skit and you have to guess the episode number that the skit aired in')
    print(' ')
    print('1 - Play the game')
    print('2 - See current scores of players')
    print('3 - Return to the Monty Python game choice menu')
    print(' ')
    choice = input ('What would you like to do?  ')
    while len(choice) != 1:
        choice = input('Please make a choice on what you want to do:  ')
    if int(choice) == 1:
        player_name = input('Enter your name to test your knowledge in the Monty Python skit guessing game:  ')
        while len(player_name) < 1:
            player_name = input('If you want to test your knowledge of Monty Python skits you must enter your name:  ')
        number_correct = 0
        number_incorrect = 0
        episodesChoice = 0
        print("What series would you like to guess skits from?")
        skitChoice = input("Enter a number between 1-4:  ")
        while len(skitChoice) != 1:
            skitChoice = input("You need to enter and episode between 1-4:  ")
        if skitChoice == "1":
            episodesChoice = season1Episodes
        elif skitChoice == "2":
            episodesChoice = season2Episodes
        elif skitChoice == "3":
            episodesChoice = season3Episodes
        elif skitChoice == "4":
            episodesChoice = season4Episodes
        skit_guess_game(player_name, number_correct, number_incorrect, episodesChoice)
    elif int(choice) == 2:
        print('PREVIOUS SCORES')
        print(' ')
        scoresFile = open ('scores.txt', 'r')
        highScores = scoresFile.read()
        print(highScores)
        scoresFile.close()
        skit_guess_instructions()
    elif int(choice) == 3:
        menu()
    else:
        print('Please make a valid selection')
        skit_guess_instructions()


#  Function to play the SKIT GUESSING GAME
def skit_guess_game(player_name, number_correct, number_incorrect, episodesChoice):
    episode_name, episode_number = random.choice(list(episodesChoice.items()))
    print(' ')
    print('What episode did skit ' + episode_name + ' appear in?')
    print(' ')
    player_guess = input('Enter an episode number between 1-13 or 14 to exit:  ')
    while int(player_guess) < 1:
        player_guess = input('You must enter an episode number between 1-13 or 14 to exit:  ')
    if int(player_guess) in range(1,15):
        if int(episode_number) == int(player_guess):
            print("CORRECT!  " + episode_name + ' appeared in episode ' + str(episode_number))
            print(' ')
            number_correct = number_correct + 1
            skit_guess_game(player_name, number_correct, number_incorrect, episodesChoice)
        elif int(player_guess) != 14:
            print('Wrong, ' + episode_name + ' appeared in episode ' + str(episode_number))
            print(' ')
            number_incorrect = number_incorrect + 1
            skit_guess_game(player_name, number_correct, number_incorrect, episodesChoice)
        elif int(player_guess) == 14:
            scoresFile = open('scores.txt','a')
            number_correct = player_name + ':  ' + str(number_correct) + ' correct'
            print(number_correct)
            number_incorrect = player_name + ':  ' + str(number_incorrect) + ' incorrect'
            print(number_incorrect)
            print(' ')
            date_played = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            scoresFile.write(date_played+'\n')
            scoresFile.write(number_correct+'\n')
            scoresFile.write(number_incorrect+'\n')
            scoresFile.close()
            menu()
    else:
        print('Please make a valid selection between 1-14')
        skit_guess_game(player_name, number_correct, number_incorrect, episodesChoice)


# -----  BEGINNING 0F HANGMAN GAME  ----- #

#  HANGMAN INSTRUCTIONS FUNCTION
def hangmanInstructions():
    instructions = open('hangman_instructions.txt', 'r')
    hangmanInstructions = instructions.read()
    print(hangmanInstructions)
    instructions.close()
    hangmanGame()


#  HANGMAN GAME FUNCTION
def hangmanGame():
    hangmanPics = [
        '''
              +---+
              |   |
                  |
                  |
                  |
                  |
             =========''', '''

           +---+
           |   |
           O   |
               |
               |
               |
         =========''', '''

           +---+
           |   |
           O   |
           |   |
               |
               |
         =========''', '''

           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========''', '''

           +---+
           |   |
           O   |
          /|\  |
               |
               |
         =========''', '''

           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
         =========''', '''

           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
         ========='''
    ]

    import random
    words = ("CAMELOT", "ROBIN", "MINSTREL", "BRING OUT YER DEAD", "THE MEANING OF LIFE", "SIR GALAHAD", "THE LIFE OF BRIAN", "CASTLE", "SIR BEDEVERE", "BROTHER MAYNARD", "HOLY GRAIL", "MONTY PYTHON", "KING ARTHUR", "FLYING CIRCUS", "SIR LANCELOT", "BLACK KNIGHT", "LUMBERJACK")
    print('H A N G M A N')
    missedLetters = ''
    correctLetters = ''
    secretWord = random.choice(words)
    gameIsOver = False

    while not gameIsOver:
        displayBoard(hangmanPics, missedLetters, correctLetters, secretWord)
        guess = getGuess(missedLetters + correctLetters)
        if guess in secretWord:
            correctLetters = correctLetters + guess
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes!  The secret word was ' + secretWord + '.  You win.')
                gameIsOver = True
        else:
            missedLetters = missedLetters + guess
            if len(missedLetters) == len(hangmanPics) - 1:
                displayBoard(hangmanPics, missedLetters, correctLetters, secretWord)
                print('You are out of guesses.  The secret word was ' + secretWord + '.  Sorry, you lose.')
                gameIsOver = True
        if gameIsOver:
            if playAgain():
                hangmanGame()
            else:
                print('I hope you enjoyed Monty Python Hangman.')
                menu()


#  DISPLAY THE BOARD FUNCTION
def displayBoard(hangmanPics, missedLetters, correctLetters, secretWord):
    print(hangmanPics[len(missedLetters)])
    print()
    print('Missed Letters:  ')
    for letter in missedLetters:
        print(letter, end=" ")
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter, end=' ')
    print()


#  GET GUESS FUNCTION - CHECKS TO MAKE SURE INPUT IS A SINGLE LETTER
def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter:  ')
        guess = guess.upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter.  Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
            print('Please enter only letters.')
        else:
            return guess


#  PLAY AGAIN FUNCTION
def playAgain():
    print()
    print('Do you want to play again?  (Yes/No)  ')
    return input().lower().startswith('y')

# -----  BEGINNING 0F RPG ADVENTURE GAME  ----- #

#  Function to start the adventure RPG
def rpg():
    print(' ')
    print('ADVENTURE ROLEPLAYING GAME TO FIND THE HOLY GRAIL')
    print(' ')
    rpg_instructions = open('rpg_instructions.txt','r')
    rpgInstructions = rpg_instructions.read()
    print(rpgInstructions)
    rpg_instructions.close()
    print(' ')
    play = input('Enter "P" to play the game or "Q" to return to the game menu:  ')
    while len(play) != 1:
        play = input('Please enter "P" to paly or "Q" to return to the game menu:  ')
    if play.upper() == "Q":
        menu()
    elif play.upper() == "P":
        print(' ')
        player_name = input('Enter your name brave adventurer to begin the quest:  ')
        while len(player_name) < 1:
            player_name = input('If you are brave enough to take on the quest you must enter your name:  ')
        enter_building(player_name)
    else:
        print('You need to make a valid selection')
        rpg()


#  Function to see if the user enters the building
def enter_building(player_name):
    print(' ')
    print('As you are walking through the village you see a decrepit building with a dusty sign hanging loosely in front of it.  Through the dust you can make out "Those who seek the Holy Grail may enter if they feel worthy."')
    print('1 - Walk through the door?')
    print('2 - Continue through the village?')
    print(' ')
    choice = input('What do you do ' + player_name +'?  ')
    while len(choice) != 1:
        choice = input(player_name + ' you must decide what to do!  ')
    if choice == '2':
        print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
        menu()
    elif choice == '1':
        print(' ')
        print('The door creaks open, scraping the floor from disuse as you enter the building.  In a moment you eyes adjust to the dimly lit room:')
        print('1 - Look around the room?')
        print('2 - Leave?')
        print(' ')
        choice = input('What do you do ' + player_name + '?  ')
        while len(choice) != 1:
            choice = input(player_name + ' you must decide what to do!  ')
        if choice == '2':
            print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
            rpg()
        elif choice == '1':
            room(player_name)
        else:
            print('Please make a valid selection')
            enter_building(player_name)
    else:
        print('Pleae make a valid selection')
        enter_building(player_name)
        

#  Function to look around the room
def room(player_name):
    print(' ')
    print('As you gaze around the room you see a bookcase against the wall, writing table in the corner, an end table next to the bookcase, a dining table, and a chair partially pulled out from the dining table')
    print('You can see objects scattered around the room but are too far away to tell what any of them are')
    print('1 - Look at the end table')
    print('2 - Look at the dining table')
    print('3 - Look at the writing desk')
    print('4 - Look at the bookcase')
    print('5 - Sit in the chair')
    print('6 - Exit the room')
    print(' ')
    choice = input('What do you do ' + player_name + '?  ')
    while len(choice) != 1:
        choice = input(player_name + ' you must decide what to do!  ')
    if choice == '6':
        print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
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
        print('you didn not make a valid selection')
        room(player_name)


#  Function for the user to look at the bookcase for the book
def bookcase(player_name,book,glasses,key,matches,papers):
    print(' ')
    if(papers):
        print('As you approach the bookcase you see shelves of books on the shelves covered in dust and cobwebs.  Scanning the titles you see one titled "The song of the Grail".')
        print('1 - Take the book')
        print('2 - Look at the end table')
        print('3 - Look at the dining table')
        print('4 - Look at the writing_desk')
        print('5 - Sit in the chair')
        print(' ')
        choice = input('What do you do ' + player_name + '?  ')
        while len(choice) != 1:
            choice = input(player_name + ' you must decice what to do!  ')
        if choice == '1':
            print('You now have the book titled "The song of the Grail".')
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
            print('Please make a valid selection')
            bookcase(player_name,book,glasses,key,matches,papers)
    else:
        print("As you approach the bookcase you see shelves of books on the shelves covered in dust and cobwebs.  You read some of the titles but don't know which book to choose.")
        print('1 - Look at the end table')
        print('2 - Look at the dining table')
        print('3 - Look at the writing desk')
        print('4 - Sit in the chair')
        print(' ')
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
            print('Please make a valid selection')
            bookcase(player_name,book,glasses,key,matches,papers)


#  Function for the user to look at the writing desk and find the glasses
def writing_desk(player_name,book,glasses,key,matches,papers):
    print(' ')
    print('When you get to the writing desk you see a pair of glasses lying on the desk')
    print('1 - Take the glasses')
    print('2 - Look at the end table')
    print('3 - Look at the dining table')
    print('4 - Look at the bookcase')
    print('5 - Sit in the chair')
    print('6 - Exit the room')
    print(' ')
    choice = input('What do you do ' + player_name + '?  ')
    while len(choice) != 1:
        choice = input(player_name + ' you must decide what to do!  ')
    if choice == '6':
        print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
        rpg()
    elif choice == '1':
        print('You pick up the glasses')
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
    print(' ')
    print('As you approach the table you see some papers lying on the corner of the table and a candle in the center of the table')
    print('1 - Look at the documents')
    print('2 - Light the candle')
    print('3 - Look at the end table')
    print('4 - Look at the writning desk')
    print('5 - Look at the bookcase')
    print('6 - Sit in the chair')
    print('7 - Exit the room')
    print(' ')
    choice = input('What do you do ' + player_name + '?  ')
    while len(choice) != 1:
        choice = input(player_name + ' you must decide what to do!  ')
    if choice == '7':
        print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
        rpg()
    elif choice == '1':
        if (glasses):
            print('The papers say "Guide to Finding the Holy Grail"')
            print('As you read the guide it tells you "Whiile I haven\'t figured out everything yet in my search I have determined that I need to light a candle to reveal a hidden door.  I\'m not sure how all of this ties together bue apparantly there is also a music box, a key, and a book called "The song of the Grail" that will also aid in my quest.')
            papers = True
            dining_table(player_name,book,glasses,key,matches,papers)
        else:
            print('The documents appear blurry and you are unable to read them right now.')
            dining_table(player_name,book,glasses,key,matches,papers)
    elif choice == '2':
        if(matches) and (key):
            print('You light the candle.  As the flame from the candle illuminates the wall next to the bookcase you see a shadow flickering in the flame that looks like a keyhole. ')
            print(' ')
            print('1 - Go to the secret door')
            print('2 - keep looking around')
            choice = input('What do you do ' + player_name +'?  ')
            while len(choice) != 1:
                choice = input(player_name + 'you must decide what to do!  ')
            if choice == '1':
                secret_room(player_name)
            elif choice == '2':
                dining_table(player_name,book,glasses,key,matches,papers)
            else:
                print('Please make a valid selection')
                dining_table(player_name,book,glasses,key,matches,papers)
        else:
            print('You feel you need the matches and something else before you light the candle')
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
        print('you didn not make a valid selection')
        dining_table(player_name,book,glasses,key,matches,papers)


#  Function for the user to sit in the chair and find the matches
def chair(player_name,book,glasses,key,matches,papers):
    print(' ')
    print('As you pull the chair out sit in the chair you notice something on the floor.  Looking closer you see a box of matches.')
    print('1 - Take the matches')
    print('2 - Go to the end table')
    print('3 - Go to the dining table')
    print('4 - Go to the writing desk')
    print('5 - Go to the bookcase')
    print('6 - Exit the room')
    print(' ')
    choice = input('What do you do ' + player_name + '?  ')
    while len(choice) != 1:
        choice = input(player_name + ' you must decide what to do!  ')
    if choice == '6':
        print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
        rpg()
    elif choice == '1':
        print('You lean down and pick up the matches off of the floor')
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
        print('Please make a valid selection')
        chair(player_name,book,glasses,key,matches,papers)


#  Function for the user to look at the end table
def end_table(player_name,book,glasses,key,matches,papers):
    if(book):
        print(' ')
        print('As you look at the end table you see a music box.  As you look closer you see what appears to be the outline of a book around it in the dust.  You think you could place the book "The song of the Grail" under the music box in that spot')
        print('1 - Place "The Song of the Grail" book under the music box')
        print('2 - Go to the dining table')
        print('3 - Go to the writing desk')
        print('4 - Go to the bookcase')
        print('5 - Sit in the chair')
        print('6 - Exit the room')
        print(' ')
        choice = input('What do you do ' + player_name + '?  ')
        while len(choice) != 1:
            choice = input(player_name + ' you must decide what to do!  ')
        if choice == '6':
            print(player_name + ' it appears you are not worthy of finding the Holy Grail after all.')
            menu()
        elif choice == '1':
            print(' ')
            print('As you set the music box on top of the book you hear something like it starts to try playing, but something is stopping		it')
            print('1 - Open the music box and see if you can figure out how to make it play')
            print('2 - Go to the dining table')
            print('3 - Go to the writing desk')
            print('4 - Go to the bookcase')
            print('5 - Sit in the chair')
            print('6 - Exit the room')
            print(' ')
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
        print('1 - Go to the dining table')
        print('2 - Go to the writing desk')
        print('3 - Go to the bookcase')
        print('4 - Sit in the chair')
        print('5 - Exit the room')
        print(' ')
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
            print('Please make a valid selection')
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


# -----  MAIN GAME CHOICE MENU  ----- #

#  Function to display the user menu for searching, displaying, and adding to the dictionaly
def menu():
    print(' ')
    print('MONTY PYTHON GAME CHOICE MENU')
    print(' ')
    print('1.  Skit guessing game')
    print('2.  Go on an adventure to find the Holy Grail')
    print('3.  Hangman')
    print('4.  Exit')
    print(' ')
    choice = input('What would you like to do?(Enter the number)  ')
    while len(choice) != 1:
        choice = input('Please make a valid selection:  ')
    if int(choice) == 1:
        skit_guess_instructions()
    elif int(choice) == 2:
        rpg()
    elif int(choice) == 3:
        hangmanInstructions()
    elif int(choice) == 4:
        print(' ')
        print('Thank you for playing these Monty Python games.  I hope you had fun!')
    else:
        print(' ')
        print('Please make a valid selection')
        print(' ')
        menu()


menu()
