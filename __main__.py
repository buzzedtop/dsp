import os
import subprocess

def convert_mp3_to_opus(mp3_file):
    """Converts an MP3 file to Opus format."""
    output_file = mp3_file.split(".")[0]
    command = "ffmpeg -i " + mp3_file + " -c:a libopus -b:a 32k -vbr on -compression_level 10 -frame_duration 60 -application voip " + output_file + ".opus"
    print(command)
    subprocess.run(command, shell=True)

def convert_mp3_to_ogg(mp3_file):
    """Converts an MP3 file to ogg format."""
    output_file = mp3_file.split(".")[0]
    command = "ffmpeg -i " + mp3_file + " -c:a libvorbis -q:a 4 " + output_file + ".ogg"
    print(command)
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    path = input("Enter the path to the folder: ")
    files = os.listdir(path)

    for mp3_file in files:
        if mp3_file.split(".")[-1] == "mp3":
            print(mp3_file)
            if mp3_file.split(".")[0] + ".opus" not in files:
                convert_mp3_to_opus(mp3_file)
            if mp3_file.split(".")[0] + ".ogg" not in files:
                convert_mp3_to_ogg(mp3_file)