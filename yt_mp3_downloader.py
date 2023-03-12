from pytube import YouTube
import os

yt = YouTube(input('URL: '))
video = yt.streams.filter(only_audio=True).last()

destination = input('DESTINATION PATH: ')
output = destination.replace("\\", "/")
output = destination.replace("C:", "")

out_file = video.download(output_path=output)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded.")