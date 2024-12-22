import yt_dlp
from moviepy import VideoFileClip, AudioFileClip
import os

def download_video(video_url, output_path="E:\\DOWNLOADED CMD VIDEOS", output_filename="final_video.mp4"):
    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    video_path = os.path.join(output_path, "video.mp4")
    audio_path = os.path.join(output_path, "audio.mp3")
    final_path = os.path.join(output_path, output_filename)  # Use the specified filename for final video
    
    # yt-dlp options for downloading video and audio separately
    video_opts = {
        'format': 'bestvideo[height<=1080]',  # Best video (1080p or lower)
        'outtmpl': video_path,
    }
    audio_opts = {
        'format': 'bestaudio/best',  # Best audio
        'outtmpl': audio_path,
    }
    
    try:
        # Download video
        print("Downloading video...")
        with yt_dlp.YoutubeDL(video_opts) as ydl:
            ydl.download([video_url])
        
        # Download audio
        print("Downloading audio...")
        with yt_dlp.YoutubeDL(audio_opts) as ydl:
            ydl.download([video_url])
        
        # Merge video and audio using moviepy
        print("Merging video and audio...")
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        final_clip = video_clip.with_audio(audio_clip)  # Updated method for setting audio
        
        # Write the final video file with the user-defined filename
        final_clip.write_videofile(final_path, codec="libx264", audio_codec="aac")
        
        print(f"Video successfully downloaded and merged at: {final_path}")
        
        # Clean up intermediate files
        os.remove(video_path)
        os.remove(audio_path)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    output_folder = input("Enter the folder to save the video (default: 'E:\\DOWNLOADED CMD VIDEOS'): ").strip()
    output_folder = output_folder if output_folder else "E:\\DOWNLOADED CMD VIDEOS"
    
    output_filename = input("Enter the desired output video filename (default: 'final_video.mp4'): ").strip()
    output_filename = output_filename if output_filename else "final_video.mp4"
    
    download_video(video_url, output_folder, output_filename)
