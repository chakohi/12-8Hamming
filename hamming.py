def encode(k):

    s = "A"+"B"+k[0]+"C"+k[1:4]+"D"+k[4:]
    main = list(s)
    #A
    counter = 0
    for i in main[::2]:
        if i == "1":
            counter += 1
    if counter%2:
        main[0] = '1'
    else:
        main[0] = '0'

    #B
    counter = 0
    counterSecond = 0
    counterThird = 0
    for i in main:
        if counter%2:
            counterSecond += 1
        if counterSecond%2:
            if i == '1':
                counterThird += 1
        counter += 1

    if counterThird%2:
        main[1] = '1'
    else:
        main[1] = '0'

    #C
    counter = 0
    for i in main[3:7]:
        if i == '1':
            counter+= 1
    if main[-1] == '1':
        counter += 1
    if counter%2:
        main[3] = '1'
    else:
        main[3] = '0'

    #D
    counter = 0
    for i in main[7:]:
        if i =='1':
            counter += 1
    if counter%2:
        main[7] = '1'
    else:
        main[7] = '0'

    last = ''
    for i in main:
        last+=i

    return last

def correct(x):
    main = list(x)

    #P1
    p1 = [main[0],main[2],main[4],main[6],main[8],main[10]]
    parity1 = 0
    counter = 0
    for i in p1:
        if i == '1':
            counter += 1

    if counter%2:
        parity1 = 1

    #P2
    p2 = [main[1],main[2],main[5],main[6],main[9],main[10]]
    counter = 0
    parity2 = 0
    for i in p2:
        if i == '1':
            counter += 1
    if counter%2:
        parity2 = 1

    #P4
    p4 = [main[3],main[4],main[5],main[6],main[11]]
    counter = 0
    parity4 = 0
    for i in p4:
        if i == '1':
            counter += 1
    if counter%2:
        parity4 = 1

    #P8
    p8 = [main[7],main[8],main[9],main[10],main[11]]
    counter = 0
    parity8 = 0
    for i in p8:
        if i == '1':
            counter += 1
    if counter%2:
        parity8 = 1


    combined = str(parity1)+str(parity2)+str(parity4)+str(parity8)

    if combined != '0000':
        converted = 0
        for i in range(len(combined)):
            n = int(combined[i])*(2**i)
            converted += n

        if main[converted-1] == '0':
            main[converted-1] = '1'
        elif main[converted-1] == '1':
            main[converted-1] = '0'

    final = ''
    for i in main:
        final+=i
    return final

while True:
    inp = input("write encode for turning 8-bit binary into hamming code, correct for correcting a wrong hamming code of one error, or quit to exit:")
    if inp == 'encode':
        binary = input("what's the 8-bit binary code that you want to turn into hamming?: ")
        print(encode(binary))
    if inp == 'correct':
        hamming = input("what's the hamming code you want to correct?(1 error): ")
        print(correct(hamming))
    if inp == 'quit':
        break
