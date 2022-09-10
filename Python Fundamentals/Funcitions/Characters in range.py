start = input()
end = input()


def characters(first,second):
    symbol = ""
    for i in range(ord(start)+1,ord(end)):
        symbol += chr(i)+" "
    return symbol


print(characters(start,end))

