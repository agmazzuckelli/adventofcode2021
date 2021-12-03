def main():

    input_list = []

    with open('./inputs/day1input.txt', 'r') as input:
        for line in input:
            input_list.append(int(line.rstrip()))

    def count_increases(heights):
        higher_than_previous = 0
        for i in range(1, len(input_list)):
            if heights[i] > heights[i-1]:
                higher_than_previous += 1
        return higher_than_previous

    # test_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    # print(count_increases(test_list))    

    def count_window_increases(heights):
        higher_than_previous = 0
        for i in range(0, len(heights)-3):
            rolling_sum_next = heights[i+1] + heights[i+2] + heights[i+3]
            rolling_sum_current = heights[i] + heights[i+1] + heights[i+2]
            if rolling_sum_next > rolling_sum_current:
                higher_than_previous += 1
        return higher_than_previous

    # print(count_window_increases(test_list))

    return count_increases(input_list), count_window_increases(input_list)

if __name__=="__main__":
    """ tests
    >>> test_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    >>> count_increases(test_list)
    7
    >>> count_window_increases(test_list)
    5
    """
    a1, a2 = main()
    print('answer1:', a1, 'answer2:', a2)