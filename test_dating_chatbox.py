from dating_chatbox import is_affirmative, end_shopping, ask_name, choose_match, resources

def test_is_affirmative(do_rant = 'Yes'):
    assert callable(is_affirmative)
    assert isinstance(is_affirmative(do_rant), bool)
    assert is_affirmative(do_rant = do_rant) == True
    
def test_end_shopping(msg = 'I\'m done'):
    assert callable(end_shopping)
    assert isinstance(end_shopping(msg), bool)
    assert end_shopping(msg = msg) == True

def test_ask_name(monkeypatch):
    # Used https://stackoverflow.com/questions/35851323/how-to-test-a-function-with
    #-input-call directly
    assert callable(ask_name)
    monkeypatch.setattr('builtins.input', lambda _: 'Jessie')
    name = input('What is your name? :\t')
    assert name == 'Jessie'
    
def test_choose_match(monkeypatch):
    # Used https://stackoverflow.com/questions/35851323/how-to-test-a-function-with
    #-input-call directly
    assert callable(choose_match)
    monkeypatch.setattr('builtins.input', lambda _: 'James')
    match = input('Enter the name of any person you want to talk to :\t')
    assert match == 'James'

def test_resources(red_flag_counter = 0, match = 'James'):
    assert callable(resources)
    assert isinstance(resources(red_flag_counter, match), str)
    assert resources(red_flag_counter = 0, match = match) == ('Good job, ' + 
                                                              'you left before the toxic human could get to you! I\'d still recommend ' + 
                                                              'checking out this resource with tips on identifying red flags:  https://' + 
                                                              'www.cosmopolitan.com/uk/love-sex/relationships/a33364278/red-flags-' + 
                                                              'relationship/')
    assert resources(red_flag_counter = 4, match = 'James') == ('Please reconsider talking to James. This person exhibits far too many' + 
                                                                ' red flags. This resource contains tips on identifying red flags: ' + 
                                                                'https://www.cosmopolitan.com/uk/love-sex/relationships/a33364278/red' + 
                                                                '-flags-relationship/')
    
    
