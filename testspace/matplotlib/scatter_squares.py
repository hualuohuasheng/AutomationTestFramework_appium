# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

x_value = list(range(1,1006))
y_value = list(value ** 2 for value in x_value)

# plt.scatter(x_value,y_value,c='red',edgecolor='none',s=40)
# plt.scatter(x_value,y_value,c=(0,0,0.8),edgecolor='none',s=40)
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Reds,edgecolor='none',s=40)

plt.title('Square Numbers',fontsize=24)
plt.xlabel('Square of Value',fontsize=14)
plt.ylabel('Value',fontsize=14)

plt.axis([0,1100,0,1100000])
# plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()

# plt.savefig('squares_plot.png',bbox_inches='tight')