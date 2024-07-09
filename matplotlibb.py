#1.Intro


#We mostly use pyplot in matplotlib, so we stick to it
#importting matplotlib as easy one; also importing numpy for array management as matplotlib works on array

import matplotlib.pyplot as plt, numpy as np

#defining the arrays  to plot on graph, ust like x,y but seperately into x array and y array

xaxis=np.array([1,2,3])
yaxis=np.array([2,3,4])

#now loading the values to the pyplot module, same as dump concept from binary file hadnling


plt.plot(xaxis, yaxis)

#now showing the graph of loaded data

plt.show()

#control + c on terminal to cancel the showing graph


#2.Line styles ---> parameter name on plot : linestyle 
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')   #u can use ls instead linestyle
plt.show()

#3.Line Color ---> parameter name on plot : color
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color = 'r')

#4. Line Width ---> parameter name on plot : linewidth
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '20.5')


#5.Axis Labels --> name of axis
plt.xlabel("X- Axis")
plt.ylabel("Y-axis")


#6.Title --> Name  of graph
plt.title("Statistic Graphical  Data")

#7. Grid --> just like graph sheets default line 
plt.grid()
	#if only for x axis,
	plt.grid(axis = 'x')
"""
Notes:

	Dimension should be same for plotting graph!
	single 

color parameter for plt.plot():
	b : blue
	g : green
	y : yellow
	r : red
	etc...  #hex also allowed

linestyle parameter for plt.plot():

	'dotted', 'dashed', ':', 'None'

	You can also set linewidth, color, linestyle properties to grid too!
"""

#Example for multiple line

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()







#----------------------------
#Example session

#histograph

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()


#Piechart
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show() 


#Bars
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()

#Scatter 
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3])
y = np.array([10,20,30])
plt.scatter(x, y)
plt.show()
