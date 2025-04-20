def count_words(text):
    return len(text.split())

def count_char_occurrence(text):
    char_stats = {}
    for char in text.lower():
        if char not in char_stats:
            char_stats[char] = 1
        else:
            char_stats[char] +=1
    return char_stats

def dict_to_sorted_list(dictChar):
    sorted_list = []
    for char in dictChar:
        if char.isalpha():
            sorted_list.append(dict({char: dictChar[char]}))
    sorted_list = sorted(sorted_list, key=lambda x :x[[*x][0]], reverse=True)
    return sorted_list
