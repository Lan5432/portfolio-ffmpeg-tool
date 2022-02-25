import argparse
from moviepy_editor import get_clip_duration


def extract_time(time_array):
    if len(time_array) == 2:
        return float(time_array[0]) * 60 + float(time_array[1])
    elif len(time_array) == 3:
        return float(time_array[2]) * 3600 + float(time_array[1]) * 60 + float(time_array[2])


def get_parsed_inputs(args):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input")
    arg_parser.add_argument("output")
    arg_parser.add_argument("--fromTime", required=False)
    arg_parser.add_argument("--toTime", required=False)
    arg_parser.add_argument("--speed")
    arg_parser.add_argument("--resize")
    return _parse_inputs(
        arg_parser.parse_args(args)
    )


def _parse_inputs(input_args):
    input_file_cmd = input_args.input
    output_file_cmd = input_args.output
    from_time_cmd = input_args.fromTime
    to_time_cmd = input_args.toTime
    speed_cmd = input_args.speed
    resize_cmd = input_args.resize

    speed = float(speed_cmd.replace(",", ".")) if speed_cmd is not None else None
    resize = float(resize_cmd.replace(",", ".")) if resize_cmd is not None else None
    clip_from_time = None
    clip_to_time = None

    if from_time_cmd is not None:
        if ":" in from_time_cmd:
            time_array = from_time_cmd.split(":")
            clip_from_time = extract_time(time_array)
        else:
            clip_from_time = float(from_time_cmd.replace(",", "."))
    else:
        clip_from_time = 0

    if to_time_cmd is not None:
        if ":" in to_time_cmd:
            time_array = to_time_cmd.split(":")
            clip_to_time = extract_time(time_array)
        else:
            clip_to_time = float(to_time_cmd.replace(",", "."))
    else:
        clip_to_time = get_clip_duration(input_file_cmd)

    print("\n" +
          f"From time: {clip_from_time if clip_from_time is not None else 'From the start'}, "
          f"to time: {clip_to_time if clip_to_time is not None else 'To the end'}. "
          f"To speed: {speed if speed is not None else 'None'} "
          f"Resize: {resize if resize is not None else 'default size'} "
          )
    return input_file_cmd, output_file_cmd, clip_from_time, clip_to_time, speed, resize
