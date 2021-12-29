import argparse
from ffmpeg_editor import call_ffmpeg_with_args
from moviepy_editor import moviepy_gif, moviepy_mp4


def get_argparse():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input")
    arg_parser.add_argument("output")
    arg_parser.add_argument("--fromTime", required=False)
    arg_parser.add_argument("--toTime", required=False)
    arg_parser.add_argument("--slowMo")
    arg_parser.add_argument("--resize")
    return arg_parser.parse_args()


def extract_time(time_array):
    if len(time_array) == 2:
        return float(time_array[0]) * 60 + float(time_array[1])
    elif len(time_array) == 3:
        return float(time_array[2]) * 3600 + float(time_array[1]) * 60 + float(time_array[2])


def parse_input_args(input_args):
    from_time_cmd = input_args.fromTime
    to_time_cmd = input_args.toTime

    resize_cmd = input_args.resize
    slow_mo_cmd = input_args.slowMo
    resize = float(resize_cmd.replace(",", ".")) if resize_cmd is not None else None
    slow_mo = float(slow_mo_cmd.replace(",", ".")) if slow_mo_cmd is not None else None

    clip_from_time = None
    clip_to_time = None

    if from_time_cmd is not None:
        if ":" in from_time_cmd:
            time_array = from_time_cmd.split(":")
            clip_from_time = extract_time(time_array)
        else:
            clip_from_time = float(from_time_cmd.replace(",", "."))

    if to_time_cmd is not None:
        if ":" in to_time_cmd:
            time_array = to_time_cmd.split(":")
            clip_to_time = extract_time(time_array)
        else:
            clip_to_time = float(to_time_cmd.replace(",", "."))

    print(f"From time: {clip_from_time if clip_from_time is not None else 'From the start'}, "
          f"to time: {clip_to_time if clip_to_time is not None else 'To the end'}. "
          f"Slow down: {slow_mo if slow_mo is not None else 'None'} "
          f"Resize: {resize if resize is not None else 'default size'} "
          )
    return input_args.input, input_args.output, clip_from_time, clip_to_time, resize, slow_mo


if __name__ == "__main__":
    input_args = get_argparse()
    input_file, output_file, from_time, to_time, resize, slow_mo = parse_input_args(input_args)
    if ".gif" in output_file:
        moviepy_gif(input_file, output_file, from_time, to_time, resize, slow_mo)
    else:
        moviepy_mp4(input_file, output_file, from_time, to_time, resize, slow_mo)
