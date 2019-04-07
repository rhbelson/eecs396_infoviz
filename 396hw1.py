import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 

f=open("antibiotics_data.csv","r")
bacteria=[]
p=[]
s=[]
n=[]
staining=[]
stains=[]
next(f)
for line in f:
	# print(line)
	attributes=line.split(",")
	if (attributes[0]!="Bacteria"):
		print(attributes[0])
		bacteria.append(attributes[0].split(" ")[0]+"\n"+attributes[0].split(" ")[1])
		p.append(float(attributes[1]))
		s.append(float(attributes[2]))
		n.append(float(attributes[3]))
		print(attributes[4][:-2])
		if (attributes[4][:-2]=="positive" or attributes[4][:-2]=="positi" ):
			staining.append("#3B1DDA")
			stains.append("positive")
		else:
			staining.append("#7BC9ED")
			stains.append("negative")

bacteria=tuple(bacteria)
p=tuple(p)
s=tuple(s)
n=tuple(n)
print(p)
print(s)
print(n)
print(staining)
print(stains)
print(bacteria)

# data to plot
n_groups = 16
# p = (90, 55, 40, 65)
# s = (85, 62, 54, 20)
# n = (75, 52, 34, 20)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8
 
rects1 = plt.bar(index, p, bar_width,
alpha=opacity,
color=staining,
label='Penicillin | Gram Negative')

staining2=[]
for p in range(len(staining)):
	if (staining[p]=="#3B1DDA"):
		staining2.append("#149E2B")
	else:
		staining2.append("#57E66F")
 
rects2 = plt.bar(index + bar_width, s, bar_width,
alpha=opacity,
color=staining2,
label='Streptomycin | Gram Negative')


staining3=[]
for p in range(len(staining)):
	if (staining[p]=="#3B1DDA"):
		staining3.append("#D11548")
	else:
		staining3.append("#F4D1DB")


rects3 = plt.bar(index + 2*bar_width, n, bar_width,
alpha=opacity,
color=staining3,
label='Neomycin | Gram Negative')

patterns = ('', '', '\\', '\\', '', '', '', '', '', '', '','\\', '\\','\\', '\\',
	'\\')
for bar, pattern in zip(rects1, patterns):
    bar.set_hatch(pattern)
for bar, pattern in zip(rects2, patterns):
    bar.set_hatch(pattern)
for bar, pattern in zip(rects3, patterns):
    bar.set_hatch(pattern)




plt.xlabel('Antibiotic Performance')
plt.ylabel('Minimum Inhibitory Concentration (MIC)')
plt.title('MIC of WW2 Antibiotics by Bacteria')
plt.xticks(index + bar_width, bacteria)


red_patch = mpatches.Patch(facecolor='#3B1DDA',edgecolor='black',hatch='///', label='Penicillin | Gram Positive')
blue_patch = mpatches.Patch(facecolor='#149E2B',edgecolor='black',hatch='///',label='Streptomycin | Gram Positive')
green_patch = mpatches.Patch(facecolor='#D11548',edgecolor='black',hatch='///', label='Neomycin | Gram Positive')
red_patch2 = mpatches.Patch(facecolor='#7BC9ED',edgecolor='black',hatch='///', label='Penicillin | Gram Negative')
blue_patch2 = mpatches.Patch(facecolor='#57E66F',edgecolor='black',hatch='///',label='Streptomycin | Gram Negative')
green_patch2 = mpatches.Patch(facecolor='#F4D1DB',edgecolor='black',hatch='///', label='Neomycin | Gram Negative')


plt.legend(handles=[red_patch, blue_patch, green_patch,red_patch2, blue_patch2, green_patch2])

for tick in ax.xaxis.get_major_ticks():
   tick.label.set_fontsize(7) 
ax.set_yscale('log')
 
plt.tight_layout()
plt.show()