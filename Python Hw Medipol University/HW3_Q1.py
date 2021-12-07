"""
Author: Atahan Koc
Description Part: In this program, a program was written that we were asked to find the common substr dec between two X and Y strings. Our program is written in a case-sensitive way.
It was successfully printed out.
"""

def common_substrings(X, Y):
    subs = []
    # case-insensitive
    X = X.lower()
    Y = Y.lower()

    for i in range(len(X)):
        for j in range(i, len(X)):
            sub = X[i:j + 1]
            # if sub is in Y and not added before, adding to sub
            if sub in Y and sub not in subs:
                subs.append(sub)
    return subs

def main():
    # user input for strings X and Y
    X = input('Enter the X : ')
    Y = input('Enter the Y : ')

    # call common_substrings function and store in list
    c_subs = common_substrings(X, Y)

    # print the length of common substring and substrings
    print('{} Common Substrings are : '.format(len(c_subs)))
    print(c_subs)

# main function
if __name__ == "__main__":
    main()