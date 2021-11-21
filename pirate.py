import pafy
import urllib.request
import re
import time

def get_prefs():
	# Ask user how they will prefer their audio files
	preftype = input("Preferred file format? (Leave blank for any): ")
	ftypestrict = input("If there is an available file not in your preferred format, but has the highest bitrate, download that instead? [y/n]: ")

	if(ftypestrict.lower() == "y"):
		ftypestrict = True
	else:
		ftypestrict = False

def download_song(audio):
	# Request a youtube search
	page_source = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + audio)

	# Extract video ID's from search results then combine to make final URL string
	video_id = re.findall(r"watch\?v=(\S{11})", page_source.read().decode())
	url = "https://www.youtube.com/watch?v=" + video_id[0]

	# Download video from URL
	video_object = pafy.new(url, basic=False)
	print("Downloading " + video_object.title + "...")
	video_prefs = video_object.getbestaudio(preftype=preftype, ftypestrict=ftypestrict)
	video_prefs.download()
	time.sleep(6)

print("-= Music Pirater 3000 =-")
print("[1] - Download from local songlist")
print("[2] - Download from Youtube playlist")
choice = int(input("enter:"))

if(choice == 1):
	file_name = input("Enter the filename of your songlist:")
	songlist_file = open(file_name, "r")
	songlist_lines = songlist_file.readlines()

	songlist = []
	for entry in songlist_lines:
		songlist.append(entry)

	# Ask user how they will prefer their audio files
	preftype = input("Preferred file format? (Leave blank for any): ")
	ftypestrict = input("If there is an available file not in your preferred format, but has the highest bitrate, download that instead? [y/n]: ")

	if(ftypestrict.lower() == "y"):
		ftypestrict = True
	else:
		ftypestrict = False

	# Download each song found in the songlist
	for song in songlist:
		download_song(song.replace(" ","+"))

	print("success")		
elif(choice == 2):
	search_term = input("Enter playlist or video URL: ")
	search_term = search_term.replace(" ", "+")

	# Ask user how they will prefer their audio files
	preftype = input("Preferred file format? (Leave blank for any): ")
	ftypestrict = input("If there is an available file not in your preferred format, but has the highest bitrate, download that instead? [y/n]: ")

	if(ftypestrict.lower() == "y"):
		ftypestrict = True
	else:
		ftypestrict = False

	download_song(search_term)

