import random


# class ListElement --> verweist auf Inhalt und Nachfolger des jeweiligen Elements
class ListElement:
    def __init__(self, data):
        self.data = data
        self.next = None


# eigentliche Listenimplementierung mit Kopf
class LinkedList:
    def __init__(self):
        self.head = None

    # add a new element to the end of the list
    def append(self, data):
        new_lem = ListElement(data)
        # checks whether there is already an element in the list
        if self.head is None:
            self.head = new_lem
            return
        # if there are already elements in the list, an entry point has to be determined
        # new ListElement is appended after the last existing element
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_lem

    # add a new element in the beginning of the list
    def prepend(self, data):
        new_lem = ListElement(data)
        new_lem.next = self.head
        self.head = new_lem

    # first element with a specific key should be deleted
    def delete_element(self, key):
        # list could be empty
        if self.head is None:
            return
        # remove head element incase key equals head element
        if self.head.data == key:
            self.head = self.head.next
            return
        # remove another element
        temp = self.head
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    # count amount of elements
    def count_elements(self):
        temp = self.head
        cnt = 0  # counter
        while temp is not None:
            cnt += 1
            temp = temp.next
        return cnt

    # get index of a specific element
    def index(self, element):
        temp = self.head
        index = 0
        while temp:
            if temp.data == element:
                return index
            temp = temp.next
            index += 1
        # if element is not in List --> return -1
        return -1

    # prints list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    # sort List
    def sort(self):
        # check, whether list is empty
        if self.head is None:
            return

        temp = self.head
        while temp.next:
            if temp.data > temp.next.data:
                # if current element is greater than the next element they are swapped
                temp.data, temp.next.data = temp.next.data, temp.data
                # start again at the beginning of the list
                temp = self.head
            else:
                temp = temp.next


# fill and print List
def main():
    firstlist = LinkedList()
    secondlist = LinkedList()

    secondlist.append(1)
    secondlist.append(2)
    secondlist.append(3)

    for num in range(12):
        firstlist.append(random.randint(1, 100))

    firstlist.print_list()
    firstlist.sort()
    print("Liste wurde sortiert, sie sieht jetzt folgendermaßen aus: ")
    firstlist.print_list()
    print("Length of List: ", firstlist.count_elements())

    print('###########################################################')
    secondlist.print_list()
    print("Index: ", secondlist.index(4))
    secondlist.delete_element(1)
    secondlist.print_list()


if __name__ == "__main__":
    main()
