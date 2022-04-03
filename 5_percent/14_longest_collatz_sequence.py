import _common_functions as cf


def longest_collatz_sequence(max):
    """
    max: maximum number to test the longest chain of
    return: number of the largest collatz sequence below max
    """
    longest_chain = []
    for i in range(1, max + 1):  # limit up to max
        chain = [i]  # starting number of sequence
        while chain[-1] != 1:  # tests if sequence is finished
            if chain[-1] % 2 == 0:  # tests if the previous number of the sequence is even
                chain.append(chain[-1] // 2)
            else:
                chain.append(3 * chain[-1] + 1)
        if len(chain) > len(longest_chain):
            longest_chain = chain
    return longest_chain[0]


assert longest_collatz_sequence(
    1000000) == 837799, "longest_collatz_sequence(1000000), 837799"
print(cf.average_running_time(1, longest_collatz_sequence, 1000000))
# Average running time of longest_collatz_sequence for 1 tests:
# 48.818769454956055 seconds
