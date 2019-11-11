import matplotlib.pyplot as plt
import xlrd
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
plt.rcParams['figure.figsize'] = (8, 6)

ratio_time = xlrd.open_workbook('data/0716/ratiotime2.xlsx')
recall_time = xlrd.open_workbook('data/0716/recalltime2.xlsx')

# plt.rcParams['figure.figsize'] = (8, 4)

# 设置数据集
str_books = ['ratio_time', 'recall_time']
str_sheets = ['trevi', 'cifar', 'deep']
# 0-1
str_book = str_books[1]
# 0-2
str_sheet = str_sheets[1]

y_label = {'ratio_time': 'Ratio', 'recall_time': 'Recall'}
legend_loc = {'ratio_time': 'upper right', 'recall_time': 'bottom right'}
left = {'ratio_timetrevi': 0.16, 'ratio_timecifar': 0.14,
        'ratio_timedeep': 0.14, 'recall_timetrevi': 0.1, 'recall_timecifar': 0.1, 'recall_timedeep': 0.1,
        }
x_factors = {'ratio_timecifar': -2, 'ratio_timetrevi': 10,
             'ratio_timedeep': 30, 'recall_timedeep': 30, 'recall_timecifar': -1.5,
             'recall_timetrevi': 0}
y_factors = {'ratio_timecifar': 1.001, 'ratio_timetrevi': 1.0001,
             'ratio_timedeep': 1.0005, 'recall_timedeep': 1.01, 'recall_timecifar': 1.01,
             'recall_timetrevi': 1.005}

ylims = {'ratio_timecifar': [1, 1.1], 'ratio_timetrevi': [1, 1.0125],
         'ratio_timedeep': [1, 1.04], 'recall_timedeep': [0.57, 1], 'recall_timecifar': [0.2, 1],
         'recall_timetrevi': [0.6, 1]}

xlims = {'ratio_timemnist': [0.01, 0.031], 'ratio_timecifar': [0.08796, 0.214], 'ratio_timetrevi': [0.031, 0.30],
         'ratio_timedeep': [0.065, 0.53], 'recall_timedeep': [0.065, 0.53], 'recall_timecifar': [0.08, 0.22],
         'recall_timetrevi': [0.024, 0.41],
         'recall_timemnist': [0.009, 0.031]}

# file name
book = eval(str_book)

sheet_cifar = book.sheets()[0]
sheet_trevi = book.sheets()[1]
sheet_deep = book.sheets()[2]

# sheet name
sheet = eval('sheet_' + str_sheet)

SRS = [x for x in sheet.col_values(0) if x != ""]
SRS_index = [x * 1000 for x in sheet.col_values(1) if x != ""]
QALSH = [x for x in sheet.col_values(2) if x != ""]
QALSH_index = [x * 1000 for x in sheet.col_values(3) if x != ""]
MUL_LSH = [x for x in sheet.col_values(4) if x != ""]
MUL_LSH_index = [x * 1000 for x in sheet.col_values(5) if x != ""]
PM_LSH = [x for x in sheet.col_values(6) if x != ""]
PM_LSH_index = [x * 1000 for x in sheet.col_values(7) if x != ""]
R_LSH = [x for x in sheet.col_values(8) if x != ""]
R_LSH_index = [x * 1000 for x in sheet.col_values(9) if x != ""]
LScan = [x for x in sheet.col_values(10) if x != ""]
LScan_index = [x * 1000 for x in sheet.col_values(11) if x != ""]

A_name = SRS.pop(0)
B_name = QALSH.pop(0)
C_name = MUL_LSH.pop(0)
D_name = PM_LSH.pop(0)
E_name = R_LSH.pop(0)
F_name = LScan.pop(0)

SRS_index.pop(0)
QALSH_index.pop(0)
MUL_LSH_index.pop(0)
PM_LSH_index.pop(0)
R_LSH_index.pop(0)
LScan_index.pop(0)

A = SRS
B = QALSH
C = MUL_LSH
D = PM_LSH
E = R_LSH
F = LScan

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
ax = plt.subplot(1, 1, 1)
# ax.grid(axis='y', linestyle=':', alpha=0.4)
# ax.grid(axis='x', alpha=0)
# ax.grid(zorder=1)
plt.rc('font', family='ARIAL', size=25)
ms = 15
plt.plot(PM_LSH_index, D, color='r', ls='-', linewidth=3, marker='o', markeredgecolor='black', markeredgewidth=2,
         label='PM-LSH',
         markersize=ms, zorder=10)
plt.plot(SRS_index, A, color='darkblue', ls='-.', linewidth=3, marker='v', markeredgecolor='black', markeredgewidth=2,
         label='SRS',
         markersize=ms)
plt.plot(QALSH_index, B, color='orange', ls=':', linewidth=3, marker='^', markeredgecolor='black', markeredgewidth=2,
         label='QALSH',
         markersize=ms)
plt.plot(MUL_LSH_index, C, color='g', ls='--', linewidth=3, marker='s', markeredgecolor='black', label='Multi-Probe',
         markeredgewidth=2,
         markersize=ms)
plt.plot(R_LSH_index, E, color='indigo', ls='--', linewidth=3, marker='+', markeredgewidth=2,
         label='R-LSH',
         markersize=ms)
plt.plot(LScan_index, F, color='black', ls='-.', linewidth=3, marker='x', label='LScan', markeredgewidth=2,
         markersize=ms)
# plt.title('square Numbers', fontsize=24)
# !!!!!!!!!!!!!!!!
# plt.ylim(ylim[0], ylim[1])
plt.yticks(fontsize=35)
if str_sheet is 'trevi' and str_book is 'ratio_time':
    plt.yticks(fontsize=25)
ylim = ylims[str_book + str_sheet]
plt.xticks(fontsize=35)
plt.ylim(bottom=ylim[0], top=ylim[1])
plt.xlabel('Time (ms)', fontsize=34)
# plt.xlim(left=0, right=0.6)
# !!!!!!!!!!!!!!!!

plt.text(x_factors[str_book + str_sheet], ylim[1] * y_factors[str_book + str_sheet], y_label[str_book], fontsize=34)

border_width = 1
# plt.legend(ncol=4, fontsize=11, facecolor='none')

ax = plt.subplot(1, 1, 1)
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)
plt.subplots_adjust(top=0.90, bottom=0.16, right=0.97, left=left[str_book + str_sheet], hspace=0, wspace=0)
plt.savefig('graph/' + str_book + '/' + str_sheet + '_' + str_book + '.eps', format='eps', dpi=300)
plt.show()
