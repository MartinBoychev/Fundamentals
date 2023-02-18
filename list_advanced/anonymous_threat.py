# read input
data = input().split()
commands = input().split()

# process commands
for i in range(len(commands)):
    if commands[i] == "3:1":
        break
    elif commands[i] == "merge":
        start_idx = int(commands[i+1])
        end_idx = int(commands[i+2])
        # handle out-of-bounds indices
        start_idx = max(0, start_idx)
        end_idx = min(len(data)-1, end_idx)
        # merge selected elements
        data[start_idx:end_idx+1] = [''.join(data[start_idx:end_idx+1])]
    elif commands[i] == "divide":
        idx = int(commands[i+1])
        partitions = int(commands[i+2])
        # divide selected element into partitions
        substring_len = len(data[idx]) // partitions
        extra_chars = len(data[idx]) % partitions
        result = []
        start = 0
        for j in range(partitions):
            length = substring_len
            if j < extra_chars:
                length += 1
            result.append(data[idx][start:start+length])
            start += length
        # remove original element and insert partitions
        data.pop(idx)
        data[idx:idx] = result

# print final result
print(''.join(data))
