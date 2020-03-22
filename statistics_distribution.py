
import random
import matplotlib.pyplot as plt
import numpy as np
def distribution_counter(num_array, interval, start=None, end=None, fig_path=None, cumulative=True):
    """
        if the num_array ranges from

    Args:
        num_array:
        start:
        end:
        interval:
        fig_path:
        cumulative:

    Returns:

    """
    num_array = np.array(num_array)
    if not start:
        start = np.min(num_array)
    if not end:
        end = np.max(num_array)

    # plt.figure()
    split_num = (end - start) / interval
    plt.hist(num_array, bins=np.linspace(start, end, split_num), normed=True, cumulative=cumulative)
    # plt.hist(query_lengths, bins='auto', normed=True, cumulative=True)

    if fig_path:
        plt.savefig(fig_path, dpi=300)
    else:
        plt.show()

def find_long_sentence(path):
    fr1 = open(path,'r',encoding='utf-8').readlines()#original data
    leng = len(fr1)
    len_list = []
    frnew = open('sample_'+ path, 'w', encoding='utf-8')
    p = 0
    for i in range(40000000, leng):
        tmp = fr1[i].strip().split(" ")
        if len(tmp) > 45:
            frnew.write(fr1[i])
            p += 1
        if i % 1000000 == 0:
            print(i)
        if p >= 40000:
            return
    # distribution_counter(len_list, 1, 0, 200, cumulative=True)

