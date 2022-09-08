def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return num_freq(str(num1)) == num_freq(str(num2))


def num_freq(call):
    counter = {}

    for num in call:
        counter[num] = counter.get(num,0) +1

    return counter

