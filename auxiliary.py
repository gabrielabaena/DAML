import numpy as np
import pandas as pd


def check_outliers(x: np.ndarray, tolerance: float = 2) -> list:
    """
    Takes as an input a column of the dataframe, and returns the indexes of the outliers, that are not in \
    [mean - tolerance * std, mean + tolerance * std]

    :param x: Input array to be verified
    :param tolerance: How many standard deviations are accepted from the mean  
    """

    mean = x.mean()
    std = x.std()

    lim_inf = mean - tolerance * std
    lim_sup = mean + tolerance * std

    outliers_index_list = []

    for idx, term in enumerate(x):
        if term < lim_inf or term > lim_sup:
            outliers_index_list.append(idx)

    return outliers_index_list


# Remove all the code after this line when testing is finished
if __name__ == "__main__":
    test_data = np.random.rand(20)
    print(test_data)
    print(check_outliers(test_data, tolerance=2))
