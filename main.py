from pytubefix import YouTube
from moviepy import VideoFileClip, AudioFileClip

url = "https://www.youtube.com/watch?v=rvAtfKiEzXU"

def on_progress(stream,chunk, bytes_remaining):
    total_size = stream.filesize
    downloaded = total_size - bytes_remaining
    progress= (downloaded/ total_size) * 100

    print(f"\rDownloading: {progress:.2f}%", end="")

def on_complete(stream,file_path):
    
    print("Download Completed")
    print(f"file saved {file_path}")

youTube = YouTube(url
                  ,use_oauth=False,
                  on_progress_callback=on_progress,
                  on_complete_callback=on_complete
                  )

highest_video = youTube.streams.get_highest_resolution(progressive=False)
highest_audio = youTube.streams.get_audio_only()
print(highest_video.filesize/pow(1024,2))

highest_audio.download()
highest_video.download()

video = VideoFileClip(highest_audio.title+".mp4")
audio = AudioFileClip(highest_audio.title+".m4a")

final_video = video.with_audio(audio)
final_video.write_videofile(f"{highest_video.title}.mp4")