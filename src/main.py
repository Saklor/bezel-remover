from moviepy.editor import *
from math import floor

blackPixel = [0, 0, 0]


def isBlackPixel(pixel):
    return (pixel == blackPixel).all()


def firstNonBlackPixelIndex(row):
    left = 0
    right = floor(len(row)/2)

    if isBlackPixel(row[right]):
        return -1

    while right > left + 1:
        middle = floor((right + left) / 2)
        if isBlackPixel(row[middle]):
            left = middle
        else:
            right = middle
    return right


def lastNonBlackPixelIndex(row):
    return len(row) - 1 - firstNonBlackPixelIndex(list(reversed(row)))


def calculateBlackPixelValues(clip):
    firstFrame = clip.get_frame(0)

    return firstFrame[0][0]


videoClip = VideoFileClip(sys.argv[1])
blackPixel = calculateBlackPixelValues(videoClip)
firstFrameFirstRow = videoClip.get_frame(0)[0]

vfx.crop(videoClip,
         x1=firstNonBlackPixelIndex(firstFrameFirstRow),
         x2=lastNonBlackPixelIndex(firstFrameFirstRow)).write_videofile(sys.argv[2], codec='mpeg4')

videoClip.close()
