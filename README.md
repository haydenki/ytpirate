# YTpirate

YTpirate is a program designed to make it easier to listen to free music. It takes a text file as input, containing a list of songs and automatically finds them on YouTube and downloads them to a directory of your choice. It also can prioritize downloads by bitrate/filetype preferences of the users choosing.


## Requirements


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the "pafy" library.

```bash
pip install pafy
```
That's all!

## Usage
Create a text file of any name, containing your song names, YouTube video URLs, or ~~YouTube playlist URLs~~ (option for downloading playlists has been temporarily deprecated due to it not working), separated by newlines.

Example:
```
Rick Astley - Never Gonna Give you up
https://www.youtube.com/watch?v=yOzEeJZ92X8&list=PL4_Ig7Xjs6hxhMJi1hyKFY5YYMd9IvkHN
the gummy bear song


```
After the file is created, simply run the .py script and input your download options as prompted, and they will start downloading!

## To-do:
1. Add support for downloading playlists

## License
[GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
