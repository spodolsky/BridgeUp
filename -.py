import matplotlib.pyplot as plt
import matplotlib.image as img
plt.clf()
QuakeData = open("currentQuakes.txt")
QuakeData.readline()
LAT = []
LONG = []
for line in QuakeData:
    line = line.split(',')
    LAT.append(float(line[1]))
    LONG.append(float(line[2]))
plt.scatter(LONG, LAT, label = "o")
image = img.imread("world-map.gif")
plt.imshow(image, extent = [-197.962, 197.701, -63.8313, 87.9263])
plt.show()
