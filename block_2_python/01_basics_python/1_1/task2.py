def get_unic_word(text):
    text = text.upper()
    word = text.split()
    unic_word = []

    for i in word:
        if i not in unic_word:
            unic_word.append(i)

    n = len(unic_word)
    for a in range(n):
        for b in range(0,n-a-1):
            if unic_word[b] > unic_word[b+1]:
                unic_word[b], unic_word[b+1] = unic_word[b+1], unic_word[b]

    return(unic_word)

stroka = 'пайтон Пайтон ПАЙТОН питон а б ш в я якорь апельсин'

print(get_unic_word(stroka))