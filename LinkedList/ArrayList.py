import random


class ArrayList:
    def __init__(self):
        # Startkapazität der Liste
        self.capacity = 4
        # Anzahl der Elemente in der Liste
        self.size = 0
        # Liste, die die Elemente enthält
        self.data = [] * self.capacity

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        # Gib Element an der angegebenen Position zurück
        return self.data[index]

    def length(self):
        # Gebe die Anzahl der Elemente in der Liste zurück
        return self.size

    def count(self, element):
        # count()-Methode der Python-Liste, um Anzahl eines Elements zu zählen
        return self.data.count(element)

    def append(self, element):
        # append()-Methode der Python-Liste, um das Element am Ende hinzuzufügen
        self.data.append(element)
        # Erhöhe die Anzahl der Elemente um 1
        self.size += 1

    def insert(self, index, element):
        # insert()-Methode der Python-Liste, um das Element an der angegebenen Position einzufügen
        self.data.insert(index, element)
        # Erhöhe die Anzahl der Elemente um 1
        self.size += 1

    def remove(self, element):
        # remove()-Methode der Python-Liste, um das erste Vorkommen des Elements zu entfernen
        self.data.remove(element)
        # Verringere die Anzahl der Elemente um 1
        self.size -= 1

    def pop(self, index=None):
        # pop()-Methode der Python-Liste, um das Element an der angegebenen Position zu entfernen
        # oder das letzte Element, wenn keine Position angegeben ist
        if index is None:
            index = -1
        element = self.data.pop(index)
        # Verringere die Anzahl der Elemente um 1
        self.size -= 1
        # Entferntes Element zurückgeben
        return element

    def __str__(self):
        return "[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]"


def main():
    # Erstelle eine neue leere MyArrayList
    firstlist = ArrayList()
    my_list = ArrayList()

    # Füge Elemente hinzu
    my_list.append(42)
    my_list.append("Hallo")
    my_list.append([1, 2, 3])

    for num in range(12):
        firstlist.append(random.randint(1, 100))

    # Gib die Elemente der Liste aus
    print(my_list)
    print(firstlist)

    firstlist.pop()
    my_list.pop(1)
    print("Vorkommen 42 in my_list: ")
    my_list.count(42)

    firstlist.count(firstlist)
    my_list.count(my_list)

    firstlist.insert(5, 123)

    print("First List nach insert von 123 am Index 5: ", firstlist)

    print("FirstList am Index 5: ", firstlist.get(5))
    print("Länge FirstList: ", firstlist.length())

    my_list.insert(0, 77)

    print(my_list)
    print(firstlist)


if __name__ == "__main__":
    main()
