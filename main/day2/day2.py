


def is_invalid_id():
    id_list = []
    ids = extract_ids()
    for id in ids:
        for ranges in extract_range(id):
            if find_repeated_sequences(ranges):
                id_list.append(ranges)
    print(sum(id_list))

def extract_ids():
    with open('main\\day2\\idList.txt', 'r') as file:
        for line in file:
            id_list = line.split(',')
        return id_list

def find_repeated_sequences(number):
    sequence_list = extract_possible_sequences(number)
    for sequence in sequence_list:
        #see if sequence exists more than once in list
        if str(number).count(sequence) >= 2 and len(sequence) * str(number).count(sequence) == len(str(number)):
            return True
        
    return False
    

def extract_possible_sequences(number):
    #iterate through id and find all possible sequences
    sequence_list = []
    for i in range(len(str(number))):
        for j in range(i, len(str(number)) + 1):
            sequence_list.append(str(number)[i:j])

    return sequence_list
        
        

def extract_range(id):
    #extract range from id string
    range_list = []

    get_vals = id.split('-')
    min_val = int(get_vals[0])
    max_val = int(get_vals[1])
    for i in range(min_val, max_val + 1):
        range_list.append(i)

    return range_list


is_invalid_id()
