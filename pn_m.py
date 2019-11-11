import matplotlib.pyplot as plt
import xlrd
from math import log
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
plt.rcParams['figure.figsize'] = (8, 6)

data = xlrd.open_workbook('data/0716/plot_s_m.xlsx')

sheets = ['s', 'm']
metrics = ['recall', 'time', 'ratio']
# 0-1;1-0;1-1;1-2
sheet = sheets[0]
metric = metrics[1]

sheet_s = data.sheets()[0]
sheet_m = data.sheets()[1]

# s
s = sheet_s.col_values(0)
s_time = [log(x * 1000, 10) for x in sheet_s.col_values(1)]

# m
m = sheet_m.col_values(0)
m_time = [log(x * 1000, 10) for x in sheet_m.col_values(1)]
m_recall = sheet_m.col_values(2)
m_ratio = sheet_m.col_values(3)

left = {'mratio': 0.11, 'stime': 0.11, 'mrecall': 0.15, 'mtime': 0.08}
lines = {'mratio': m_ratio, 'stime': s_time, 'mrecall': m_recall, 'mtime': m_time}
ylims = {'mratio': [1, 1.1], 'stime': [log(14, 10), log(18, 10)], 'mrecall': [0.01, 0.04],
         'mtime': [log(100, 10), log(1000, 10)]}
y_factors = {'mratio': 1.001, 'stime': 1.0005, 'mrecall': 1.01, 'mtime': 1.005}
y_labels = {'recall': 'Recall', 'time': 'Time (ms)', 'ratio': 'Ratio'}

l_m_time = [log(x, 10) for x in [1, 200, 400, 600, 800, 1000]]
l_s_time = [log(x, 10) for x in [15, 15.3, 15.6, 15.9, 16.2, 16.5]]
y_ticks = {'mratio': [1.0, 1.02, 1.04, 1.06, 1.08, 1.1],
           'stime': l_s_time,
           'mrecall': [0, 0.01, 0.02, 0.03, 0.04, 0.05],
           'mtime': l_m_time}
line = lines[sheet + metric]
index = eval(sheet)
xlim = [index[0], index[-1]]
ylim = ylims[sheet + metric]
y_factor = y_factors[sheet + metric]
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['figure.figsize'] = (10, 8)

ax = plt.subplot(1, 1, 1)
# ax.grid(axis='y', linestyle=':', alpha=0.4)
# ax.grid(axis='x', alpha=0)
# ax.grid(zorder=1)
plt.rc('font', family='ARIAL', size=25)

plt.plot(index, line, color='red', ls='-', linewidth=4, marker='o', markersize=30, markeredgecolor='black',
         markeredgewidth=3)

# y_ticks[sheet + metric],
plt.yticks(fontsize=35)
plt.xticks([10, 15, 20, 25], fontsize=35)
if sheet is 's':
    plt.xticks(index, fontsize=35)
plt.ylim(ymin=ylim[0], ymax=ylim[1])
plt.xlim(xmin=xlim[0], xmax=xlim[1])
plt.text(xlim[0], ylim[1] * y_factor, y_labels[metric], fontsize=40)
plt.xlabel(sheet, fontsize=45)
border_width = 1
# plt.legend(loc='upper right', ncol=4, fontsize=14, facecolor='none')

ax = plt.subplot(1, 1, 1)
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)
plt.subplots_adjust(top=0.92, bottom=0.14, right=0.96, left=left[sheet + metric], hspace=0, wspace=0)
plt.savefig('graph/s_m/' + metric + '_' + sheet + '.eps', format='eps', dpi=300)
plt.show()
