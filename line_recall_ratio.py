import matplotlib.pyplot as plt
import numpy as np
import xlrd
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
plt.rcParams['figure.figsize'] = (8, 6)

data = xlrd.open_workbook('data/line_data.xlsx')
sheet_ratio = data.sheets()[0]
sheet_recall = data.sheets()[1]

names = ['ratio', 'recall']
name = names[0]

# /100
ratio_L1 = [x / 100 for x in sheet_ratio.col_values(0)]
ratio_L2 = [x / 100 for x in sheet_ratio.col_values(1)]
ratio_QD = [x / 100 for x in sheet_ratio.col_values(2)]
ratio_Rand = [x / 100 for x in sheet_ratio.col_values(3)]
ratio_index = np.arange(0, 20, step=1)
ratio_x_label = [str(int(x)) for x in sheet_ratio.col_values(5)]
# ratio_x_label.append('r"$\\times 10^{2}$"')
for i in range(len(ratio_x_label)):
    if i % 2 == 0:
        ratio_x_label[i] = ' '
ratio_ylim = [1, 1.35]
ratio_x_name = 'ratio'

# /10000
recall_L1 = [x / 10000 for x in sheet_recall.col_values(0)]
recall_L2 = [x / 10000 for x in sheet_recall.col_values(1)]
recall_QD = [x / 10000 for x in sheet_recall.col_values(2)]
recall_Rand = [x / 10000 for x in sheet_recall.col_values(3)]
recall_x_label = [str(int(x)) for x in sheet_recall.col_values(5)]
recall_index = np.arange(0, 20, step=1)
for i in range(len(recall_x_label)):
    if i % 2 == 0:
        recall_x_label[i] = ' '
# recall_x_label[0] = '100'
recall_xlim = [0, 2100]
recall_ylim = [0, 1.25]
recall_x_name = 'recall'

y_names = {'ratio': 'Ratio', 'recall': 'Recall'}
y_factors = {'ratio': 1.001, 'recall': 1.005}
y_labels = {'ratio': [1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35], 'recall': [0, 0.25, 0.5, 0.75, 1.0, 1.25]}

A = eval(name + '_L1')
B = eval(name + '_L2')
C = eval(name + '_QD')
D = eval(name + '_Rand')

index = eval(name + '_index')
x_label = eval(name + '_x_label')
x_name = eval(name + '_x_name')
ylim = eval(name + '_ylim')
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
ax = plt.subplot(1, 1, 1)
ax.grid(axis='y', linestyle=':', alpha=0.4)
ax.grid(axis='x', alpha=0)
ax.grid(zorder=1)
plt.rc('font', family='ARIAL', size=25)
ms = 20

plt.plot(index, B, color='r', ls='-', linewidth=2, marker='o', markersize=ms, markeredgecolor='black',
         markeredgewidth=2, label='L2',
         zorder=10)
plt.plot(index, A, color='darkblue', ls='-.', linewidth=2, marker='v', markersize=ms, markeredgecolor='black',
         markeredgewidth=2,
         label='L1')
plt.plot(index, C, color='g', ls='--', linewidth=2, marker='s', markersize=ms, markeredgecolor='black',
         markeredgewidth=2, label='QD')
plt.plot(index, D, color='black', ls=':', linewidth=2, marker='x', markersize=ms, label='Rand')

# plt.title('square Numbers', fontsize=24)
# !!!!!!!!!!!!!!!!
# plt.ylim(ylim[0], ylim[1])
plt.yticks(y_labels[name], fontsize=25)
# plt.yticks(, fontsize=17)

plt.xticks(index, x_label, fontsize=20)
# plt.ylim(ymin=1)
plt.xlim(xmin=0, xmax=19)
# plt.xlabel(x_name, fontsize=23)    recall_x_label
# !!!!!!!!!!!!!!!!
plt.text(0, ylim[1] * y_factors[name], y_names[name], fontsize=34)
# plt.text(19, 1, 'r$\\times 10 ^ {2}$', fontsize=30, zorder=5)
plt.xlabel('T', fontsize=34)

border_width = 1
plt.legend(loc='upper right', ncol=4, fontsize=19, facecolor='none')

ax = plt.subplot(1, 1, 1)
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)
plt.subplots_adjust(top=0.93, bottom=0.13, right=0.95, left=0.11, hspace=0, wspace=0)
plt.savefig('graph/recall&ratio/' + name + '.eps', format='eps', dpi=300)
plt.show()
