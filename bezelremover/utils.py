def outputResult(clip, dest):
    clip.write_videofile(dest, codec='mpeg4')


def debugOutputResult(clip, dest):
    clip.save_frame(dest)
