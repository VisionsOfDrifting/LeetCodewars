def get_spaces(row, desc, k):
    max_spaces = (k - 1) * 2 - 1
    if desc:
        spaces = max_spaces - row * 2
    else:
        spaces = max_spaces - (k - 1 - row) * 2
    return spaces


def is_descending(index, k):
    # Check whether the index is more or less than halfway
    # through its oscillation back to the starting point
    return index % (2 * (k - 1)) < k - 1


def zigzag(sentence, k):
    n = len(sentence)

    for row in range(k):
        i = row
        line = [" " for _ in range(n)]

        while i < n:
            # print(line)
            line[i] = sentence[i]
            desc = is_descending(i, k)
            spaces = get_spaces(row, desc, k)
            i += spaces + 1

        # print(line)
        print("".join(line))

input_string = "thisisazigzag"
k = 4
zigzag(input_string, k)
print()
input_string = "thisisanotherzigzag"
k = 5
zigzag(input_string, k)
