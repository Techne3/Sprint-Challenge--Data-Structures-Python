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
        # if storage is full, remove the head=>old, to free up space
        # and add new item to tail => newest
        elif self.storage.length == self.capacity:
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
        # if start.next, set current_node to start next, else set current_node to storage head
        if start.next:
            current_node = start.next
        else:
            current_node = self.storage.head
        # while current_node does not equal start, append current_node value to contents
        while current_node != start:
            list_buffer_contents.append(current_node.value)
            # if current_node then set current_node to current_node next, else current_node to storage head
            if current_node.next:
                current_node = current_node.next
            else:
                current_node = self.storage.head
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
