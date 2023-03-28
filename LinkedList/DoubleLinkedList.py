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
            # wenn Liste leer ist, ist das neue Element Head (+Tail)
            self.head = new_elm
            self.tail = new_elm
        else:
            # ansonsten wird das Element am Tail angehängt
            new_elm.prev = self.tail
            self.tail.next = new_elm
            self.tail = new_elm

    # delete
    def delete_node(self, data):
        # diese Methode ermöglicht es, unter Angabe des Knotens in der Liste, ein bestimmtes Element zu löschen

        # Überprüfen, ob der Knoten, der gelöscht werden soll, der Kopf der Liste ist
        if self.head == data:
            self.head = data.next

        # Vorgänger mit Nachfolger verbinden
        if data.prev is not None:
            data.prev.next = data.next

        # Nachfolger mit Vorgänger verbinden
        if data.next is not None:
            data.next.prev = data.prev

    def delete_elm(self, data):
        # in dieser delete-methode wird ein gewünschtes Element gelöscht
        if data == self.head.data:
            self.head = self.head.next
            return
        temp = self.head
        while temp.data != data:
            temp = temp.next
        temp.prev.next = temp.next

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

    # index
    def index(self, key):
        curr = self.head
        index = 0
        # List durchgehen und suchen bis gewünschtes Element gefunden
        while curr is not None and curr.data != key:
            curr = curr.next
            index += 1
        if curr is None:
            return -1
        else:
            return index

    def clear(self):
        # alle Knoten leeren
        self.tail.prev = None
        self.head.next = None
        self.tail = None
        self.head = None

    def reverse(self):
        # zweite Liste erzeugen, erste Liste von hinten durchgehen und in neue Liste einfügen
        if self.head is None:
            return
        rev_list = DoubleLinkedList()
        # temp ist self.tail, weil Liste jetzt von hinten durchgegangen wird
        temp = self.tail
        # durchgehen, solange man noch nicht vorne in der Liste angekommen ist
        while temp is not self.head:
            # Elemente der neuen Liste hinzufügen
            rev_list.append(temp)
            # um ein Element weiter vorgehen
            temp = temp.prev
        # am Schluss head hinzufügen
        rev_list.append(self.head)
        return rev_list


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
    print("Elements in List 1: ", listone.count_elements())
    print("Delete second element from List 1: ", listone.delete_node(node_to_delete))
    listone.display()
    print("Delete 15 from List 1: ", listone.delete_elm(15))
    listone.display()
    rev_list = listone.reverse()
    print("List 1 Reverse: ")
    rev_list.display()
    listtwo.clear()
    listtwo.display()


if __name__ == '__main__':
    main()
