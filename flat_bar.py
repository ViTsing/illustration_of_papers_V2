import numpy as np
import matplotlib.pyplot as plt
import xlrd

# plt.style.use('ggplot')
book = xlrd.open_workbook('data/0716/bar3.xlsx')
sheet = book.sheets()[0]

recall_SRS = sheet.row_values(2)
recall_QA = sheet.row_values(3)
recall_MUL = sheet.row_values(4)
recall_PM_Tree = sheet.row_values(5)

ratio_SRS = sheet.row_values(9)
ratio_QA = sheet.row_values(10)
ratio_MUL = sheet.row_values(11)
ratio_PM_Tree = sheet.row_values(12)

time_SRS = sheet.row_values(21)
time_QA = sheet.row_values(22)
time_MUL = sheet.row_values(23)
time_PM_Tree = sheet.row_values(24)

recall_ylim = [0.4, 1]
ratio_ylim = [1, 1.03]
time_ylim = [0.9, 2.5]

name = 'time'
x_labels = {'ratio': 'Ratio', 'recall': 'Recall', 'time': 'Time'}
y_factors = {'ratio': 1.0005, 'recall': 1.01, 'time': 1.01}

bar_1 = eval(name + '_SRS')
bar_2 = eval(name + '_QA')
bar_3 = eval(name + '_MUL')
bar_4 = eval(name + '_PM_Tree')
ylim = eval(name + '_ylim')

index = np.array([1, 2, 3, 4, 5, 6, 7])
x_ticks = ['Audio', 'MNIST', 'NUS', 'Trevi', 'Cifar', 'GIST', 'Deep']

bar_width = 0.2
line_width = 1.0
plt.rc('font', family='serif', size=20)
# plt.rc('axes', axisbelow=True)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['figure.figsize'] = (16, 4)

plt.xticks(index + bar_width, x_ticks, fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(0.5, 8)
plt.ylim(ylim[0], ylim[1])  # y轴取值范围
# plt.ylabel("FScore", rotation='horizontal')
plt.text(0.5, ylim[1] * y_factors[name], x_labels[name], fontsize=16)
# plt.xlabel('', fontsize=25)

border_width = 1
ax = plt.subplot(1, 1, 1)
ax.grid(axis='y', linestyle=':', alpha=0.4)
ax.grid(axis='x', alpha=0)
ax.grid(zorder=1)
# hatch {'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}

plt.bar(index + bar_width * 0, bar_4, bar_width, facecolor='w', edgecolor='black',
        linewidth=line_width,
        label='PM-LSH', alpha=0.7, zorder=2, hatch='x')
plt.bar(index + bar_width * 1, bar_1, bar_width, facecolor='lightsteelblue', edgecolor='black', linewidth=line_width,
        label='SRS', alpha=0.6, zorder=2, hatch='')
plt.bar(index + bar_width * 2, bar_2, bar_width, facecolor='cornflowerblue', edgecolor='black',
        linewidth=line_width,
        label='QALSH', alpha=0.7, zorder=2, hatch='\\')
plt.bar(index + bar_width * 3, bar_3, bar_width, facecolor='mediumblue', edgecolor='black',
        linewidth=line_width,
        label='Multi-Probe', alpha=0.7, zorder=2, hatch='//')

# , bbox_to_anchor=(1, 1.3)
plt.legend(loc='upper right', bbox_to_anchor=(1, 1.15), ncol=4, fontsize=12, facecolor='none')

ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)

file_name = name + '_bar'
plt.subplots_adjust(top=0.85, bottom=0.1, right=0.97, left=0.1, hspace=0, wspace=0)
plt.savefig('graph/bar/' + file_name + '.pdf', format='pdf', dpi=300)
# plt.show()
plt.close()
