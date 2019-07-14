class Sort(object):
    def __init__(self):
        pass

    def implement_quick_sort(self, A):
        return self._quick_sort(A, 0, len(A)-1)

    def implement_merge_sort(self, A):
        return self._merge_sort(A)

    def _quick_sort(self, A, lo, hi):
        if lo < hi:
            q = self._partition(A, lo, hi)
            self._quick_sort(A, lo, q - 1)
            self._quick_sort(A, q + 1, hi)
        return A

    def _partition(self, A, lo, hi):
        pivot = A[hi]
        i = lo
        for j in range(lo,hi):
            if A[j]< pivot:
                A[i], A[j] = A[j],A[i]
                i += 1
        A[i], A[hi] = A[hi],A[i]
        return i

    def _merge_sort(self):
        #a:list
        if len(self.a) < 1:
            return self.a
        a1 = a[:len(self.a)//2]
        a2 = a[len(self.a)//2:]
        a1 = self._merge_sort(a1)
        a2 = self._merge_sort(a2)
        return self._merge_two_sorted_array(a1, a2)

    def _merge_two_sorted_array(self, a1, a2):
        p, q = 0, 0
        res = []
        while p < len(a1) and q < len(a2):
            if a1[p] < a2[q]:
                res.append(a1[p])
                p+=1
            else:
                res.append(a2[q])
                q+=1
        if p<len(a1):
            res += a1[p:]
        if q<len(a2):
            res += a2[q:]
        return res

if __name__== '__main__':
    a= Sort()
    print(a.implement_quick_sort([]))
    print(a.implement_quick_sort([1,1]))
    print(a.implement_quick_sort([100,1,2,3,-10000,1.1]))