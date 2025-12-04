#read text
with open("main/day3/batteries.txt") as f:
    batteries = f.readlines()
    voltage = 0
    for battery in batteries:
        battery = battery.rstrip("\n").split()
        battery_list = []
        for number in battery[0]:
            battery_list.append(int(number))
        i = 12
        remaining_index = 12
        joltage_list = []
        while i > 0:
            if i == 1:
                max_i = max(battery_list)
                joltage_list.append(max_i * (10**(i - 1)))
                break
            max_i = max(battery_list[:-(i- 1)])
            max_i_index = battery_list.index(max_i)
            battery_list[max_i_index] = -1
            battery_list = battery_list[max_i_index+1:]
            joltage_list.append(max_i * (10**(i - 1)))
            i -= 1
        voltage += sum(joltage_list)
   


    print(voltage)