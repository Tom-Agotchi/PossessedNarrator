import random;
import time;
import pygame;
from mido import MidiFile, MidiTrack, Message
import sys;

# program_change
def generateMIDI():
	mid = MidiFile(type=0);

	track = MidiTrack();2

	mid.tracks.append(track);

	notes = range(10, 70);#range(40, 90);#range(20, 120);

	#channel 10 reserved for percussion
	
	#change 'instrument' with program_change 0-127
	for i in range(0, 200):
		for i in range(0,15):
			# note = random.choice(notes);
			t=random.randint(0,15);
			track.append(Message('program_change', channel=i, program=random.randint(0,127)));
			track.append(Message('note_on', channel=i, note=random.choice(notes), time=t));#i*100));, velocity=random.randint(50,127)
			track.append(Message('note_off', channel=i, note=random.choice(notes), time=(t+random.randint(1,10))*1));#, velocity=random.randint(50,127)

	mid.save('shit.mid');

def playMIDI(midiSong):
	# midiSong = getOSMIDI();
	pygame.init();
	pygame.mixer.music.load(midiSong);
	pygame.mixer.music.play();
	# print('got here')


#___________________________________________
print("Annnnd a 1, and a 2...");
while True:
	generateMIDI();
	playMIDI('shit.mid');
	time.sleep(60)