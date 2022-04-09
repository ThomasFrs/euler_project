import _common_functions as cf

# Disclaimer: No matter how bad this looks, I made this and didn't copy it from anywhere else
# and this took some time and i hate how much it didn't relied on maths but rather on brute force
# or i completely missed something


def number_to_word_length(original_number):
    """
    original_number: positive integer
    return: length of original_number fully written out
    """
    number = int(original_number)
    thresholds = [1000, 100, 90, 80, 70, 60, 50, 40, 30, 20, 19,
                  18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    lettered_thresholds = [
        "thousand",
        "hundred",
        "ninety",
        "eighty",
        "seventy",
        "sixty",
        "fifty",
        "forty",
        "thirty",
        "twenty",
        "nineteen",
        "eighteen",
        "seventeen",
        "sixteen",
        "fifteen",
        "fourteen",
        "thirteen",
        "twelve",
        "eleven",
        "ten",
        "nine",
        "eight",
        "seven",
        "six",
        "five",
        "four",
        "three",
        "two",
        "one"]
    number_in_words = []
    while number > 0:
        for n in thresholds:
            if number >= n:
                if number // n > 1:
                    number_in_words.append(
                        lettered_thresholds[thresholds.index(number // n)])
                elif number >= 100:
                    number_in_words.append("one")
                number_in_words.append(
                    lettered_thresholds[thresholds.index(n)])
                number -= n * (number // n)
    if original_number > 100 and original_number % 100 != 0 and "hundred" in number_in_words:
        number_in_words.insert(number_in_words.index("hundred") + 1, "and")
    return len("".join(number_in_words))


def number_letter_counts(max):
    """
    max: positive integer
    return: sum of every length of lettered numbers ranging from 1 to max
    """
    return sum([number_to_word_length(i) for i in range(1, max + 1)])


print(cf.average_running_time(1000, number_letter_counts, 1000))
# Average running time of number_letter_counts for 1000 tests:
# 0.0033513846397399904 seconds
