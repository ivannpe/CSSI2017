class Musician:
    def __init__(self, name, instrument, song):
        self.name = name
        self.instrument = instrument
        self.song = song
        self.recording = recording
    def description(self):
        return "The artist you have chosen is {0}, they play the {1}, and a popular song is {2}".format(self.name,self.instrument,self.song)
    def is_recording(self):
        if self.recording:
            return "Yessir"
        else:
            return "On tour"
kanye = Musician('kanye', 'vocals', 'famous', False)
chance = Musician('Chance', 'rapper', 'no problem', True)

print chance.is_recording()
print kanye.is_recording()
