import yaml

# Returns a string contaning the max number of coins possible to collect, the number of dragons to slay and which dragons to slay
# Returns "-1" is not possible to satisfy the last princess
def dragons_and_princesses(file_name):
    mission_success = True
    
    # Creates a dictionary of steps conataining the steo numbers, their values (princess with dragons slayed, or dragons with gold),
    # and the total number of steps
    with open(file_name, 'r') as file:
        steps = yaml.safe_load(file)
    
    # Inits a dictionary to hold evey slain dragon with its gold value to calculate at the end
    dragons_slayed_and_coins = {}
    first_key = list(steps.keys())[0]
    num_of_steps = (int)(steps[first_key])
    steps.pop(first_key)
    
    # For every step, greedyliy slay each dragon and remove the least valued dragons whenever met with a princess stasfied with the number of
    # dragons slayed so far to meet the recuirment not the marry her
    for step in steps.items():
        current_pair = step[1].split(" ")
        step_key = (int)(step[0])
        step_char = current_pair[0]
        step_val = (int)(current_pair[1])
        
        if step_char == "d":
            dragons_slayed_and_coins[step_key + 1] = step_val
        
        if step_char == "p":
            if step_key < num_of_steps - 1:
                while(len(dragons_slayed_and_coins) >= step_val):
                    min_dragon_value = min(list(dragons_slayed_and_coins.values()))
                    dragons_slayed_and_coins.pop([key for (key, value) in dragons_slayed_and_coins.items() if value == min_dragon_value][0])
            elif step_key >= num_of_steps - 1 and len(dragons_slayed_and_coins) < step_val:
                mission_success = False
                break
    
    ans = "-1"
    
    if mission_success:
        total_num_of_coins = sum(list(dragons_slayed_and_coins.values()))
        total_num_of_dragons_slayed = len(dragons_slayed_and_coins)
        dragons_numbers = ' '.join(map(str, list(dragons_slayed_and_coins.keys())))
        
        ans = f"{total_num_of_coins}\n{total_num_of_dragons_slayed}\n{dragons_numbers}"
        
    return ans

print(dragons_and_princesses('test0.yaml'))
