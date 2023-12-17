import argparse
from ffmpeg_editor import get_clip_duration


def extract_time(time_array):
    """
    Converts hh:mm:ss timestamps to just seconds
    :param time_array: The timestamp split into a list [hh, mm, ss]
    :return: A sum of the time in seconds
    """
    if len(time_array) == 2:
        return float(time_array[0]) * 60 + float(time_array[1])
    elif len(time_array) == 3:
        return float(time_array[2]) * 3600 + float(time_array[1]) * 60 + float(time_array[2])


def get_parsed_inputs():
    """
    Captures the arguments to be parsed
    :return: A Python object with the arguments as properties
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input")
    arg_parser.add_argument("output")
    arg_parser.add_argument("--fromTime", required=False, type=str)
    arg_parser.add_argument("--toTime", required=False, type=str)
    arg_parser.add_argument("--speed", required=False, type=float)
    arg_parser.add_argument("--resize", required=False, type=float)
    return _parse_inputs(
        arg_parser.parse_args()
    )


def _parse_inputs(input_args):
    """
    Sanitizes and parses all inputs
    :param input_args: Args parsed by get_parsed_inputs
    :return: Values in order: the input file name, the output file name, starting time we wish to clip, final time we wish to clip to, speed, and resize factor.
    Time can be specified as just seconds, float seconds, or hh:mm:ss timestamps.
    """
    input_file_cmd = input_args.input
    output_file_cmd = input_args.output
    from_time_cmd = input_args.fromTime
    to_time_cmd = input_args.toTime
    speed_cmd = input_args.speed
    resize_cmd = input_args.resize

    speed = float(speed_cmd) if speed_cmd is not None else None
    resize = float(resize_cmd) if resize_cmd is not None else None
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
          f"To speed: {speed if speed is not None else 'Same speed'} "
          f"Resize: {resize if resize is not None else 'Same size'} "
    )
    return input_file_cmd, output_file_cmd, clip_from_time, clip_to_time, speed, resize
