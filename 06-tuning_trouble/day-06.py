def find_marker(buffer: str, window_size: int) -> int:
    for x in range(len(buffer) - window_size):
        window = set(buffer[x:x+window_size])
        if len(window) == window_size:
            return x+window_size
    return None


if __name__ == '__main__':
    with open('input.txt') as file:
        data_buffer = file.read()

    # Part 1
    print(f"The start marker is at: {find_marker(data_buffer, 4)}")

    # Part 2
    print(f"The first message marker is at: {find_marker(data_buffer, 14)}")
