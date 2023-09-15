import os
import moviepy.editor as mp

# Define a directory for saving generated videos
VIDEO_OUTPUT_DIR = 'static/videos/'

def generate_video(translated_transcript, selected_language):
    try:
        # Create a directory for the language if it doesn't exist
        lang_output_dir = os.path.join(VIDEO_OUTPUT_DIR, selected_language)
        os.makedirs(lang_output_dir, exist_ok=True)

        # Set the output video file path
        video_filename = f'{selected_language}_video.mp4'
        video_path = os.path.join(lang_output_dir, video_filename)

        if not os.path.isfile(video_path):
            # Logic for generating the video using MoviePy
            # Example: Create a video with the translated text
            video_clip = mp.TextClip(translated_transcript, bg_color='white', fontsize=48)
            video_clip = video_clip.set_duration(10)  # Set the duration in seconds
            video_clip = video_clip.resize((1920, 1080))  # Set the dimensions of the video
            video_clip.write_videofile(video_path, codec='libx264', fps=24)

        return video_path

    except Exception as e:
        return str(e)
