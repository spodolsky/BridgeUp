import matplotlib.pyplot as plt
import matplotlib.image as img
plt.clf()
image = img.imread("world-map.gif")
plt.imshow(image, extent = [0, 197.349, -64, 88.809])
QuakeData = open("currentQuakes.txt")
QuakeData.readline()
LAT = []
LONG = []
for line in QuakeData:
    line = line.split(',')
    LAT.append(float(line[1]))
    LONG.append(float(line[2]))
plt.scatter(LONG, LAT, label = "o")
plt.show()