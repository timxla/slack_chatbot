import matplotlib.pyplot as plt
import json

dictionary = json.load(open('2022-06-06_statistics.json', 'r'))
xAxis = [key for key, value in dictionary.items()]
yAxis = [value for key, value in dictionary.items()]
plt.grid(False)

## BAR GRAPH ##
col = ['#123FFF','#00FF11','#123456','#F21451','#245124','#AF2D22','#AADDFF','#DDBBFF','#11FFDD','#CCAADD','#DDBBAA','#33AABB','#44BBFF','#55CC25','#AABBCC','#FDABCD','#ABCFDB','#ABDFBC','#2FAFBF','#ABDFDF']
plt.bar(xAxis,yAxis, color=col)
plt.xlabel('Clothing')
plt.ylabel('Value')
plt.xticks(rotation=30,fontsize=5)
#plt.show()
plt.savefig('report.png')