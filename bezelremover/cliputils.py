from math import floor


class ClipUtils:
    def __init__(self, clip):
        super().__init__()
        self.clip = clip
        self.blackPixel = self.calculateBlackPixelValues()

    def isBlackPixel(self, pixel):
        return (pixel == self.blackPixel).all()

    def firstNonBlackPixelIndex(self, row):
        left = 0
        right = floor(len(row)/2)

        if self.isBlackPixel(row[right]):
            return -1

        while right > left + 1:
            middle = floor((right + left) / 2)
            if self.isBlackPixel(row[middle]):
                left = middle
            else:
                right = middle
        return right

    def lastNonBlackPixelIndex(self, row):
        return len(row) - 1 - self.firstNonBlackPixelIndex(list(reversed(row)))

    def calculateBlackPixelValues(self):
        return self.clip.get_frame(0)[0][0]

    def calculateXOffset(self):
        firstFrameFirstRow = self.clip.get_frame(0)[0]
        return (self.firstNonBlackPixelIndex(firstFrameFirstRow),
                self.lastNonBlackPixelIndex(firstFrameFirstRow))
