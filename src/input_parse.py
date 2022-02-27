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
    arg_parser.add_argument("--fromTime", required=False, type=str)
    arg_parser.add_argument("--toTime", required=False, type=str)
    arg_parser.add_argument("--speed", required=False, type=float)
    arg_parser.add_argument("--resize", required=False, type=float)
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

    print("\n" +
          f"From time: {from_time_cmd if from_time_cmd is not None else 'From the start'}, "
          f"to time: {to_time_cmd if to_time_cmd is not None else 'To the end'}. "
          f"To speed: {speed_cmd if speed_cmd is not None else 'None'} "
          f"Resize: {resize_cmd if resize_cmd is not None else 'default size'} "
          )
    return input_file_cmd, output_file_cmd, from_time_cmd, to_time_cmd, speed_cmd, resize_cmd
