class List:
    def __init__(self, *elements):
        self.len = 0
        self.head = None
        for element in elements:
            self.pushAfter(element)

    def is_empty(self):
        return self.len < 1

    def last_current(self):
        return self.len - 1

    def __len__(self):
        return self.len

    def __str__(self):
        return "[" + ", ".join(str(element) for element in self) + "]"

    def _iter_node(self):
        if not self.is_empty():
            current = self.head.next
            while True:
                yield current
                if current == self.head:
                    break
                current = current.next

    def __iter__(self):
        for element in self._iter_node():
            yield element.content

    def _reversed_node(self):
        if not self.is_empty():
            current = self.head
            while True:
                yield current
                if current == self.head.next:
                    break
                current = current.previous

    def __reversed__(self):
        for element in self._reversed_node():
            yield element.content

    def _get_node(self, current):
        if (current > len(self) - 1):
            return self.head
        else:
            if self.last_current() // 2 < current:
                direction = self._reversed_node()
                current = self.last_current() - current
            else:
                direction = self._iter_node()

            tmp_current = 0
            for position in direction:
                if tmp_current == current:
                    return position
                tmp_current += 1

    def __iadd__(self, itemList):
        if isinstance(itemList, List):
            for element in itemList:
                self.pushAfter(element)
        else:
            raise NotImplementedError
        return self

    def __add__(self, itemList):
        if isinstance(itemList, List):
            tmp = self.copy()
            tmp += itemList
            return tmp
        else:
            raise NotImplementedError

    def __getitem__(self, current):  # operateur []
        if (current > len(self) - 1) or (current < 0):
            return None
        else:
            return self._get_node(current).content

    def __setitem__(self, current, item):
        target = self._get_node(current)
        target.changeContent(item)

    def insert(self, current, item):
        if current == 0:
            self.pushBefore(item)
        elif current > len(self) - 1:
            self.pushAfter(item)
        else:
            tmp = Node(item)
            old_node = self._get_node(current)
            old_node.previous.addNext(tmp)
            tmp.addPrevious(old_node.previous)
            tmp.addNext(old_node)
            old_node.previous = tmp
            self.len += 1

    def pushAfter(self, element):
        tmp = Node(element)
        if self.head is None:
            self.head = tmp
            self.head.addNext(tmp)
            self.head.addPrevious(tmp)
        else:
            tmp.addNext(self.head.next)
            self.head.next.addPrevious(tmp)
            self.head.next = tmp
            tmp.addPrevious(self.head)
            self.head = tmp
        self.len += 1

    def pushBefore(self, element):
        if self.head is None:
            self.pushAfter(element)
        else:
            tmp = Node(element)
            tmp.addPrevious(self.head)
            tmp.addNext(self.head.next)
            self.head.next.addPrevious(tmp)
            self.head.next = tmp
            self.len += 1

    def pop(self, current=None):
        if not current is None and not isinstance(current, int):
            raise Exception("Just interger it's accepted.")
        if self.head is not None:
            if (current is None) or (current >= len(self)-1):
                tmp = self.head
            else:
                tmp = self._get_node(current)
            self._remove(tmp)
            return tmp.content
        raise Exception("Lenght is 0 and your head is None. List empty.")


    def _remove(self, node):
        node.previous.addNext(node.next)
        node.next.addPrevious(node.previous)
        if self.head == node:
            self.head = node.previous
        self.len -= 1
        if len(self) == 0:
            self.head = None

    def clear(self):
        self.head = None
        self.len = 0

    def copy(self):
        tmp = List()
        for element in self:
            tmp.pushAfter(element)
        return tmp

    def reverse(self):
        tmp = List()
        for element in reversed(self):
            tmp.pushAfter(element)
        return tmp


class Node:
    def __init__(self, element):
        self.previous = None
        self.content = element
        self.next = None
    
    def addPrevious(self, prv):
        self.previous = prv

    def addNext(self, nxt):
        self.next = nxt

    def changeContent(self, element):
        self.content = element
