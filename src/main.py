import sys
from ffmpeg_editor import call_ffmpeg_with_args
from input_parse import get_parsed_inputs
from moviepy_editor import moviepy_gif, moviepy_mp4


if __name__ == "__main__":
    input_file, output_file, from_time, to_time, speed, resize = get_parsed_inputs(sys.argv[1:])
    if ".gif" in output_file:
        moviepy_gif(input_file, output_file, from_time, to_time, speed, resize)
    else:
        moviepy_mp4(input_file, output_file, from_time, to_time, speed, resize)
