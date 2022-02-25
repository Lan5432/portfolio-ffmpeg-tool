from src.input_parse import get_parsed_inputs
from common import generate_input


def test_fromtime_inseconds_remains():
    input_args = generate_input("files/test.mp4", "result.gif", input_from_time="2")
    result_input, result_output, result_from_time, result_to_time, result_speed, result_resize \
        = get_parsed_inputs(input_args)
    assert result_from_time == 2


def test_totime_inseconds_remains():
    input_args = generate_input("files/test.mp4", "result.gif", input_to_time="2")
    result_input, result_output, result_from_time, result_to_time, result_speed, result_resize \
        = get_parsed_inputs(input_args)
    assert result_to_time == 2


def test_fromtime_intimestring_converts_properly():
    input_args = generate_input("files/test.mp4", "result.gif", input_from_time="04:05")
    result_input, result_output, result_from_time, result_to_time, result_speed, result_resize \
        = get_parsed_inputs(input_args)
    assert result_from_time == 245


def test_totime_intimestring_converts_properly():
    input_args = generate_input("files/test.mp4", "result.gif", input_to_time="04:05")
    result_input, result_output, result_from_time, result_to_time, result_speed, result_resize \
        = get_parsed_inputs(input_args)
    assert result_to_time == 245


def test_fromtime_omitted_defaults_to_start_time():
    input_args = generate_input("files/test.mp4", "result.gif")
    result_input, result_output, result_from_time, result_to_time, result_speed, result_resize \
        = get_parsed_inputs(input_args)
    assert result_from_time == 0


def test_totime_omitted_defaults_to_end_time():
    input_args = generate_input("files/test.mp4", "result.gif")
    result_input, result_output, result_from_time, result_to_time, result_speed, result_resize \
        = get_parsed_inputs(input_args)
    assert result_to_time == 25.12

def test_speed():
    input_args = generate_input("files/test.mp4", "result.gif", input_speed="9")
    result_input, result_output, result_from_time, result_to_time, result_speed, result_resize \
        = get_parsed_inputs(input_args)
    assert result_speed == 9

def test_resize():
    input_args = generate_input("files/test.mp4", "result.gif", input_resize="3")
    result_input, result_output, result_from_time, result_to_time, result_speed, result_resize \
        = get_parsed_inputs(input_args)
    assert result_resize == 3

