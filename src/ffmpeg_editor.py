import ffmpeg
from math import modf, ceil


def video_and_audio(input_file, output_file, from_time, to_time, speed, resize):
    """
    Parse video and audio
    :param input_file: Input file name
    :param output_file: Output file name
    :param from_time: Starting moment to clip, video and audio
    :param to_time: Ending moment to clip, video and audio
    :param speed: Speed to be applied to video, removes audio if present
    :param resize: Resizes video
    """
    frame_time = float(get_video_data_(input_file)['r_frame_rate'].split('/')[0])

    start_frame = frame_time * from_time
    end_frame = frame_time * to_time

    input_file = ffmpeg.input(input_file)

    video = input_file.video \
        .trim(start_frame=start_frame, end_frame=end_frame) \
        .setpts('PTS-STARTPTS')  # Resetting frametime after trim

    audio = input_file.audio \
        .filter('atrim', start=from_time, end=to_time) \
        .filter('asetpts', 'PTS-STARTPTS')  # Resetting frametime after trim

    if resize is not None:
        video = video.filter('scale', w=f'{resize}*in_w', h=f'{resize}*in_h')

    output = ffmpeg.output(video, audio, output_file)

    if speed is not None:
        setpts_factor = 1 / speed
        video = video.setpts(f'{setpts_factor}*PTS')
        output = ffmpeg.output(video, output_file)

    output.overwrite_output().run()


def audio(input_file, output_file, from_time, to_time):
    """
    Parse just audio
    :param input_file: Input file name
    :param output_file: Output file name
    :param from_time: Starting audio clip time
    :param to_time: Ending audio clip time
    """
    input_file = ffmpeg.input(input_file)

    input_file.audio \
        .filter('atrim', start=from_time, end=to_time) \
        .filter('asetpts', 'PTS-STARTPTS') \
        .output(output_file).overwrite_output().run()


def get_video_data_(input_file):
    probe = ffmpeg.probe(input_file)
    return next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)


def get_clip_duration(input_file):
    """
    Runs ffprobe to recover the full clip's duration
    :param input_file: The input file, to obtain it.
    :return: Total duration in seconds.
    """
    duration = get_video_data_(input_file)['duration']
    duration_split = modf(float(duration))
    return duration_split[1] + ceil(duration_split[0] * 60)
