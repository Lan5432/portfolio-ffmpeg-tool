from input_parse import get_parsed_inputs
from ffmpeg_editor import video_and_audio, audio

if __name__ == "__main__":
    input_file, output_file, from_time, to_time, speed, resize = get_parsed_inputs()
    if '.mp4' in output_file:
        video_and_audio(input_file, output_file, from_time, to_time, speed, resize)
    if '.mp3' in output_file:
        audio(input_file, output_file, from_time, to_time)
