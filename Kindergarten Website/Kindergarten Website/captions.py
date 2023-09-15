import os

# Define a directory for saving generated captions
CAPTIONS_OUTPUT_DIR = 'static/captions/'

def generate_captions(translated_transcript, selected_language):
    try:
        # Create a directory for the language if it doesn't exist
        lang_output_dir = os.path.join(CAPTIONS_OUTPUT_DIR, selected_language)
        os.makedirs(lang_output_dir, exist_ok=True)

        # Set the output captions file path
        captions_filename = f'{selected_language}_captions.srt'
        captions_path = os.path.join(lang_output_dir, captions_filename)

        if not os.path.isfile(captions_path):
            # Logic for generating captions (optional)
            # Example: Create an SRT file with subtitles
            captions_text = '1\n00:00:00,000 --> 00:00:10,000\n' + translated_transcript
            with open(captions_path, 'w', encoding='utf-8') as captions_file:
                captions_file.write(captions_text)

        return captions_path

    except Exception as e:
        return str(e)
