
from secrets import randbelow

class Node:

    def __init__(self, value: any, next_element):

        # Value stored in the node
        self.value: any = value

        # next element in the list
        self.nextElement: Node = next_element


class List:

    def __init__(self):

        # How many elements are stored in the list
        self.length: int = 0

        # Start of the linked list
        self.root: Node = None

        # Tail of the linked list
        self.tail: Node = None

    def __get_node(self, index: int) -> Node:
        
        """
        Private function for returning the node at
        a specific index in the list
        Returns a Node or None.
        """

        current: Node = self.root

        if index >= self.length:
            
            return None
        
        for _ in range(0, index):

            current = current.nextElement

        return current

    def add(self, value: any):

        """
        Add a value to the end of the list.
        returns nothing.
        """

        # if the list is empty add the first element

        if self.root is None:

            self.root = Node(value, None)

            self.tail = self.root

            self.length += 1

            return

        # list has at least one element

        new_addition: Node = Node(value, None)

        self.tail.nextElement = new_addition

        self.tail = new_addition

        self.length += 1

    def get_value(self, index: int) -> any:
        
        """
        Retrieve the value in the node at a specified
        index.
        Returns the value stored in that node.
        """

        # Retrieve the node at the specified index
        current: Node = self.__get_node(index)

        if current is None:

            return None

        # Return the value stored in the current node
        return current.value

    def set_value(self, index: int, value: any):

        """
        Set the value in the node at the specified index.
        Returns nothing.
        """

        # Retrieve the node at the specified index
        current: Node = self.__get_node(index)

        if current is None:
            return

        # set the new value
        current.value = value

    def clone(self):

        """
        Duplicates the current list and returns
        the newly created duplicate
        """

        list_clone: List = List()

        current: Node = self.root

        if (current is None):
            
            return list_clone

        for _ in range(0, self.length):

            list_clone.add(current.value)

            current = current.nextElement

        return list_clone

    def shuffle(self):
        
        """
        Randomizes the order of the list using secrets.randbelow
        """

        list_length: int = self.length

        for index in range(0, list_length):

            # Find a random integer between 0 and length - 1
            randint : int = randbelow(self.length)

            # Get a node at the random index and one at our current
            # itteration index
            random_node: Node = self.__get_node(randint)

            current_node: Node = self.__get_node(index)

            # Make sure that __get_node() didn't have
            # Any issues
            if (random_node is None or current_node is None):

                return

            # Swap the value in current_node and random_node
            temp_value: any = current_node.value

            current_node.value = random_node.value

            random_node.value = temp_value

    def contains(self, value: any) -> bool:

        """
        Checks to see if the element passed is in the list.
        Returns True if it exists, False otherwise.
        """

        current: Node = self.root

        for _ in range(0, self.length):

            if current.value == value:

                return True

            current = current.nextElement

        return False

    def remove_at(self, index: int):

        """
        Removes the Node at a specified index.
        Returns nothing.
        """

        # out of bounds
        if index >= self.length:

            return

        if index == 0:

            self.root = self.root.nextElement

            self.length -= 1

            return

        current: Node = self.__get_node(index - 1)

        if current is None:

            return

        # Skip over current
        current.nextElement = current.nextElement.nextElement

        self.length -= 1

        return

    def remove_value(self, value: any):
        
        """
        Removes the first Node in the list containing
        the passed value
        """

        # current for iteration through the list
        current: Node = self.root

        # previous for deletion of current from the list
        previous: Node = None

        for _ in range(0, self.length):

            # Found the element to remove
            if current.value == value:

                # Removing the first element in the list
                if (previous == None):
                    
                    # remove the first element in the list
                    self.root = self.root.nextElement

                #Removing an element other than the first one
                else:

                    # jump over current
                    previous.nextElement = current.nextElement

                # decrement the list length
                self.length -= 1

                # Value found and removed. All done here.
                break
            
            # not an equal element, moving on the the next element
            previous = current
            
            current = current.nextElement

    def __str__(self) -> str:

        current: Node = self.root

        if current is None:
            return ""

        string_to_build: str = ""

        for i in range(0, self.length):

            string_to_build += current.value

            if i < self.length - 1:

                string_to_build += ", "

            current = current.nextElement

        return string_to_build
