from playsound import playsound as ps
import os

def gen_song_list(path):
	songs = os.listdir(path)
	for song in songs:
		if song.endswith('.mp3'):
			print(song)
			ps(song)

def searchMusic():

	ch = int(input("Enter Choice :\n1.Manually add Music Path\n2.Play Music in Current Path\nch = "))
	if ch==1:
		path = str(input("Enter Music Path = "))
		os.chdir(path)
		gen_song_list(path)
	elif ch==2:
		path=os.getcwd()
		gen_song_list(path)
	# music_name = str(input("Enter Music Name ( with extension eg .mp3, .mp4 ) = "))
	
	


searchMusic()
