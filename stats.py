
def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
