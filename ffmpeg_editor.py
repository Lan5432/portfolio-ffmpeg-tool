import subprocess
import ffmpeg

vf_string = "fps=30,scale=1600:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse"


def call_ffmpeg_with_args(input_file, output_file, seek_time, to_time):
    ffmpeg.input(input_file) \
        .output(output_file, ss=seek_time, t=to_time, vf=vf_string) \
        .filter() \
        .overwrite_output().run()


def call_ffmpeg_subprocess_with_args(input_file, output_file, seek_time, to_time):
    subprocess.run(["ffmpeg", f" -ss {seek_time}", f" -t {to_time}", " -itsscale 1", f" -i {input_file}", "-y",
                   f" -vf {vf_string}", output_file])
