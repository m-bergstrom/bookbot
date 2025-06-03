def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    character_counts = {}
    for character in text:
        character = character.lower()
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    
    return character_counts

def get_sorted_character_counts(character_counts):
    counts_list = []
    for character in character_counts:
        count = character_counts[character]
        counts_list.append({"char": character, "num": count})

    counts_list.sort(key=lambda count: count["num"], reverse=True)

    return counts_list
