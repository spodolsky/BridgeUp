import numpy as np
import matplotlib.pyplot as plt
import csv

#generate cloud cover percentage map for 2017
CCData = open("CloudFraction1_2017.csv", 'r')
csvReader = csv.reader(CCData, delimiter=',')
cloudcover = list(csvReader)
CCArray = np.empty([len(cloudcover), len(cloudcover[0]), 3], dtype=np.uint8)
CCData.seek(0)
cc1 = [255, 0, 0]
cc2 = [255, 124, 0]
cc3 = [255, 243, 0]
cc4 = [193, 255, 0]
cc5 = [100, 255, 0]
cc6 = [0, 255, 54]
cc7 = [0, 255, 158]
cc8 = [0, 255, 255]
cc9 = [0, 174, 255]
cc10 = [0, 62, 255]
rowcount = -1

for row in csvReader:
    rowcount+=1
    colcount = -1
    
    for value in row:
        colcount+=1
        
        if 0 <= float(value) < 0.1:
            CCArray[rowcount,colcount,0]=cc1[0]
            CCArray[rowcount,colcount,1]=cc1[1]
            CCArray[rowcount,colcount,2]=cc1[2]
       
        elif 0.1 < float(value) < 0.2:
           CCArray[rowcount,colcount,0]=cc2[0]
           CCArray[rowcount,colcount,1]=cc2[1]
           CCArray[rowcount,colcount,2]=cc2[2]
            
        elif 0.2 < float(value) < 0.3:
           CCArray[rowcount,colcount,0]=cc3[0]
           CCArray[rowcount,colcount,1]=cc3[1]
           CCArray[rowcount,colcount,2]=cc3[2]
    
        elif 0.3 < float(value) < 0.4:
           CCArray[rowcount,colcount,0]=cc4[0]
           CCArray[rowcount,colcount,1]=cc4[1]
           CCArray[rowcount,colcount,2]=cc4[2]
           
        elif 0.4 < float(value) < 0.5:
            CCArray[rowcount,colcount,0]=cc5[0]
            CCArray[rowcount,colcount,1]=cc5[1]
            CCArray[rowcount,colcount,2]=cc5[2]
        
        elif 0.5 < float(value) < 0.6:
            CCArray[rowcount,colcount,0]=cc6[0]
            CCArray[rowcount,colcount,1]=cc6[1]
            CCArray[rowcount,colcount,2]=cc6[2]
         
        elif 0.6 < float(value) < 0.7:
            CCArray[rowcount,colcount,0]=cc7[0]
            CCArray[rowcount,colcount,1]=cc7[1]
            CCArray[rowcount,colcount,2]=cc7[2]
      
        elif 0.7 < float(value) < 0.8:
            CCArray[rowcount,colcount,0]=cc8[0]
            CCArray[rowcount,colcount,1]=cc8[1]
            CCArray[rowcount,colcount,2]=cc8[2]
       
        elif 0.8 < float(value) < 0.9:
            CCArray[rowcount,colcount,0]=cc9[0]
            CCArray[rowcount,colcount,1]=cc9[1]
            CCArray[rowcount,colcount,2]=cc9[2]
      
        elif 0.9 < float(value) <= 1:
           CCArray[rowcount,colcount,0]=cc10[0]
           CCArray[rowcount,colcount,1]=cc10[1]
           CCArray[rowcount,colcount,2]=cc10[2]
plt.clf()
plt.suptitle("Cloud Cover Percentage in 2017", y=.8)
plt.imshow(CCArray)
plt.axis('off')
plt.show()  

#generate temperature map for cloud cover percentage in 2002
csvFile = open("CloudFraction1_2002.csv")
csvReader = csv.reader(csvFile, delimiter=',')
stringMatrix = list(csvReader)

numCols = len(stringMatrix[0])
numRows = len(stringMatrix)

grid = np.empty([numRows, numCols, 3],dtype=np.uint8)
csvFile.seek(0)

rownum = -1
for row in csvReader:
    rownum += 1
    colnum = -1
    for value in row:
        colnum += 1
        if float(value) < 0.1:
             grid[rownum, colnum] = cc1
        elif 0.1 < float(value) < 0.2:
            grid[rownum,colnum] = cc2
        elif 0.2 < float(value) < 0.3:
            grid[rownum,colnum] = cc3
        elif 0.3 < float(value) < 0.4:
            grid[rownum,colnum] = cc4
        elif 0.4 < float(value) < 0.5:
            grid[rownum,colnum] = cc5
        elif 0.5 < float(value) < 0.6:
            grid[rownum,colnum] = cc6
        elif 0.6 < float(value) < 0.7:
            grid[rownum,colnum] = cc7
        elif 0.7 < float(value) < 0.8:
            grid[rownum,colnum] = cc8
        elif 0.8 < float(value) < 0.8:
            grid[rownum,colnum] = cc9
        elif 0.9 < float(value) <= 1:
            grid[rownum,colnum] = cc10

               
plt.clf()
plt.suptitle("Cloud Cover Percentage in 2002", y=.80)
plt.imshow(grid)
plt.axis('off')
plt.show()
