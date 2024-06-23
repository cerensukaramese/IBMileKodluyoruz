import math

points = [
    (1, 2),
    (4, 6),
    (7, 1),
    (3, 9),
    (5, 5)
]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print("Tüm nokta çiftleri arasındaki Öklid mesafeleri:", distances)
print("En küçük Öklid mesafesi:", min_distance)
