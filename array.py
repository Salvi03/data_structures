class Array:
    def __init__(self, length):
        self.value = None
        if length:
            self.next = Array(length-1)

    def set_value(self, pos, value):
        if not pos:
            self.value = value
            return value

        return self.next.set_value(pos-1, value)

    def get_value(self, pos):
        if not pos:
            return self.value

        return self.next.get_value(pos-1)


if __name__ == "__main__":
    array = Array(5)
    array1 = Array(2)

    array.set_value(0, array1)
    array1.set_value(0, 6)

    array2 = array.get_value(0)
    array2.set_value(0, 98)

    print(array.get_value(0).get_value(0))

    """
    array.set_value(2, 56)
    array.set_value(0, 2)
    print(f"{ array.get_value(0) } { array.get_value(2) }")
    """
