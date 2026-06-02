
def get_unique_char(message):  # O(n^2)
    unique_char = []
    for character in message:  # O(n)
        unique = True
        # check if the character has already been added to unique_char list
        for e in unique_char:  # O(n)
            if e == character:
                # change unique to False if the character already exist in unique_char list
                unique = False
                break
        if unique:
            unique_char.append(character)  # O(1) amortized
    return unique_char


def get_frequency(message, unique_char):  # O(n^2)
    # use a dictionary where
    #   the key is the unique character
    #   the value is the frequency
    frequency = {}
    for character in unique_char:  # O(n)
        char_freq = 0
        # count the number of occurrences of the current character
        for e in message:  # O(n)
            if character == e:
                # increase char_freq by 1 every time a character in message
                # is the same as a character in the unique_char list
                char_freq += 1
        frequency[character] = char_freq  # Average case O(1) or Amortized worst case O(n)
    return frequency


def get_occurring_probability(message, frequency):  # O(n)
    # use a dictionary where
    #   the key is the unique character
    #   the value is the probability of occurrence
    probability = {}
    message_length = len(message)
    for key, value in frequency.items():  # O(n)
        # probability of occurrence of a unique character = frequency/message_length
        probability[key] = value / message_length
    return probability


def get_cumulative_sum(lower_bound, upper_bound, probability_ls):  # O(n) (where append to a list takes O(1) amortized)
    cumulative_sum = [lower_bound]
    diff_btw_two_bounds = upper_bound - lower_bound
    char_lower_bound = lower_bound
    for probability in probability_ls:  # O(n)
        char_upper_bound = char_lower_bound + (diff_btw_two_bounds * probability)
        cumulative_sum.append(char_upper_bound)  # O(1) amortized
        char_lower_bound = char_upper_bound
    return cumulative_sum


def associate_key_with_interval(cumulative_sum, unique_char):  # O(n) (where adding to a dictionary O(1) average case)
    # use a dictionary where
    #   the key is the unique character
    #   the value is a list of length 2 where
    #       - the first element is the lower bound
    #       - the second element is the upper bound
    interval = {}
    i = 0
    j = 0
    while i < len(cumulative_sum) - 1:  # O(n)
        key = unique_char[j]
        lower_bound = cumulative_sum[i]
        upper_bound = cumulative_sum[i + 1]
        interval[key] = [lower_bound, upper_bound]  # Average case O(1) or Amortized worst case O(n)
        i += 1
        j += 1
    return interval


# get_tag() takes O(n^2) (if get_cumulative_sum() and associate_key_with_interval() take O(n))
def get_tag(probability, unique_char, message):
    # put all values from probability dictionary into a probability list
    probability_ls = []
    for key, value in probability.items():  # O(n)
        probability_ls.append(value)  # O(1) amortized
    # then use the probability list to calculate cumulative sum of probability_ls
    # initially, the lower bound is 0.0 and the upper bound is 1.0
    cumulative_sum = get_cumulative_sum(0.0, 1.0, probability_ls)  # O(n) (where append to a list takes O(1) amortized)
    print('Cumulative sum for interval [0, 1): ', cumulative_sum)
    # associate each key with its interval
    interval_dict = associate_key_with_interval(cumulative_sum,
                                                unique_char)  # O(n) (where adding to a dictionary O(1) average case)

    # get the tag
    tag = 0.0
    for character in message:  # O(n)
        # get the interval of the current character (narrow down the interval)
        char_interval = interval_dict.get(character)  # Average case O(1) or Amortized worst case O(n)
        # get the lower and upper bound of the interval of the current character
        char_lower_bound = char_interval[0]
        char_upper_bound = char_interval[1]
        # calculate the tag: tag = average of lower and upper bound
        # the tag is recalculated until the last element in the message is reached
        tag = (char_lower_bound + char_upper_bound) / 2.0
        # every time the interval is narrowed down:
        #   - get the new cumulative sum for the new interval
        #   - each key will have a new lower and upper bound in the new interval
        cumulative_sum = get_cumulative_sum(char_lower_bound, char_upper_bound,
                                            probability_ls)  # O(n) (where append to a list takes O(1)
        interval_dict = associate_key_with_interval(cumulative_sum,
                                                    unique_char)  # O(n) (where adding to a dictionary O(1) average case)
    return tag


def concatenate_char(ls):  # O(n)
    string = ''
    for e in ls:  # O(n)
        string += e
    return string


def arithmetic_encoding(message):  # O(n^2)
    # generate a list that contains unique characters in the message
    unique_char = get_unique_char(message)  # O(n^2)
    print('Unique char in the message: ', unique_char)
    # get frequency of occurrences of all unique characters in the message
    frequency = get_frequency(message, unique_char)  # O(n^2)
    print('Frequency of each unique character: ', frequency)
    # get probability of occurrence of all unique characters in the message
    probability = get_occurring_probability(message, frequency)  # O(n)
    print('Occurring probability of each unique character: ', probability)
    # get the tag: get_tag() takes O(n^2) (if get_cumulative_sum() and associate_key_with_interval() take O(n))
    tag = get_tag(probability, unique_char, message)  # O(n^2)
    return tag, probability


def arithmetic_decoding(probability, message_length, tag):  # O(n^2)
    # put all values from probability dictionary into a probability list
    # put all keys from probability dictionary into a unique_char list
    probability_ls = []
    unique_char = []
    for key, value in probability.items():  # O(n)
        probability_ls.append(value)  # O(1) amortized
        unique_char.append(key)  # O(1) amortized
    # then use the probability list to calculate cumulative sum of probability_ls
    # initially, the lower bound is 0.0 and the upper bound is 1.0
    cumulative_sum = get_cumulative_sum(0.0, 1.0, probability_ls)  # O(n) (where append to a list takes O(1) amortized)
    # associate each key with its interval
    interval_dict = associate_key_with_interval(cumulative_sum,
                                                unique_char)  # O(n) (where adding to a dictionary O(1) average case)
    print(cumulative_sum,interval_dict)
   # breakpoint()
    print("tiposaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    i = 0
    message_char_ls = []
    current_lower_bound = 0.0
    current_upper_bound = 1.0
    while i < message_length:  # O(n)
        for key, value in interval_dict.items():  # O(n)
            # get the interval of the current character (key)
            lower_bound = value[0]
            upper_bound = value[1]
            if i==16:
                breakpoint()
            # check if tag is within the interval of the current character (key)
            if (tag > lower_bound) and (tag < upper_bound):
                # narrow down the interval
                current_lower_bound = lower_bound
                current_upper_bound = upper_bound
                # add the character to message_char_ls if tag is within the interval of the current character (key)
                message_char_ls.append(key)  # O(1) amortized
                break
        # every time the interval is narrowed down:
        #   - get the new cumulative sum for the new interval
        #   - each key will have a new lower and upper bound in the new interval
        cumulative_sum = get_cumulative_sum(current_lower_bound, current_upper_bound,
                                            probability_ls)  # O(n) (where append to a list takes O(1) amortized)
        interval_dict = associate_key_with_interval(cumulative_sum,
                                                    unique_char)  # O(n) (where adding to a dictionary O(1) average case)
        i += 1

    return concatenate_char(message_char_ls)


def run_arithmetic_coding():

    message = 'alksdjfalkdsjfalsdkjaaslkdjfalskdjflaskdjfalsdjb'
    message_len = len(message)
    print('The message is ', message)
    print('The length of the message is', message_len)

    tag, probability = arithmetic_encoding(message)
    print('The tag for ', message, ' is ', tag)
    
    #exit()
    decoded_msg = arithmetic_decoding(probability, message_len, tag)
    print('Decode the message using probability (coding model), message length, and the generated tag: ', decoded_msg)


if __name__ == '__main__':
    run_arithmetic_coding()

