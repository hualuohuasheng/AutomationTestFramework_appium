# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

input_value = list(range(1,6))
squares = list(value ** 2 for value in input_value)
print(squares)
plt.plot(input_value,squares,linewidth=5)

#设置图表标题，并给坐标轴加上标签
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Squares of Value",fontsize=14)

#坐标轴刻度标记大小
plt.tick_params(axis='both',labelsize=14)

plt.show()