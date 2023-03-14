import random


class ListElement:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # append
    def append(self, data):
        new_elm = ListElement(data)
        if self.head is None:
            self.head = new_elm
            self.tail = new_elm
        else:
            new_elm.prev = self.tail
            self.tail.next = new_elm
            self.tail = new_elm

    # delete
    def delete_node(self, data):
        # diese Methode ermöglicht es, unter Angabe des Knotens in der Liste, ein bestimmtes Element zu löschen

        # Überprüfe, ob der Knoten, der gelöscht werden soll, der Kopf der Liste ist
        if self.head == data:
            self.head = data.next

        # Verbinde den Vorgänger-Knoten mit dem Nachfolger-Knoten
        if data.prev is not None:
            data.prev.next = data.next

        # Verbinde den Nachfolger-Knoten mit dem Vorgänger-Knoten
        if data.next is not None:
            data.next.prev = data.prev

    def delete_elm(self,data):
        # in dieser delete-methode ein gewünschtes Element gelöscht
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node == self.head and current_node == self.tail:
                    self.head = None
                    self.tail = None
                elif current_node == self.head:
                    self.head = current_node.next
                    self.head.prev = None
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    self.tail.next = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                return True
            current_node = current_node.next
        return False

    # print/display
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

    # count
    def count_elements(self):
        temp = self.head
        cnt = 0  # counter
        while temp is not None:
            cnt += 1
            temp = temp.next
        return cnt

    # get
    '''def get_from_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.value'''

    # index
    def index(self, key):
        curr = self.head
        index = 0
        while curr is not None and curr.data != key:
            curr = curr.next
            index += 1
        if curr is None:
            return -1
        else:
            return index


def main():
    listone = DoubleLinkedList()
    listtwo = DoubleLinkedList()

    listone.append(1)
    listone.append(3)
    listone.append(15)
    listone.append(7)

    for num in range(12):
        listtwo.append(random.randint(1, 100))

    listone.display()
    listtwo.display()

    node_to_delete = listone.head.next  # den zweiten Knoten löschen

    print("Index of 3 in List 1: ", listone.index(3))
    # print("Element at Index 4 in List 2: ", listtwo.get_from_index(4))
    print("Elements in List 1: ", listone.count_elements())
    print("Delete second element from List 1: ", listone.delete_node(node_to_delete))
    listone.display()
    print("Delete 15 from List 1: ", listone.delete_elm(15))
    listone.display()


if __name__ == '__main__':
    main()
