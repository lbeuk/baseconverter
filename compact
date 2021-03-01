allbases = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
base_from = input("BASE TO CONVERT FROM: ")
base_to = input("BASE TO CONVERT TO: ")
def run():
    opts = allbases[0:base_from]
    userin = input("INPUT (BASE {}): ".format(base_from)).upper()
    iterator = range(len(userin))
    out_sum = 0
    for i in iterator:
        index = len(userin) - 1 - i
        ch = userin[index]
        if ch not in opts:
            print("You failed")
        else:
            for j in range(len(opts)):
                if opts[j] == ch:
                    out_sum += j * pow(len(opts), i)
    opts = allbases[0:base_to]
    userin: int = out_sum
    out_str = ""
    while userin > 0:
        rem = userin % len(opts)
        userin = (userin - rem) // len(opts)
        char = opts[rem]
        out_str = char + out_str
    print("RESULT: {}".format(out_str))
try:
    base_from = int(base_from)
    base_to = int(base_to)
    if base_from > 36 or base_from < 2 or base_to > 36 or base_to < 2:
        print("Valid bases are only from 2 to 36")
        exit(2)
    run()
except:
    print("This only accepts integer inputs")
