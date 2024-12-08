import math

def euclideanDistance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculateAllDistances(points):
    distances = []
    for a in points:
        for b in points:
            if a != b:
                distances.append(euclideanDistance(a, b))
    return distances

def findMinimumDistance(distances):
    minDistance = distances[0]
    for distance in distances:
        if distance < minDistance:
            minDistance = distance
    print("Minimum distance of these points is: " + str(minDistance))

points = [(0, 3), (4, 0)]

distances = calculateAllDistances(points)
findMinimumDistance(distances)
