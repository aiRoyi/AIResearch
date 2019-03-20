import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    total_times = 10000
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    #数据可视化
    plt.hist(result_arr, bins=range(2, 14), density=1, edgecolor='black', linewidth=1, rwidth=0.8)
    tick_lables = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_lables)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')

    # x = range(1, total_times + 1)
    # plt.scatter(x, roll1_arr, c='red', alpha=0.5)
    # plt.scatter(x, roll2_arr, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
