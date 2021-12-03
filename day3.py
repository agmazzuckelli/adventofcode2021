def main():
    
    diagnostics = []

    with open('./inputs/day3input.txt') as input:
        for line in input:
            diagnostics.append([int(i) for i in line.rstrip()]) # list-ify each input to make it searchable later

    def process_digits(bins, index_to_process):
        ''' Return list of counts of 0s, 1s for that index position
        '''
        counts = [0, 0] # count of 0s, 1s
        indexes_of_zeroes = []
        indexes_of_ones = []
        for idx, bin in enumerate(bins):
            if bin[index_to_process] == 0:
                counts[0] += 1
                indexes_of_zeroes.append(idx)
            elif bin[index_to_process] == 1:
                counts[1] += 1
                indexes_of_ones.append(idx)
        return counts, indexes_of_zeroes, indexes_of_ones          
 
    def find_measure(bins, measure):
        measure_value = []
        for i in range(0, len(bins[0])): # assume all instructions same length
            counts = process_digits(bins, i)[0]
            most = 0 if counts[0] > counts[1] else 1
            least = 1 - most
            if measure == 'gamma':
                measure_value.append(most)
            elif measure == 'epsilon':
                measure_value.append(least)
        return measure_value

    def reduce_list(bins, index_to_process, measure):
        counts, zero_indexes, one_indexes = process_digits(bins, index_to_process)
        most = 0 if counts[0] > counts[1] else 1 # 1 wins in tie
        least = 1 - most
        reduced_list = []
        if measure == 'oxygen':
            relevant_list = zero_indexes if most == 0 else one_indexes
            for index in relevant_list:
                reduced_list.append(bins[index])
        if measure == 'carbon':
            relevant_list = zero_indexes if least == 0 else one_indexes
            for index in relevant_list:
                reduced_list.append(bins[index])
        return reduced_list            

    def find_measure_prob_two(bins, index_to_process, measure):
        # seemed a bit natural to recurse along along a smaller problem until our base of one item left
        if len(bins) == 1:
            return bins[0]
        else:
            reduced_list = reduce_list(bins, index_to_process, measure)
            return find_measure_prob_two(reduced_list, index_to_process + 1, measure) # index_to_process increments as we reduce list size this was the key

    test_bins = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    test_bins = [[int(i) for i in item] for item in test_bins]

    # list_of_bins = test_bins
    list_of_bins = diagnostics
    # print(list_of_bins)
    gamma = find_measure(list_of_bins, 'gamma')
    epsilon = find_measure(list_of_bins, 'epsilon')

    oxygen = find_measure_prob_two(list_of_bins, 0, 'oxygen')
    carbon = find_measure_prob_two(list_of_bins, 0, 'carbon')

    return gamma, epsilon, oxygen, carbon

if __name__=='__main__':
    gamma, epsilon, oxygen, carbon = main()
    print('gamma:', gamma, 'epsilon:', epsilon)
    print('oxygen:', oxygen, 'carbon:', carbon)
    gamma_dec = int(''.join(map(str, gamma)), 2)
    epsilon_dec = int(''.join(map(str, epsilon)), 2)
    oxygen_dec = int(''.join(map(str, oxygen)), 2)
    carbon_dec = int(''.join(map(str, carbon)), 2)
    print('gamma_dec:', gamma_dec, 'epsilon_dec:', epsilon_dec)
    print('oxygen_dec', oxygen_dec, 'carbon_dec:', carbon_dec)
    print('power:', gamma_dec * epsilon_dec)
    print('life_support_rating:', oxygen_dec * carbon_dec)
