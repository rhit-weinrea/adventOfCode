def merge_ranges(range_list):
    range_list.sort()
    merged = []
    for r in range_list:
        if len(merged) == 0 or r[0] > merged[-1][1] + 1:
            merged.append(list(r))
        else:
            merged[-1][1] = max(merged[-1][1], r[1])

    return merged


def extract_ranges():
    with open('main\\day5\\id.txt', 'r') as file:
        range_list = []
        count = 0
        for line in file:
            line = line.strip()
            if '-' in line:
                a, b = map(int, line.split('-'))
                range_list.append((a, b))
            if(line.count('-') == 0 and line.strip() != ''):
                get_vals = line.rstrip('\n')
                for range in range_list:
                    if int(get_vals) >= range[0] and int(get_vals) <= range[1]:
                        count += 1
                        break

            


    merged = merge_ranges(range_list)
    total_ids = 0
    for r in merged:
        total_ids += r[1] - r[0] + 1


    print("Merged Ranges:", merged)
    print("Total IDs:", total_ids)
    print("Count:", count)



extract_ranges()