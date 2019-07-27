# coding=utf-8

# 导入
import numpy as np


def fill_array(t):
    """
    对数组中含有nan的一系列操作
    :param t:传入的数组
    :return: 返回计算后的数组
    """
    for i in range(t.shape[1]):  # 遍历每一列

        temp_col = t[:, i]  # 取出当前一列的值

        nan_num = np.count_nonzero(temp_col != temp_col)  # 判断当前一列中nan的个数

        if nan_num != 0:  # 不为0,说明当前这一列中有nan
            temp_not_col = temp_col[temp_col == temp_col]  # 取出当前一列不为nan的array
            temp_col[np.isnan(temp_col)] = temp_not_col.mean()  # 选中当前nan的位置,替换成不为nan的均值

    return t


if __name__ == '__main__':
    # 创建数组
    t1 = np.arange(24).reshape((4, 6)).astype("float")

    # 修改为nan
    t1[1, 2:] = np.nan
    print(t1)

    # 处理nan
    t2 = fill_array(t1)
    print(t2)
