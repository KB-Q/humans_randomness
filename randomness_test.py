# All tests return dataframe with the test result appended as new column
import pandas as pd
import numpy as np


def frequency_test(df):
    """
    Find relative frequency of 1-s.
    """
    frequency_test_column = []

    # For every string in dataframe
    for i in range(len(df)):
        string = df.loc[i]['String']

        # Relative frequency
        freq = string.count('1') / len(string)
        frequency_test_column.append(freq)

    df['freq_test'] = frequency_test_column
    return df


def frequency_std_test(df, m):
    """
    Split string into non-overlapping blocks of size m.
    Find standard deviation of relative frequencies of 1-s within blocks.
    """
    frequency_std_test_column = []

    # For every string in dataframe
    for i in range(len(df)):
        string = df.loc[i]['String']

        number_of_blocks = int(np.floor(len(string) / m))
        block_start_index = 0
        block_end_index = m

        # List of relative frequencies for all blocks
        block_freq_list = []

        # For every block in string
        for k in range(number_of_blocks):
            block_data = string[block_start_index:block_end_index]

            # Relative frequency within block
            block_freq = block_data.count('1') / m
            block_freq_list.append(block_freq)

            block_start_index += m
            block_end_index += m

        # Standard deviation of frequencies for all blocks
        std = np.std(block_freq_list)
        frequency_std_test_column.append(std)

    df['freq_std_test'] = frequency_std_test_column
    return df


def running_frequency_std_test(df):
    """
    Find standard deviation of running relative frequencies of 1-s.
    """
    running_frequency_std_test_column = []

    # For every string in dataframe
    for i in range(len(df)):
        string = df.loc[i]['String']

        # List of running frequencies
        run_freq_list = []

        # For every element in string
        for k in range(1, len(string)):
            # Running relative frequency
            run_freq = string[:k].count('1') / len(string)
            run_freq_list.append(run_freq)

        # Standard deviation of running frequencies
        std = np.std(run_freq_list)
        running_frequency_std_test_column.append(std)

    df['rfreq_std_test'] = running_frequency_std_test_column
    return df


def run_test(df):
    """
    Find total number of runs (run is an uninterrupted sequence of identical bits).
    """
    run_test_column = []

    # For every string in dataframe
    for i in range(len(df)):
        string = df.loc[i]['String']
        runs = 0

        # For every element in string
        for k in range(1, len(string)):
            if string[k] != string[k - 1]:
                runs += 1
        run_test_column.append(runs)

    df['run_test'] = run_test_column
    return df


def block_test(df, m):
    """
    Split string into non-overlapping blocks of size m=3 or m=4.
    Find frequencies of all 2^m unique patterns and their standard deviation.
    """
    block_test_column = []

    pattern_3_list = ['000', '100', '010', '001', '110', '101', '011', '111']
    pattern_4_list = ['0000', '1000', '0100', '0010', '0001', '1100', '1010', '0101', '1001', '0011', '0110', '1110',
                      '0111', '1101', '1011', '1111']

    if m == 3:
        pattern_list = pattern_3_list
    else:
        pattern_list = pattern_4_list

    # For every string in dataframe
    for i in range(len(df)):
        string = df.loc[i]['String']

        number_of_blocks = int(np.floor(len(string) / m))

        # List of pattern counts
        pattern_count_list = []

        # For every pattern
        for pattern in pattern_list:
            pattern_count = 0

            # Check with the sliding window
            for k in range(number_of_blocks):
                block_start_index = k * m
                block_end_index = block_start_index + m
                block_data = string[block_start_index:block_end_index]
                inner_count = 0

                while inner_count < m:
                    sub_block = block_data[inner_count:inner_count + m]
                    if sub_block == pattern:
                        # Pattern found, the window slides to the position after the found pattern
                        pattern_count += 1
                        inner_count += m
                    else:
                        # Pattern not found, the window slides one position forward
                        inner_count += 1
            pattern_count_list.append(pattern_count)

        # Standard deviation of pattern counts
        std = np.std(pattern_count_list)
        block_test_column.append(std)

    df['block_{}_test'.format(m)] = block_test_column
    return df


def alternation_test(df, m):
    """
    Find total number of non-overlapping blocks "101010..." and "010101..." of length m (m is even).
    """
    alternation_test_column = []

    pattern1 = '10' * int(m / 2)
    pattern2 = '01' * int(m / 2)

    # For every string in dataframe
    for i in range(len(df)):
        string = df.loc[i]['String']

        number_of_blocks = int(np.floor(len(string)/m))
        pattern_count = 0

        # Check with the sliding window
        for k in range(number_of_blocks):
            block_start_index = k * m
            block_end_index = block_start_index + m
            block_data = string[block_start_index:block_end_index]
            inner_count = 0

            while inner_count < m:
                sub_block = block_data[inner_count:inner_count + m]
                if sub_block == pattern1:
                    # Pattern found, the window slides to the position after the found pattern
                    pattern_count += 1
                    inner_count += m
                elif sub_block == pattern2:
                    # Pattern found, the window slides to the position after the found pattern
                    pattern_count += 1
                    inner_count += m
                else:
                    # Pattern not found, the window slides one position forward
                    inner_count += 1
        alternation_test_column.append(pattern_count)

    df['alter_{}_test'.format(m)] = alternation_test_column
    return df


def monotonicity_test(df, m):
    """
    Find total number of non-overlapping blocks "111111..." and "000000..." of length m.
    """
    monotonicity_test_column = []

    pattern1 = '1' * m
    pattern2 = '0' * m

    # For every string in dataframe
    for i in range(len(df)):
        string = df.loc[i]['String']

        number_of_blocks = int(np.floor(len(string) / m))
        pattern_count = 0

        # Check with the sliding window
        for k in range(number_of_blocks):
            block_start_index = k * m
            block_end_index = block_start_index + m
            block_data = string[block_start_index:block_end_index]
            inner_count = 0

            while inner_count < m:
                sub_block = block_data[inner_count:inner_count + m]
                if sub_block == pattern1:
                    # Pattern found, the window slides to the position after the found pattern
                    pattern_count += 1
                    inner_count += m
                elif sub_block == pattern2:
                    # Pattern found, the window slides to the position after the found pattern
                    pattern_count += 1
                    inner_count += m
                else:
                    # Pattern not found, the window slides one position forward
                    inner_count += 1

        monotonicity_test_column.append(pattern_count)
    df['mono_{}_test'.format(m)] = monotonicity_test_column
    return df
