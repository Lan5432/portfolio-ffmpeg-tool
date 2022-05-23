from src.moviepy_editor import moviepy_gif, moviepy_mp4, get_clip_duration
from os.path import exists
from os import remove

input_file = "files/test.mp4"


def _generate_output_file_name(extension):
    output_file_name = "output_test"
    return "files/" + output_file_name + extension


def _clean_up(output_file):
    if exists(output_file):
        remove(output_file)


# def test_mp4():
#     from_time_input = 5
#     to_time_output = 10
#     output_file = _generate_output_file_name(".mp4")
#     moviepy_mp4(input_file, output_file, from_time_input, to_time_output)
#     try:
#         assert round(get_clip_duration(output_file)) == 5
#         assert ".mp4" in output_file
#         assert exists(output_file)
#     finally:
#         _clean_up(output_file)
#
#
# def test_gif():
#     from_time_input = 10
#     to_time_output = 12
#     output_file = _generate_output_file_name(".gif")
#     moviepy_gif(input_file, output_file, from_time_input, to_time_output)
#     try:
#         assert round(get_clip_duration(output_file)) == 2
#         assert ".gif" in output_file
#         assert exists(output_file)
#     finally:
#         _clean_up(output_file)

