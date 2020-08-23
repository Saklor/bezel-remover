import argparse
from .utils import outputResult, debugOutputResult


def parseArguments():
    parser = argparse.ArgumentParser(
        description='Remove dark bezels from a video.')
    parser.add_argument('input', metavar='input_video', type=str,
                        help='the video that will have its bezels removed')
    parser.add_argument('output', metavar='output', type=str,
                        help='output destination')
    parser.add_argument('--debug', dest='outputResult', action='store_const',
                        const=debugOutputResult, default=outputResult,
                        help='if set the output will be the first frame of the modified video')

    return parser.parse_args()
