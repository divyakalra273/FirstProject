"""
    1.Think of an object
    Song:Title,Artist,Duration

"""
#2.Write its Class

class Song:
    def __init__(self, title, artist, duration):
        self.title=title
        self.artist=artist
        self.duration=duration
        self.nextSong=None
        self.previousSong=None


    def showSongDetails(self):
        print("{}\t{}\t{}\t".format(self.title,self.artist,self.duration))

#3.From class create the Real Object in memory

song1 = Song ("Muqabla" , "Yash" , 3.45)
song2 = Song("Ek Toh","Neha Kakkar",4.50)
song3 = Song("Garmi","Badshah",3.45)
song4 = Song("Gulabi","Ammal",3.45)

print("Song 1 is:",song1)
print("Song 2 is:",song2)
print("Song 3 is:",song3)
print("Song 4 is:",song4)

#Refernce Copy Operation
song1.nextSong = song2
song2.nextSong = song3
song3.nextSong = song4
song4.nextSong = song1

song1.previousSong = song4
song2.previousSong = song1
song3.previousSong = song2
song4.previousSong = song3

temp = song1

while temp.nextSong != song1:
    print("----------------")
    temp.showSongDetails()
    print("----------------")
    temp = temp.nextSong

temp1 = song4
while temp1.previousSong != song4:
    print("--------------")
    temp1.showSongDetails()
    print("----------------")
    temp1 = temp1.previousSong

temp1.showSongDetails()
print("---------------")


