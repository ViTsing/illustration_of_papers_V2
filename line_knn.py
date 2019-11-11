import matplotlib.pyplot as plt
import xlrd
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
plt.rcParams['figure.figsize'] = (8, 6)

file_names = ['cifar_knn', 'trevi_knn', 'deep_knn']
file_save_name = {'cifar_knn': 'cifar', 'trevi_knn': 'trevi', 'deep_knn': 'deep'}
metrics = ['time', 'recall', 'ratio']
# 0-2
file_name = file_names[0]
# 0-2
metric = metrics[0]
left = {'cifar_knntime': 0.08, 'cifar_knnrecall': 0.1, 'cifar_knnratio': 0.16,
        'trevi_knntime': 0.12, 'trevi_knnrecall': 0.1, 'trevi_knnratio': 0.14,
        'deep_knntime': 0.11, 'deep_knnrecall': 0.1, 'deep_knnratio': 0.14}
y_labels = {'recall': 'Recall', 'ratio': 'Ratio', 'time': 'Time (ms)'}
y_factors = {'cifar_knntime': 1.01, 'cifar_knnrecall': 1.001, 'cifar_knnratio': 1.0001,
             'trevi_knntime': 1.01, 'trevi_knnrecall': 1.001, 'trevi_knnratio': 1.0001,
             'deep_knntime': 1.01, 'deep_knnrecall': 1.005, 'deep_knnratio': 1.0001}
xlims = {'fixed': [1, 100]}
ylims = {'cifar_knntime': [0.01, 0.06], 'cifar_knnrecall': [0.7, 1], 'cifar_knnratio': [1, 1.015],
         'trevi_knntime': [0.01, 0.6], 'trevi_knnrecall': [0.68, 1], 'trevi_knnratio': [1, 1.01],
         'deep_knntime': [0.2, 0.55], 'deep_knnrecall': [0.55, 1], 'deep_knnratio': [1, 1.02]}

mnist_knn_data = xlrd.open_workbook('data/0716/knn/' + file_name + '.xlsx')

sheet_time = mnist_knn_data.sheets()[0]
sheet_recall = mnist_knn_data.sheets()[1]
sheet_ratio = mnist_knn_data.sheets()[2]

# time data
times = 1000
time_SRS = sheet_time.col_values(0)
time_QALSH = sheet_time.col_values(1)
time_Multi = sheet_time.col_values(2)
time_PM = sheet_time.col_values(3)
time_R = sheet_time.col_values(4)
time_LS = sheet_time.col_values(5)

time_SRS = [x * times for x in time_SRS]
time_QALSH = [x * times for x in time_QALSH]
time_Multi = [x * times for x in time_Multi]
time_PM = [x * times for x in time_PM]
time_R = [x * times for x in time_R]
time_LS = [x * times for x in time_LS]
# time_index = np.arange(len(time_SRS))
# time_x_label = [str(int(x)) for x in sheet_time.col_values(5)]
time_x_name = 'time'

# ratio data
ratio_SRS = [x for x in sheet_ratio.col_values(0)]
ratio_QALSH = [x for x in sheet_ratio.col_values(1)]
ratio_Multi = [x for x in sheet_ratio.col_values(2)]
ratio_PM = [x for x in sheet_ratio.col_values(3)]
ratio_R = [x for x in sheet_ratio.col_values(4)]
ratio_LS = [x for x in sheet_ratio.col_values(5)]
# ratio_index = np.arange(len(ratio_SRS))
# ratio_x_label = [str(int(x)) for x in sheet_ratio.col_values(5)]
ratio_x_name = 'ratio'

# recall data
recall_SRS = [x for x in sheet_recall.col_values(0)]
recall_QALSH = [x for x in sheet_recall.col_values(1)]
recall_Multi = [x for x in sheet_recall.col_values(2)]
recall_PM = [x for x in sheet_recall.col_values(3)]
recall_R = [x for x in sheet_recall.col_values(4)]
recall_LS = [x for x in sheet_recall.col_values(5)]
# recall_x_label = [str(int(x)) for x in sheet_recall.col_values(5)]
# recall_index = np.arange(len(recall_SRS))
recall_x_name = 'recall'

A = eval(metric + '_SRS')
B = eval(metric + '_QALSH')
C = eval(metric + '_Multi')
D = eval(metric + '_PM')
E = eval(metric + '_R')
F = eval(metric + '_LS')

index = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# x_label = eval(metric + '_x_label')
y_lable = y_labels[metric]
y_factor = y_factors[file_name + metric]
xlim = xlims['fixed']
ylim = ylims[file_name + metric]
if metric is 'time':
    ylim[0] = ylim[0] * times
    ylim[1] = ylim[1] * times
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
# plt.rcParams['figure.figsize'] = (6, 6)

ax = plt.subplot(1, 1, 1)
# ax.grid(axis='y', linestyle=':', alpha=0.4)
# ax.grid(axis='x', alpha=0)
# ax.grid(zorder=1)
plt.rc('font', family='ARIAL', size=25)

ms = 20
lw = 2

plt.plot(index, D, color='r', ls='-', linewidth=2, marker='o', label='PM-LSH', markersize=ms, markeredgecolor='black',
         markerfacecolor='r', zorder=10)
plt.plot(index, A, color='darkblue', ls='-.', linewidth=2, marker='v', label='SRS', markersize=ms,
         markeredgecolor='black', markerfacecolor='darkblue')
plt.plot(index, B, color='orange', ls=':', linewidth=2, marker='^', label='QALSH', markersize=ms,
         markeredgecolor='black', markerfacecolor='orange')
plt.plot(index, C, color='g', ls='--', linewidth=2, marker='s', label='Multi-Probe', markersize=ms,
         markeredgecolor='black', markerfacecolor='g')
plt.plot(index, E, color='indigo', ls='--', linewidth=2, marker='+', label='R-LSH', markersize=ms,
         markerfacecolor='none')
plt.plot(index, F, color='black', ls='-.', linewidth=2, marker='x', label='LScan', markersize=ms,
         markerfacecolor='none')

# plt.plot(index, D, color='black', ls='-', linewidth=2, marker='o', label='PM-Tree', markersize=8)
# plt.plot(index, A, color='black', ls='-.', linewidth=2, marker='v', label='SRS', markersize=8)
# plt.plot(index, C, color='black', ls='--', linewidth=2, marker='s', label='Multi-Probe', markersize=8)
# plt.plot(index, B, color='black', ls=':', linewidth=2, marker='x', label='QALSH', markersize=8)
# plt.plot(index, E, color='black', ls='--', linewidth=2, marker='+', label='R', markersize=8)
# plt.plot(index, F, color='black', ls='-.', linewidth=2, marker='^', label='LS', markersize=8)

# plt.title('square Numbers', fontsize=24)
# !!!!!!!!!!!!!!!!
# plt.ylim(ylim[0], ylim[1])
# plt.yticks([1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35], fontsize=14)

plt.xticks(index, fontsize=30)
plt.ylim(bottom=ylim[0], top=ylim[1])
plt.xlim(left=1, right=100)
plt.yticks(fontsize=30)
if metric is 'ratio':
    plt.yticks(fontsize=25)

plt.xlabel('k', fontsize=34)
# !!!!!!!!!!!!!!!!
plt.text(1, ylim[1] * y_factor, y_lable, fontsize=34)

border_width = 1
# plt.legend(ncol=4, fontsize=11, facecolor='none')
# plt.legend(ncol=6, bbox_to_anchor=(0.001, 1), loc='lower left', fontsize=30)
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)
plt.subplots_adjust(top=0.92, bottom=0.15, right=0.95, left=left[file_name + metric], hspace=0, wspace=0)
plt.savefig('graph/knn/' + file_save_name[file_name] + '_knn_' + metric + '.eps', format='eps', dpi=300)
# =============================================================================
# plt.savefig('graph/knn/' + file_name + '_' + metric + '.jpg', format='JPEG', dpi=1200)
# =============================================================================
plt.show()
