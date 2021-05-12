def isValid(a):
    count = 0
    for i in range(len(a)):
        if a[i] == '(':
            count += 1
        elif a[i] == ')':
            count -= 1
            if count < 0:
                return False
    return True


if __name__ == "__main__":
    print(isValid('(a)'))
