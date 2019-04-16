import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 

f=open("minimalist.csv","r")
heights=[]
names=[]
next(f)
for line in f:
	# print(line)
	attributes=line.split(",")
	names.append(attributes[0].replace("\n",""))
	heights.append(int(attributes[1].replace("\n","")))

heights=tuple(heights)
names=tuple(names)
print(heights)
print(names)
# data to plot
n_groups = 13

 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.6
opacity = 0.8
 
rects1 = plt.bar(index, heights,
alpha=opacity,
color="blue",
label='River Name')








plt.xlabel('River')
plt.ylabel('River Length')
plt.title('Longest rivers')
plt.xticks(index + bar_width, names)




plt.legend()

# for tick in ax.xaxis.get_major_ticks():
#    tick.label.set_fontsize(7) 
# ax.set_yscale('log')
 
plt.tight_layout()
plt.show()