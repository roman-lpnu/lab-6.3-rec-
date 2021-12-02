import random

def create(a,low,high,i,n):
    if i<n:
        a.append(random.randint(low, high))
        create(a,low,high,i+1,n)

def num(a,i):
    if a[i] % 2 == 1:
        return min(a[i], a, 0)
    if a[i] == a[len(a) - 1]:
        return 'Немає непарних чисел'
    if i<len(a):
        return num(a,i+1)

def min(nmin,a,i):
    if i > len(a) - 1:
        return nmin
    else:
        if a[i] < nmin and a[i] % 2 == 1:
            nmin = a[i]
        return min(nmin, a, i + 1)

def main():
    a = []
    n = (int(input('n=')))
    low = (int(input('low=')))
    high = (int(input('high=')))
    create(a, low, high, 0, n)
    print(a)
    print(num(a,0))

if __name__=='__main__':
    main()
