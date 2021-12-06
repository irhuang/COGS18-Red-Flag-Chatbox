import string
import random
import nltk

# Different output responses from dating interest, which will be randomized later
choice_list1 = ['We\'re not close enough for me to tell you my deep feelings', 
                       'Would you like to rant? If so, say \"I\'m angry\"',
                       'Good, how are you?',
                       'Do you want to go grocery shopping? If so, say "GET FOOD"']
# Output responses if user asks a question
choice_list2 = ['Fine.', 'Mhm', 'Huh?', 'Whatever', '\'Sup bitch', 'Sheeeeeeeesh',  
                       'I just want you to be my rave babe 😩☝️', 
                       'I copped a fire jean jacket the other day, check me out! 😉💕',
                       'Wassup ma, wanna get some Korean bbq t\'night? 🥺',
                       '( ͡° ͜ʖ ͡°) Hey sexaaayy~']

def ask_name():
    '''Ask for and save user's name
    Outputs
    ------------    
    name: str
        Name of user
    '''
    
    # User types their username and are greeted
    name = input('What is your name? :\t')
    
    print('Welcome ' + name + '. You can leave the conversation with ' + 
         'with "BYE"')
    return name
    
def choose_match():
    '''Ask for and save name of who user is talking to
    Outputs
    ------------    
    match: str
        Name of match
    '''
    
    # User designates person to talk to
    match = input('Enter the name of any person you want to talk to :\t')
    
    return match
    
def pick_red_flag():
    '''Picks one of the red flag lines'''
    
    # A list of red flag messages in response to user getting food
    return random.choice(['You\'re gonna gain weight 🤮', 
                                     'Forget food, come home with me 😏',
                                     'I\'m too rich for my own good, don\'t' +  
                                     ' look at the price tag babygirl (▀̿Ĺ̯▀̿ ̿)',
                                     'Nah, let\'s grab boba',
                                     'Are you giving me the silent treatment? 🥺👉👈'])
    
def get_input(name, match, red_flag_counter):
    '''Ask user for an input message - first two lines are from Lec 20
    Inputs
    ------------    
    name: str
        Name of user
    match: str
        Name of match
    red_flag_counter: int
        How many red flags have accumulated
    
    Outputs
    ------------    
    msg: str
        Message user inputs
    out_msg: str
        Message that is returned
    red_flag_counter: int
        Updated red flags accumulated
    '''

    # Structures chatbox so messages the user says are clearly shown to be said 
    # by that user 
    msg = input(name + ' :')
    out_msg = None
    
    # One conversation path - shopping
    if msg == 'GET FOOD':
        counter = 0
        
        # A list to store the items the user buys
        food_list = []
        food = input('What do you get? When you\'re done inputting, ' +  
                     'say "I\'m done" :\t')
        
        # As long as the user is still shopping, the list grows and
        # red flag counters add for each red flag message that shows up
        while food != 'I\'m done' and red_flag_counter <= 3:
            food_list.append(food)
            food = input('')
            counter = counter + 1
            
            # Dating interest says a red flag after every 2 food inputs
            # after the first food input, which is added to total
            # red flag encounters
            if counter % 2 == 0:
                print(match + ': ' + pick_red_flag())
                red_flag_counter = red_flag_counter + 1
            
            # User ends shopping trip and gets a "receipt"
            if end_shopping(food):
                print('You bought: ' + str(food_list))
                break
    
    return msg, out_msg, red_flag_counter

def end_shopping(msg):
    '''Returns true if message is I'm done, otherwise False'''
    return msg == 'I\'m done'

def is_question(input_string):
    '''Determine if input from user is a question - from Lec 20'''
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output

def end_chat(msg):
    '''Identify if user says 'BYE' in input and end chat - from Lec 20'''
    
    if msg == 'BYE':
        output = 'bye'
        chat = False
    else:
        output = None
        chat = True
        
    return output, chat

def return_message(out_msg, question, red_flag_counter):
    '''Generic responses for the chatbot to return - from Lec 20'''
        
    # If we don't have an output yet, but the input was a question, 
    # return msg related to it being a question
    if not out_msg and question:
        rand = random.randint(0, len(choice_list1) - 1)
        out_msg = choice_list1[rand]

    # Catch-all to say something if msg not caught & processed so far
    if not out_msg:
        # Random output message is chosen from one of the items in 
        # the response list as defined at the very beginning of the 
        # file
        rand = random.randint(0, len(choice_list2) - 1)
        out_msg = choice_list2[rand]
        
        # Only certain output messages are red flags
        # Only those that are red flag messages count towards the 
        # red flag counter
        if rand >= 6:
            red_flag_counter = red_flag_counter + 1
            
    return out_msg, red_flag_counter

def rant(msg, name):
    '''Check if user wants to rant
    Inputs
    ------------    
    msg: str
        Message user inputs, from before
    name: str
        Name of user
    
    Outputs
    ------------  
    do_rant: str
        If user wants to rant or no
    '''

    if msg == 'I\'m angry':
        # User can choose to rant or not
        do_rant = input('So you want to rant? Yes or No \t')
    else:
        do_rant = None
    return do_rant

def is_affirmative(do_rant):
    '''Returns true if message is Yes or yes, otherwise False'''
    return do_rant == 'Yes' or do_rant == 'yes'
    
def go_rant(do_rant, name):
    '''Path where user can have consecutive spaces to say what they want to say
    Inputs
    ------------    
    do_rant: str
        If user wants to rant or no
    name: str
        Name of user
        
    Outputs
    ------------    
    rant_msg: str
        User input when ranting
    '''
    if is_affirmative(do_rant):
        # User can choose how many empty text lines they want, to rant
        lines = input('How many lines of rant do you have pent ' +
                      'up? You\'ll have as many boxes as you enter here \t' + 
                      '\nWhen you\'re done, type \"I\'m done\"')
        # User can type anything within the empty text spaces they specified 
        # without dating interest saying something right after each input
        for line in range(0, int(lines)):
            rant_msg = input(name + ' :' + '')
            if rant_msg == 'I\'m done':
                break
    else:
        rant_msg = None
    return rant_msg
        

def resources(red_flag_counter, match):
    '''End message and something to leave the users with
    Inputs
    ------------    
    red_flag_counter: int
        Red flags accumulated
    match: str
        Name of user

    Outputs
    ------------    
    end: str
        Final message to user, includes resources
    '''
    
    # If red flag encounters have surpassed limit, they are stopped
    if red_flag_counter > 3:
        end = ('Please reconsider talking to ' + match + '. This person ' + 
              'exhibits far too many red flags. This resource contains ' + 
              'tips on identifying red flags: https://www.cosmopolitan.' + 
              'com/uk/love-sex/relationships/a33364278/red-flags-relationship/')
    # If user ends conversation before the limit, they are commended
    else:
        end = ('Good job, you left before the toxic human could get to you!' + 
              ' I\'d still recommend checking out this resource with tips on' + 
              ' identifying red flags:  https://www.cosmopolitan.com/uk/' + 
              'love-sex/relationships/a33364278/red-flags-relationship/')
    return end
    
def have_a_chat():
    '''Main function to run our chatbot - from Lec 20'''
    
    name = ask_name()
    match = choose_match()
    chat = True
    red_flag_counter = 0
    
    while chat and red_flag_counter <= 3:
        
        # Pick possible red flag line - helper method for grocery shopping
        red_flag_msg = pick_red_flag()
        
        # Get input message from the user
        msg, out_msg, red_flag = get_input(name, match, red_flag_counter)
        red_flag_counter = red_flag
        
        # Check if the input is a question
        question = is_question(msg)
        
        # Check if user wants to rant
        do_rant = rant(msg, name)
        rant_msg = go_rant(do_rant, name)
        
        # Check for an end msg 
        out_msg, chat = end_chat(msg)
        
        # Specify what to return
        out_msg, red_flag = return_message(out_msg = out_msg, question = question, 
                                 red_flag_counter = red_flag_counter)
        red_flag_counter = red_flag
        
        print(match + ':', out_msg)
        
    # Message user gets when they end conversation or surpass the red flag limit
    print(resources(red_flag_counter, match))

  
    