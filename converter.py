# Convert from any base to decimal

# Allbases holds up to base 36
allbases = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Settings
base_from = input("BASE TO CONVERT FROM: ")
base_to = input("BASE TO CONVERT TO: ")

def run():
    # Define your options for input
    opts = allbases[0:base_from]

    # Get input
    userin = input("INPUT (BASE {}): ".format(base_from)).upper()

    # Generates an array/list/iterator for indexes in the input string
    iterator = range(len(userin))

    # Output sum
    out_sum = 0

    # Iterate over all indexes of input
    for i in iterator:

        # Because we are "big endian", we want to start from the right end of the string
        # Because len returns one more than the last index, we use (len - 1) - i
        index = len(userin) - 1 - i

        # Character of index
        ch = userin[index]

        # Verifies character is in the list
        if ch not in opts:
            print("You failed")
        else:

            # Iterate over each of the options
            for j in range(len(opts)):

                # If opt is the current option
                if opts[j] == ch:

                    # Add the index of the current option times the place value (base ^ i)
                    out_sum += j * pow(len(opts), i)
        

    # Converting from decimal to any base

    # Define your options for output
    opts = allbases[0:base_to]

    # Take input from the sum of the last converter
    userin: int = out_sum

    # Create new out string
    out_str = ""

    # Keep on running the following algorithm until 0
    while userin > 0:

        # Define the remainder when the input is divided by the base
        rem = userin % len(opts)

        # Rewrite the input as the input - remainder, which returns an even multiple of the base,
        # and deivide it by the base to go to the next place value (10 / 10 = 1, 20 / 10 = 2, gives you the tens place)
        userin = (userin - rem) // len(opts)

        # Adds to the output string the string of the remainder, which is held within opts by the index of its int value
        char = opts[rem]

        # Adds character to the string
        out_str = char + out_str


    print("RESULT: {}".format(out_str))

# Just stuff for implementing the input, not part of the actual algorithm
try:
    base_from = int(base_from)
    base_to = int(base_to)

    if base_from > 36 or base_from < 2 or base_to > 36 or base_to < 2:
        print("Valid bases are only from 2 to 36")
        exit(2)
    run()
except:
    print("This only accepts integer inputs")
