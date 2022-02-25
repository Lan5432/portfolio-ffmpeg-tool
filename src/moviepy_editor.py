from moviepy.editor import vfx
from moviepy.video.io.VideoFileClip import VideoFileClip


def moviepy_gif(input_file, output_file, from_time, to_time, speed=None, resize=None):
    clip = _clip_file(input_file, from_time, to_time, speed, resize)
    clip.write_gif(output_file)
    clip.close()


def moviepy_mp4(input_file, output_file, from_time, to_time, speed=None, resize=None):
    clip = _clip_file(input_file, from_time, to_time, speed, resize)
    clip.write_videofile(output_file)
    clip.close()


def get_clip_duration(input_file):
    return VideoFileClip(input_file).duration


def _clip_file(input_file, from_time=0, to_time=0, speed=None, resize=None):
    clip = VideoFileClip(input_file)

    clip = clip.subclip(from_time, to_time)

    if speed is not None:
        clip = clip.fx(vfx.speedx, speed)
    if resize is not None:
        clip = clip.resize(resize)
    return clip
