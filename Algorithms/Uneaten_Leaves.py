import array


def count(n, a):
    leaves = array.array('i', (0 for i in range(0, n)))
    for i in a:
        j = i - 1
        while(j < n):
            leaves[j] = 1
            j += i
    cnt = 0
    for i in range(0, n):
        if leaves[i] == 0:
            cnt += 1
        
    return cnt

if __name__ == '__main__':
    count(10, [2, 4, 5])