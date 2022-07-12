
def bigger_is_greater(w):
    length = len(w)
    char_list = list(w)

    index = length - 2
    while index >= 0 and char_list[index] >= char_list[index + 1]:
        index -= 1

    if index < 0:
        return "no answer"
    else:
        last_letter = length - 1
        while last_letter >= index and char_list[last_letter] <= char_list[index]:
            last_letter -= 1

        char_list[index], char_list[last_letter] = char_list[last_letter], char_list[index]
    if ''.join(char_list) == w or len(w) == 1:
        return "no answer"
    else:
        answer = ''.join(char_list)
        return answer[:index + 1] + answer[index + 1:][::-1]