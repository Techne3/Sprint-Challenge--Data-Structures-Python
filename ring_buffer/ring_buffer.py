from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if buffer is full and a new element is inserted, the oldest element in buffer is
        # overwritten with the newest element
        # if storage is not full, add to tail and update the current
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if storage is full, remove the head=>old, to free up space and add new item to tail => newest
        elif self.storage.length >= self.capacity:
            remove_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            # if current is at the head, set the current to tail
            if remove_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # set the start to current and append value to contents
        start = self.current
        list_buffer_contents.append(start.value)
        # loop through the nodes and append values
        # if start.next, set next_value to start next, else set next_value to storage head
        if start.next:
            next_value = start.next
        else:
            next_value = self.storage.head
        # while next_value does not equal start, append next_value value to contents
        while next_value != start:
            list_buffer_contents.append(next_value.value)
            # if next_value then set next_value to next_value next, else next_value to storage head
            if next_value.next:
                next_value = next_value.next
            else:
                next_value = self.storage.head
        # return contents
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
