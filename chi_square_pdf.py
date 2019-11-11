from scipy.special import gamma
import matplotlib.pyplot as plt
import math
import numpy as np


def chi_square_pdf(x, k):
    y = (pow(0.5, k / 2) * pow(x, k / 2 - 1) * pow(math.e, -x / 2)) / gamma(k / 2)
    return y


plt.rc('font', family='Times New Roman')

x = np.arange(0, 50, 0.1)
y = chi_square_pdf(x, 15)

points = [(8.5468, 0), (8.5468, chi_square_pdf(8.5468, 15))]
(xpoints, ypoints) = zip(*points)
plt.plot(xpoints, ypoints, color='black')

points = [(22.3071, 0), (22.3071, chi_square_pdf(22.3071, 15))]
(xpoints, ypoints) = zip(*points)
plt.plot(xpoints, ypoints, color='black')

points = [(15, 0), (15, chi_square_pdf(15, 15))]
(xpoints, ypoints) = zip(*points)
plt.plot(xpoints, ypoints, color='black')

plt.ylim(bottom=0, top=0.1)
plt.xlim(left=0, right=50)

# plt.title("Chi-Square")
plt.plot(x, y, color='black')
x1 = np.arange(0, 8.5468, 0.1)
x2 = np.arange(8.5468, 22.3071, 0.1)
x3 = np.arange(22.3071, 50, 0.1)

plt.fill_between(x=x1, y1=chi_square_pdf(x1, 15), y2=0, facecolor='gold', interpolate=True)
plt.fill_between(x=x2, y1=chi_square_pdf(x2, 15), y2=0, facecolor='#33b864', interpolate=True)
plt.fill_between(x=x3, y1=chi_square_pdf(x3, 15), y2=0, facecolor='red', interpolate=True)

# plt.plot(x, y, color='darkolivegreen')
# plt.xticks(ticks=[8.5468, 15, 22.3071], labels=[r'$u$', r"$r^{'}$", r'$v$'])
ax = plt.gca()
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.savefig('graph/chisquare/' + 'Chi-Square' + '.png', format='png', dpi=300)
# plt.show()
