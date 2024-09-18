import os
import subprocess

# Set the directory containing the videos and output directory
input_dir = "videos-new"
output_dir = "videos-new-output"

# Make sure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define the target resolution for TikTok (16:9 portrait)
output_width = 1080
output_height = 1920

# Loop through each file in the directory
for file_name in os.listdir(input_dir):
    # Check if the file is a video (you can add more video formats if needed)
    if file_name.endswith(('.mp4', '.mov', '.avi', '.mkv')):
        # Define the input and output file paths
        input_file = os.path.join(input_dir, file_name)
        output_file = os.path.join(output_dir, f"resized_{file_name}")

        # FFmpeg command to resize video, keeping aspect ratio and cropping to cover
        ffmpeg_command = [
            'ffmpeg', '-i', input_file, '-vf',
            f'scale={output_width}:{output_height}:force_original_aspect_ratio=increase,crop={output_width}:{output_height}',
            '-c:a', 'copy', output_file
        ]

        # Execute the FFmpeg command
        subprocess.run(ffmpeg_command, check=True)
        print(f"Processed {file_name} and saved to {output_file}")
