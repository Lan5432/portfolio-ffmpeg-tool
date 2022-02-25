
def generate_input(input_file, output_file, input_from_time=None, input_to_time=None, input_speed=None,
                   input_resize=None):
    input_args = [input_file, output_file]
    if input_from_time:
        input_args.append("--fromTime")
        input_args.append(input_from_time)
    if input_to_time:
        input_args.append("--toTime")
        input_args.append(input_to_time)
    if input_speed:
        input_args.append("--speed")
        input_args.append(input_speed)
    if input_resize:
        input_args.append("--resize")
        input_args.append(input_resize)
    return input_args
