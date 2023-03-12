from pytube import YouTube
import os

# get the YouTube video URL from user input
url = input('URL: ')

# create a YouTube object and get the audio stream
yt = YouTube(url)
audio_stream = yt.streams.filter(only_audio=True).last()

# loop until a valid output path choice is entered
while True:
    try:
        # ask user for the output path choice
        choice = int(input("standard path (1) custom path (2): "))
        if choice == 1:
            output_path = '' # enter here your standard paths
        elif choice == 2:
            destination = input('DESTINATION PATH: ')
            output_path = destination.replace("\\", "/").replace("C:", "")
        else:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

# download the audio stream to the chosen output path
output_file = audio_stream.download(output_path=output_path)

# rename the downloaded audio file to a .mp3 file
base, ext = os.path.splitext(output_file)
new_file = base + '.mp3'
os.rename(output_file, new_file)

print(yt.title + " has been successfully downloaded.")