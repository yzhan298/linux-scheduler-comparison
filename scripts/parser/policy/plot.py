'''
XML parsing and plot benchmark for different policy

For class project 221 2017 winter

'''
#import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
from retrive_info import *

minn, maxn = 0, 0

# Latt, C-Ray, 7-Zip Compression, Hackbench, FFmpeg, John The Ripper
x_name = [] # this is the names on x-axis
for name in score_dict:
    x_name.append(name)
x_name[1] = "7-Zip"
print(x_name)
N = len(x_name) # this is the number of 

#latt, ms, less is better
latt_p = [] # the policies of latt
latt_score = [] # the scores of latt
for item in score_dict['Latt']:
    latt_p.append(item[1])
    latt_score.append(int(item[2]))
# normalization
minn, maxn = min(latt_score), max(latt_score)
for i,v in enumerate(latt_score):
    latt_score[i] = 1 - (v - minn)/(maxn - minn)
'''
#c-ray, s, less is better
cray_p = [] # the policies of C-Ray
cray_score = [] # the scores of C-Ray
for item in score_dict['C-Ray']:
    #print(item[2])
    cray_p.append(item[1])
    cray_score.append(float(item[2]))
# normalization
print(cray_score)
minn, maxn = min(cray_score), max(cray_score)
for i,v in enumerate(cray_score):
    cray_score[i] = 1 - (v - minn)/(maxn - minn)
'''
#7-zip, MIPS, more is better
sevenzip_p = [] # the policies of 7-zip
sevenzip_score = [] # the scores of 7-zip
for item in score_dict['7-Zip Compression']:
    #print(item)
    sevenzip_p.append(item[1])
    sevenzip_score.append(int(item[2]))
# normalization
minn, maxn = min(sevenzip_score), max(sevenzip_score)
for i,v in enumerate(sevenzip_score):
    sevenzip_score[i] = (v - minn)/(maxn - minn)

# hackbench has 4 configs, s, less is better
hackbench_c = [] # configs of Hackbench
hackbench_p = [] # the policies of Hackbench
hackbench_score = [] # the scores of Hackbench
for i, item in enumerate(score_dict['Hackbench']):
    #print(item)
    if i%7 == 0:
        hackbench_c.append(item[0])
    hackbench_p.append(item[1])
    hackbench_score.append(float(item[2]))
# normalization
minn, maxn = min(hackbench_score[:7]), max(hackbench_score[:7])
for i in range(0,7):
    hackbench_score[i] =1 - (hackbench_score[i] - minn)/(maxn - minn)
minn, maxn = min(hackbench_score[7:14]), max(hackbench_score[7:14])
for i in range(7,14):
    hackbench_score[i] =1 - (hackbench_score[i] - minn)/(maxn - minn)
minn, maxn = min(hackbench_score[14:21]), max(hackbench_score[14:21])
for i in range(14,21):
    hackbench_score[i] =1 - (hackbench_score[i] - minn)/(maxn - minn)
minn, maxn = min(hackbench_score[21:28]), max(hackbench_score[21:28])
for i in range(21,28):
    hackbench_score[i] =1 - (hackbench_score[i] - minn)/(maxn - minn)

#ffmpeg, s, less is better
ff_p = [] # the policies of FFmpeg
ff_score = [] # the scores of FFmpeg
for item in score_dict['FFmpeg']:
    #print(item)
    ff_p.append(item[1])
    ff_score.append(float(item[2]))
# normalization
minn, maxn = min(ff_score), max(ff_score)
for i,v in enumerate(ff_score):
    ff_score[i] = 1 - (v - minn)/(maxn - minn)

#john the ripper has 3 configs, REAL C/S, more is better
jtr_c = [] # the configs of John The Ripper
jtr_p = [] # the policies of John The Ripper
jtr_score = [] # the scores of John The Ripper
for i, item in enumerate(score_dict['John The Ripper']):
    #print(item)
    if i%7 == 0:
        jtr_c.append(item[0])
    jtr_p.append(item[1])
    jtr_score.append(int(item[2]))
# normalization
minn, maxn = min(jtr_score[:7]), max(jtr_score[:7])
for i in range(0,7):
    jtr_score[i] = (jtr_score[i] - minn)/(maxn - minn)
minn, maxn = min(jtr_score[7:14]), max(jtr_score[7:14])
for i in range(7,14):
    jtr_score[i] = (jtr_score[i] - minn)/(maxn - minn)
minn, maxn = min(jtr_score[14:21]), max(jtr_score[14:21])
for i in range(14,21):
    jtr_score[i] = (jtr_score[i] - minn)/(maxn - minn)

# modify x_name with configs
#print(x_name)
x_name[2], x_name[3] = x_name[3], x_name[2]
x_name[3] = "Hackbench\n(Pipes,Process)"
x_name[4] = "John The Ripper\n(DES)"
x_name.append("Hackbench\n(Sockets,Process)")
x_name.append("Hackbench\n(Sockets,Thread)")
x_name.append("Hackbench\n(Pipes,Thread)")
x_name.append("John The Ripper\n(MD5)")
x_name.append("John The Ripper\n(Blowfish)")
x_name[7], x_name[4] = x_name[4], x_name[7]
#print(x_name)

# rearrange scores
conf_list1 = []
num_config = len(latt_score)
#print(num_config)
for i in range(0,num_config):
    temp_list = []
    temp_list.append(latt_score[i])
    temp_list.append(sevenzip_score[i])
    temp_list.append(ff_score[i])
    temp_list.append(hackbench_score[i])
    temp_list.append(jtr_score[i])
    temp_list.append(hackbench_score[i+14])
    temp_list.append(hackbench_score[i+21])
    temp_list.append(hackbench_score[i+7])
    temp_list.append(jtr_score[i+7])
    temp_list.append(jtr_score[i+14])
    temp_list[4], temp_list[7] = temp_list[7], temp_list[4]
    conf_list1.append(temp_list)
#print(conf_list1)
#print(len(conf_list1))

# plotting
#ind = np.arange(N+5)  # the x locations for the groups
ind =  np.array([0,2,4,6,8,10,12,14,16,18])
#print(ind)
width = 0.15 # the width of the bars

colormap = plt.cm.gist_ncar
cmaps = [colormap(i) for i in np.linspace(0, 0.9, 7)]
#color={colormap(i) for i in np.linspace(0, 0.9, 7)}
print(colormap)
fig, ax = plt.subplots()
for i in range(0,num_config):
    ax.bar(ind+(i-3)*width, conf_list1[i], width,label=latt_p[i], color=cmaps[i])


# add some text for labels, title and axes ticks
ax.set_ylabel('Benchmark Scores')
ax.set_title('Scheduler Comparison')
ax.set_xticks(ind + width / (N+5))
#ax.set_xticklabels(('Latt', 'C-Ray', '7-Zip', 'Hackbench', 'FFmpeg', 'John The Ripper'))
ax.set_xticklabels(x_name,size='x-small',stretch='extra-condensed', rotation=20, ha='right')
#ax.legend()
#ax.set_yscale('log',nonposy='clip')
ax.legend(loc='best',bbox_to_anchor=(1, 1.02))
#ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('b1', 'p2', 'p3', 'p4', 'p5'))

'''
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
'''

plt.show()


