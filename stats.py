def count_words(text):
    words = text.split()
    return len(words)


def count_each_character(text):
    lower_case_text = text.lower()
    result = {}
    for character in lower_case_text:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result


def sort_on_character_count(character):
    return character["count"]


def sort_character_dictionary(character_dictionary):
    sorted_list = []
    for character in character_dictionary:
        sorted_list.append({"character": character, "count": character_dictionary[character]})
    sorted_list.sort(reverse=True, key=sort_on_character_count)
    return sorted_list