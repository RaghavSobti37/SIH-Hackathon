from googletrans import Translator
import moviepy.editor as mp
import requests
from bs4 import BeautifulSoup

# Define a dictionary of subjects/chapters/videos and their associated keywords
topics_keywords = {
    "Math": ["mathematics", "algebra", "geometry"],
    "Science": ["science", "biology", "chemistry"],
    "History": ["history", "world history", "ancient civilizations"],
}

# Read the transcript from a text file
transcript_file_path = 'transcript.txt'
with open(transcript_file_path, 'r', encoding='utf-8') as file:
    transcript = file.read()

# Translate the transcript to another language (e.g., French)
translator = Translator()
translated_transcript = translator.translate(transcript, src='en', dest='fr').text

# Extract the relevant keywords based on the subject/chapter/video
subject = "Math"  # Replace with the appropriate subject/chapter/video
if subject in topics_keywords:
    keywords = topics_keywords[subject]
else:
    keywords = []  # Default to an empty list if subject is not found

# Function to search for images using keywords
def search_images(keyword):
    search_url = f"https://www.google.com/search?q={keyword}&tbm=isch"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_links = [img['src'] for img in soup.find_all('img')]
    return image_links

# Create a list of image links for each keyword
image_links_per_keyword = {}
for keyword in keywords:
    image_links = search_images(keyword)
    image_links_per_keyword[keyword] = image_links

# Create a dummy image for the video (using the first image link for each keyword)
image_clips = []
for keyword in keywords:
    if keyword in image_links_per_keyword:
        image_url = image_links_per_keyword[keyword][0]
        image_clip = mp.ImageClip(image_url)
        image_clip = image_clip.set_duration(10)  # Set the duration in seconds
        image_clip = image_clip.resize((1920, 1080))  # Set the dimensions of the image
        image_clips.append(image_clip)

# Create an audio clip with the translated transcript
audio_clip = mp.TextClip(translated_transcript, bg_color='white', fontsize=48)
audio_clip = audio_clip.set_duration(10)  # Set the duration in seconds

# Combine the images and audio to create the video
video_clip = mp.concatenate_videoclips(image_clips)
video_clip = video_clip.set_audio(audio_clip)

# Export the video
output_video_path = 'output_video.mp4'
video_clip.write_videofile(output_video_path, codec='libx264', fps=24)
