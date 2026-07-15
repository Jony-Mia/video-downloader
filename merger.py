from moviepy import VideoFileClip, AudioFileClip

video = VideoFileClip("Love Me Like You Do - Ellie Goulding (Lyrics)  Ed Sheeran, Powfu (Mix Lyrics).mp4")
audio = AudioFileClip("Love Me Like You Do - Ellie Goulding (Lyrics)  Ed Sheeran, Powfu (Mix Lyrics).m4a")

final = video.with_audio(audio)
final.write_videofile("output.mp4")