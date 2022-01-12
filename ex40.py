#mystuff = {'apple':"I AM APPLES"}
#print(mystuff['apple'])

class Song(object):
    #self refers to the instance we are about to create
    # This has to be used whenever a constructor (class) will be used
    def __init__(self,lyrics):
        self.lyrics = lyrics

    #behaviour defined on top of song
    # can only call this method on an instance of a song
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_b_day = Song(["Happy b day to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

#creates an instance of the song class
nmh = Song(["But for now we are young", 
            "So let us sing in the sun"])

# nmh is the instance, that is implicitidy passed 
# to sing me a song
nmh.sing_me_a_song()

happy_b_day.sing_me_a_song()