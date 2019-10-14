from gtts import gTTS
# from tempfile import TemporaryFile
from mido import MidiFile, MidiTrack, Message
import os
import time
import glob
import random
import winsound
import pygame
import win32com.client


tts = gTTS(text='Momma? Do you want your momma?', lang='en-uk');
# f = TemporaryFile();
# tts.write_to_fp(f);
# # Play f
# os.system(tts);
# f.close();

tts.save("momma.mp3");


def weightedRandomSelect( L, W ):

	if len(L) != len(W) :
		raise "LISTS NOT SAME LENGTH" 

	wtotal = 0;
	for x in W:
		wtotal += x;

	si = random.random()*wtotal;#( 0, wtotal );
	if si >= wtotal:
		si = 0;

	R = L[0];
	sli = 0;
	st = 0;
	while st < si:
		st += W[sli];
		R = L[ sli ];
		sli += 1;
	return R;


def randomWord():
	t = "abcdefghijklmnopqrstuvwxyz";
	#w = "92349334932434931453821111"
	w = [9,2,3,4,9,3,3,4,9,3,2,4,3,4,9,3,1,4,5,3,8,2,1,1,1,1];
	
	n = 1 + random.randint( 0,13 );

	s = "";
	while n > 0:
		s += weightedRandomSelect( t, w )
		n -= 1;
	return s;

def randomSentence():
	articles= ["the","a","an","and","but","who","sometimes","1986","Jason", "Cody"]
	weights= [3,2,2,2,2,1,1,0.1,1,1];
	s = [];
	n = random.randint( 5, 23 );
	while n > 0:
		if random.randint( 0,3 ) < 1 :
			s.append( weightedRandomSelect( articles, weights ) );
			#s.append( random.choice( articles ) );
		else:
			s.append( randomWord() );
		n -= 1;
	return s;

def generatePitchXMLS():
	return "<pitch middle = '"+str( random.randint(-10,10) )+"'/>"

def speakBroken( speaker, sl ):

	"""
	pit = -10;
	s = "";
	for k in sl:
		#s += " " + generatePitchXMLS() + k
		s += "<pitch middle = '"+str( pit )+"'/>" + " " + k
		pit += 1;
		#s = generatePitchXMLS() + " "+ k
	speaker.Speak( s, 1 );
	"""

	speaker.Speak( " ".join(sl), 1 );
	while True:
		newrate = random.randint( 1, 18 ) - 9;
		speaker.Rate = newrate;	#Must be -10 ... 10 
		speaker.Volume = 100; #0..100
		# print( str( newrate ) );
		isdone = speaker.WaitUntilDone( 250 );
		if isdone:
			break;
"""

	for v in sl :
		speaker.Rate = random.randint( 0, 20 ) - 10;
		speaker.Speak( v, 1 );
"""
# print( randomWord() )

def getRandomOSSound():
	pickAsound = random.choice(glob.glob(os.path.expanduser('~')+"\\..\\..\\Windows\\Media\\*.wav"));
	# pickAsong = random.choice(glob.glob(os.path.expanduser('~')+"\\..\\..\\Windows\\Media\\*.mid"));
	return pickAsound;
	
def getOSMIDI():
	pickAsong = random.choice(glob.glob(os.path.expanduser('~')+"\\..\\..\\Windows\\Media\\*.mid"));
	return pickAsong;

def playRandomOSsound():
	soundfile = getRandomOSSound();
	winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC);

def playMIDIshit(midiSong):
	# midiSong = getOSMIDI();
	pygame.init();
	pygame.mixer.music.load(midiSong);
	pygame.mixer.music.play();

def playMP3(mp3file):
	pygame.init();
	pygame.mixer.music.load(mp3file);
	pygame.mixer.music.play();
	while pygame.mixer.music.get_busy(): 
		continue;

def generateMIDI():
	mid = MidiFile(type=0);

	track = MidiTrack();

	mid.tracks.append(track);

	notes = range(20, 120);#range(40, 90);

	for i in range(0, 20):
	    note = random.choice(notes);
	    track.append(Message('note_on', note=note, velocity=random.randint(50,127), time=i*100));
	    track.append(Message('note_off', note=note, velocity=random.randint(50,127), time=(i+random.randint(1,5))*100));

	mid.save('random.mid');


#_____________________________________________________
speaker = win32com.client.Dispatch("SAPI.SpVoice");



while True:
	# generateMIDI();
	# playMIDIshit('random.mid');
	# playRandomOSsound();
	os.system("momma.mp3");
	# speaker.Speak('Momma? Do you want your momma?');
	time.sleep(3);
	# rs = randomSentence();
	# print( rs );
	# speakBroken( speaker, rs  );
	# # print( "finished" );
	# playRandomOSsound();
	# playMIDIshit(getOSMIDI());

"""
while True:
	newrate = random.randint( 1, 18 ) - 9;
	speaker.Rate = newrate;
	print( str( newrate ) );
	isdone = speaker.WaitUntilDone( 500 );
	if isdone:
		break;
print( "finished" );
"""

#speaker.Speak( " ".join( rs ) , 1 );
#speaker.Speak( " ".join( randomSentence() ) , 1 );
#speaker.Speak( " ".join( randomSentence() ) , 1 );

#speaker.Speak( " " );	#//Wait until speech is finished (hack)

# myWord = " ".join(  randomSentence() );
# print(myWord);
# speaker.Speak(myWord);

#fout = open( '_wavemesast34.wav', 'wb')
#speaker.SpeakStream( fout );#" ".join(rs) );
#fout.close();