# High Quality YouTube Video Downloader with pytube and moviepy

import os
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Takes the link from the user
link = input("Enter the link: ")
video_name = input("Enter the video name: ")

#takes the location from the user
location = input("Enter the folder location: ")

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
highest_video.download(output_path=location, filename="video")
highest_audio.download(output_path=location, filename="audio")

clip1 = VideoFileClip(rf"{location}/video")

audio = AudioFileClip(rf"{location}/audio")

# Merges the video and audio
clip1.audio = CompositeAudioClip([audio])

clip1.write_videofile(rf"{location}/{video_name}.mp4")

# Removes the single files, ADD THE LOCATION
os.remove(rf"{location}/video")
os.remove(rf"{location}/audio")
