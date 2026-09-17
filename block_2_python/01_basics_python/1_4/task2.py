input_words = input()
def checker(words):
    dict_symbol={}
    for one in words:
        if one not in dict_symbol:
            dict_symbol[one]= 1
        else:    
            dict_symbol[one] += 1
    return dict_symbol
print(checker(input_words))
