from django.shortcuts import render
from pytube import YouTube
from django.contrib import messages
from pytube.exceptions import PytubeError, VideoUnavailable

def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        if not link:
            messages.error(request, "Please provide a YouTube link.")
            return render(request, 'youtube.html')
        
        try:
            video = YouTube(link)
            stream = video.streams.get_lowest_resolution()
            stream.download()
            messages.success(request, "Video downloaded successfully!")
        except VideoUnavailable:
            messages.error(request, "The video is unavailable or restricted.")
        except PytubeError as e:
            messages.error(request, f"An error occurred: {str(e)}")
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
    
    return render(request, 'youtube.html')
