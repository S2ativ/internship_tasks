input_words = input().split()

def group(words):
    result = {}
    for word in words:
        first_letter=word[0]
        if first_letter not in result:
            result[first_letter]=[]
        result[first_letter].append(word)
    return result
print(group(input_words))


     

    