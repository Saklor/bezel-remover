from moviepy.editor import *
from .commandline import parseArguments
from .cliputils import ClipUtils


def main():
    arguments = parseArguments()

    videoClip = VideoFileClip(arguments.input)
    clipUtils = ClipUtils(videoClip)

    x1, x2 = clipUtils.calculateXOffset()
    videoClip = vfx.crop(videoClip, x1=x1, x2=x2)

    arguments.outputResult(videoClip, arguments.output)

    videoClip.close()
