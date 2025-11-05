def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    norm_text = text.lower()
    char_count = {}
    for ch in norm_text:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return char_count


def dict_list(text):
    # Set a value for the dictionary
    counts = get_char_count(text)
    
    result = []
    for ch, num in counts.items():
        if ch.isalpha():
            result.append({"char": ch, "num": num})
    
    # This is a sort helper
    def sort_on(item):
        return item["num"]
    
    result.sort(key=sort_on, reverse=True)
    return result


