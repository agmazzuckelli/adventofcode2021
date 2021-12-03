def main():

    day2_command_list = []

    with open('./inputs/day2input.txt', 'r') as input:
        for line in input:
            day2_command_list.append(line.rstrip())
    
    def execute_single_command_first_prob(command, horizontal_pos, depth):
        direction = command.split(' ')[0]
        amount_to_move = int(command.split(' ')[1])
        if direction == 'forward':
            horizontal_pos[0] += amount_to_move
        elif direction == 'up':
            depth[0] -= amount_to_move
        elif direction == 'down':
            depth[0] += amount_to_move

    def execute_single_command_second_prob(command, horizontal_pos, depth, aim):
        direction = command.split(' ')[0]
        amount_to_move = int(command.split(' ')[1])
        if direction == 'forward':
            horizontal_pos[0] += amount_to_move
            depth[0] += aim[0] * amount_to_move
        elif direction == 'up':
            aim[0] -= amount_to_move
        elif direction == 'down':
            aim[0] += amount_to_move
    
    def process_commands(command_list):
        horizontal_position, depth, aim = [0], [0], [0] # take advantage of list mutability
        for command in command_list:
            # to run both would just need another set of horiz, depth but too lazy for that
            # execute_single_command_first_prob(command, horizontal_position, depth, aim)
            execute_single_command_second_prob(command, horizontal_position, depth, aim)
        return horizontal_position[0], depth[0]
    
    # test_commands = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']
    # print(process_commands(test_commands))

    return process_commands(day2_command_list)


if __name__=='__main__':
    # run once for ans2, change out commented in process_commands lines for ans1
    horizontal, depth = main()
    print('horizontal:', horizontal, 'depth:', depth)
    print('answer:', horizontal * depth)