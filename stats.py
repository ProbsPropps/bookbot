def count_words(text):
    new_array = text.split()
    num_words = len(new_array)
    return num_words

def count_characters(text):
    char_dict = {}
    text_lower = text.lower()
    for t in text_lower:
        char_dict[t] = 0
    for t in text_lower:
        char_dict[t] += 1
    return char_dict

def sort_on(char_dict):
    return char_dict["num"]

def sorted_count(char_dict):
    sorted_list = []
    for c, n in char_dict.items():
        sorted_list.append({"char": c, "num": n})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list