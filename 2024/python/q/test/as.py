def find_text_in_file(file_path, search_text, search_number):
    count_char = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            for position, char in enumerate(line):
                if char == search_text:
                    print(line_number-1, position)
                    count_char += 1
                    if count_char == search_number:
                        print(f"{search_number}th '{search_text}' found at line {line_number}, position {position}")
                        return line_number, position

    print(f"{search_number}th '{search_text}' not found.")
    return None


find_text_in_file('in.txt', 'H', 157)