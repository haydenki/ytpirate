import pafy
import urllib.request
import re
import time

## FUNCTIONS

def get_prefs():
	# Ask user how they will prefer their audio files
	preftype = input("Preferred file format? (Leave blank for any): ")
	ftypestrict = input("If there is an available file not in your preferred format, but has the highest bitrate, download that instead? [y/n]: ")
	filepath = input("File path to download to? (Leave blank for the directory this script is located in): ")
	if(ftypestrict.lower() == "y"):
		ftypestrict = True
	else:
		ftypestrict = False

	return preftype, ftypestrict, filepath

def download_song(audio):
	# Request a youtube search
	page_source = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + audio)

	# Extract video ID's from search results then combine to make final URL string
	video_id = re.findall(r"watch\?v=(\S{11})", page_source.read().decode())
	url = "https://www.youtube.com/watch?v=" + video_id[0]

	# Download video from URL
	audio_object = pafy.new(url, basic=False)
	print("Downloading " + video_object.title + "...")
	video_prefs = audio_object.getbestaudio(preftype=preftype, ftypestrict=ftypestrict)
	audio_prefs.download(filepath=filepath)
	time.sleep(6)

## MENU

print("-= YTpirate =-")
file_name = input("Enter the filename of your songlist: ")

songlist_file = open(file_name, "r")
songlist_lines = songlist_file.readlines()

songlist = []
for entry in songlist_lines:
	songlist.append(entry)

preftype, ftypestrict, filepath = get_prefs()

# Download each song found in the songlist
for song in songlist:
	try:
		download_song(song.replace(" ","+"))
	except:
		print("Unknown error in downloading \"" + song + "\"!")
print("Finished!")		

