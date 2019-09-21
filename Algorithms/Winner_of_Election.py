# code

import collections
def winner(input):
    count = collections.Counter(input)
    print(count.most_common()[0][0])


if __name__ == '__main__':
    input = ["john", "johnny", "jackie",
             "johnny", "john", "jackie",
             "jamie", "jamie", "john",
             "johnny", "jamie", "johnny",
             "john"]
    winner(input)