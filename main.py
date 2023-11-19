from List import List
from Matrix import Matrix

if __name__ == '__main__':
    m = Matrix()
    m.pushAfter(List(0,1))
    m.pushAfter(List(4,5))
    m.pushAfter(List(8,9))

    for i in range(10):
        for j in range(4, -1, -1):
            print(i, 4 - j - 1)

    print(m)
    print(m.reverse())
    print(m.reverse(""))
    for element in m.show_elements_per_cordonate():
        print(element)
