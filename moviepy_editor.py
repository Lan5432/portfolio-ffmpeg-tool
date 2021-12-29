from moviepy.editor import vfx
from moviepy.video.io.VideoFileClip import VideoFileClip


def moviepy_gif(input_file, output_file, from_time=0, to_time=0, resize=None, slow_mo=None):
    clip = _clip_file(input_file, from_time, to_time, resize, slow_mo)
    clip.write_gif(output_file)


def moviepy_mp4(input_file, output_file, from_time=0, to_time=0, resize=None, slow_mo=None):
    clip = _clip_file(input_file, from_time, to_time, resize, slow_mo)
    clip.write_videofile(output_file)


def _clip_file(input_file, from_time=0, to_time=0, resize=None, slow_mo=None):
    clip = VideoFileClip(input_file)

    from_time = from_time if from_time is not None else 0
    to_time = from_time + to_time if to_time is not None else round(clip.duration - from_time, 2)
    clip = clip.subclip(from_time, to_time)

    if resize is not None:
        clip = clip.resize(resize)
    if slow_mo is not None:
        clip = clip.fx(vfx.speedx, slow_mo)
    return clip
