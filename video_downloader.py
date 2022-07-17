# High Quality Youtube Video Downloader with pytube and moviepy

from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from sys import argv
import os

# Takes the link from the user
link = input("Please, enter link: ")

yt = YouTube(link)

name = yt.title

# Prints the title of the video
print("Title: ", yt.title)

# Prints the amount of view of the video
print("View: ", yt.views)

stream = yt.streams.filter(adaptive=True)

# Takes the highest quality version of the video
highest_video = stream[0]

# Takes the highest quality version of the audio
highest_audio = stream[-1]

# Downloads the video and audio, ADD THE LOCATION
highest_video.download(output_path='Location of the video', filename="video")
highest_audio.download(output_path='Location of the audio', filename="audio" )

clip1 = VideoFileClip("video")

audio = AudioFileClip("audio")

# Merges the video and audio
clip1.audio = CompositeAudioClip([audio])

clip1.write_videofile(f"{name}.mp4")

# Removes the single files, ADD THE LOCATION
for file in os.listdir('Location of the video and audio'):
    os.remove("video")
    os.remove("audio")
