def palindrom(text):
    clean_text = ""
    text = text.lower()

    for i in text:
        if i.isalpha():
            clean_text += i

    return clean_text == clean_text[::-1]


test_text1 = "А роза /упала на ла.пу Азора"
# test_text2 ='Не падала роза'

print(palindrom(test_text1))
# print(palindrom(test_text2))
