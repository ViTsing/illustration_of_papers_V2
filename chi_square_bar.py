import matplotlib.pyplot as plt

num_list = [0.1, 0.35, 0.1]
index = [2, 6, 10]
plt.xlim(left=0, right=12)
plt.ylim(bottom=0, top=0.6)

plt.rcParams['figure.figsize'] = (8, 4)
plt.rc('font', family='Times New Roman')
ax = plt.gca()
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(Falsplt.xticks([0, 8.5468, 15, 22.3071, 30, 40, 50])e)
ax.spines['left'].set_visible(False)
plt.bar(index[0], num_list[0], 4, facecolor='gold', linewidth=2, edgecolor='black')
plt.bar(index[1], num_list[1], 4, facecolor='#33b864', linewidth=2, edgecolor='black')
plt.bar(index[2], num_list[2], 4, facecolor='red', linewidth=2, edgecolor='black')

# plt.xticks(['i_1', 'i_2', 'i_3'])
plt.savefig('graph/chisquare/' + 'Chi-Square-bar' + '.png', format='png', dpi=300)

plt.show()
