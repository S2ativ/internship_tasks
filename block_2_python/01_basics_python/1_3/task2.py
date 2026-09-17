data = input()
data = data.split()
def preobraz(dataa):
    if len(dataa) == 0:
        return []
    elif len(dataa) == 1:
        return ['SINGLE']
    else :
        dataa = ['START'] + dataa[1:-1] + ['END']
        return dataa
print(preobraz(data))
