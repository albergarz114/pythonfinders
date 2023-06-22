import datetime                         # Imported datetime to make presentable
from random import choice              # imported random choice function

Today_Date = datetime.datetime.now()             # .now() to get the present/current date

year = Today_Date.strftime("%Y")        ##strftime:datetime object####
month = Today_Date.strftime("%m")
day = Today_Date.strftime("%d")
Formatted_Date = day + "/" + month + "/" + year 

def show_menu():                        #def
    print("\n   Menu:")                 #displays menu and all options on Terminal
    print("1. Logical Jokes")
    print("2. Random Jokes")
    print("0. Exit")


def love():
    # List of logical jokes
    logical_jokes = [                               
        "This sentence contains exactly three errors.\n\t> The first two errors? The extra E in 'three' and the missing R in 'error'. The third error? The fact that there are only two errors.",
        "How do mathematicians scold their children?\n\t> If I've told you n times, I've told you n+1 times... Math equations use letters in place of unsolved numbers.",
        "A mathematician wanders back home at 3 a.m. and proceeds to get an earful from his wife.\n\t> 'You are late!' she yells. 'You said you'd be home by 11:45!' Actually, the mathematician replies coolly, I said I'd be home by a quarter of 12. Divide 12 by four or a quarter, which is three!",
        "Did you hear about the mathematician who's afraid of negative numbers?\n\t> He will stop at nothing to avoid them. Explanation: Once he hits zero in the countdown, it's all negative numbers from there.",
        "Why did Beethoven get rid of his chickens?\n\t> All they said was Bach, Bach, Bach.",
        "C, E-flat, and G walk into a bar.\n\t> The bartender shows them the door and says, 'Sorry, we don't serve minors.'",
        "A sign at a music shop:\n\t> Gone chopin. Bach in a minuet.",
        "What was Beethoven's favorite fruit?\n\t> Ba-na-na-naaaaaaa!",                         ####REMEMBER!!!! LISTS ARE WITH BRACKETS###
        "DNA say to the other DNA?\n\t> Do these genes make me look fat?",
        "A German walks into a bar and asks for a martini. The bartender asks, 'Dry?'\n\t> The German replies, 'Nein, just one.'",
        "I finally decided to sell my vacuum cleaner.\n\t> All it was doing was gathering dust.",
        "If you jumped off the bridge in Paris,\n\t> You would be in Seine.",
        "God, how long is a million years?\n\t> To me, it's about a minute.\n\t> God, how much is a million dollars?\n\t> To me, it's a penny.\n\t> God, may I have a penny?\n\t> Wait a minute.",
        "How can you make time fly?\n\t> Throw a clock out a window.",
        "What is the best way to get a math tutor?\n\t> An add."
    ]

    # Displayed LIST
    print(Formatted_Date)  #current date##
    print("Welcome to Jokes! Press 'n' to generate a logical joke, 'q' to exit, or 'a' to add a joke.")
    while True:
        user_Input = input("N/Q for Exit/A: ").lower() # OPTIONS AND IMPLEMENTED LOWER CASES
        if user_Input == "n":
            print(choice(logical_jokes))
        if user_Input == "q":
            break
        if user_Input == "a":
            user_Joke = input("Please Enter Your Joke:")  # Implementing and entering a joke if 'a'
            logical_jokes.append(user_Joke)      
            print("Updated List: ", logical_jokes)
    print("Thank you for using Jokes!") # Decided to implement to make it presentable

def random_joke():  #def key word you can create a function and give it a name. Without it is NOT A FUNCTION##
    # Dictionary of random jokes
    random_jokes = {
        'Why did the student wear glasses in math class?':'\n\t> To improve di-vision',         #left is KEY and right is VALUE###
        'Why did the obtuse angle jump in the pool?':'\n\t> Because it was over 90 degrees',
        'Why does algebra improve your dancing skills?':'\n\t> Because you can use algo-rhythm.',
        'What is a math teachers favorite place in NYC?':'\n\t> Times Square',
        'Do you know what seems odd to me?':'\n\t> Numbers that are not divisible by two',
        'Where should you do your math homework?':'\n\t> On a multiplication table',
        'Why do teens always travel in groups of three or five?':'\n\t> Because they can not even',                     ###DICTIONARIES ARE THE BOMB####
        'Why did seven eat nine?':'\n\t> Because you are supposed to eat three squared meals every day',                ####REMEMBER ALWAYS WITH CURLY BRACES###
        'Are monsters good at math?':'\n\t> Not unless you Count Dracula',
        'Did you know that there are three kinds of people in the world?':'\n\t> People who can count and people who can\'t',
        'What did the calculator say to the student?':'\n\t> You can always count on me',
        'What do you call a group of dudes who love math?':'\n\t> Alge-bros',
        'Do you know who invented algebra?':'\n\t> An x-pert',
        'Why was math class so long?':'\n\t> The teacher kept going off on a tangent',
        'Why did the two fours skip lunch?':'\n\t> They already eight',
        'Why do mathematicians like parks?':'\n\t> Because of all the natural logs',
        'Why don\'t math majors throw house parties?':'\n\t> Because it\'s dangerous to drink and derive'   ##left is KEY and right is VALUE###
    }

    # Displayed DICTIONARIES 
    print(Formatted_Date) #current date##
    print("Welcome to Jokes! Press 'n' to generate a random joke, 'q' to exit, or 'a' to add a joke.")
    while True:
        user_Input = input("N/Q for Exit/A: ").lower() #lower cases is easier for humans##
        if user_Input == "n":
            #created a function 'CHOSEN_JOKE'####
            chosen_joke = choice(list(random_jokes.keys()))  #method to retrieve the dictionary keys for example '.key' {key:new value}#
            print(chosen_joke)                               # key method gives the input from the left side of the colon(:)#  
            print(random_jokes[chosen_joke])                 # for example on line #56:'Why did the student wear glasses in math class?'#
                                                             # another example on line #71:'Why do mathematicians like parks?##
        if user_Input == "q":
            break
        if user_Input == "a":
            user_Joke = input("Please Enter Your Joke:")
            user_Answer = input("Why? ")
            random_jokes.update({user_Joke: user_Answer})     ##Remember:{Key is LEFT:VALUE IS RIGHT}
            print("Updated Dictionary: ", random_jokes)
    print("Thank you for using Jokes!")


while True:             #WHILE LOOP##
    show_menu()             
    user_choice = input("Enter your choice: ")

    if user_choice == "1":   #OPTION 1#
        love()
    
    elif user_choice == "2":        #OPTION2#
        random_joke()
    
    elif user_choice == "0":
        print("Exiting...")         #option0##
        break
    else:
        print("Invalid choice. Please try again.")  




