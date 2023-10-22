# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    points = []
    minSegment = segments[0]

    # find the lowest segment
    for segment in segments:
        if segment.end < minSegment.end:
            minSegment = segment

    # remove the min segment
    segments.remove(minSegment)

    enclosedSegments = []
    for segment in segments.copy():
        if segment.start <= minSegment.end:
            enclosedSegments.append(segment)
            segments.remove(segment)

    points.append(minSegment.end)

    if len(segments) == 0:
        return points
    else:
        points.extend(optimal_points(segments))
    return points


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=" ")
