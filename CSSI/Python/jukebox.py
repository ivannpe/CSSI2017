songs = ["uptown funk", "thinking out loud" , "blank space" , "take me to church" , "shake it off", "wake me up"]

def list_songs():
    for song in songs:
        print song

def play_songs():
    list_songs()
    song_name = int(raw_input('Pick Song Number:  '))
    print songs[song_name]

def search_songs():
    search = raw_input('Search:  ')
    for song in songs:
        if search in song:
            print song

def quit_songs():
    print 'Goodbye'

def Options():
    option = ''
    while option != 'quit':
        option = raw_input('Pick Menu Item: List, Play, Search, Quit  ')
        option = option.lower()
        if option == 'list':
            list_songs()
        if option == 'play':
            play_songs()
        if option == 'search':
            search_songs()
        if option == 'quit':
            quit_songs()
Options()
