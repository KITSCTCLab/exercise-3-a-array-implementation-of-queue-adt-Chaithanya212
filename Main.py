class Solution:

    """This class implements linear queue.

      Attributes:

          stack: A list which maintains the content of stack.

          queue: A list which maintains the content of queue.

          top: An integer which denotes the index of the element at the top of the stack.

          front: An integer which denotes the index of the element at the front of the queue.

          rear: An integer which denotes the index of the element at the rear of the queue.

          size: An integer which represents the size of stack and queue.

      """


    # Write your code here

    def init(self, size):

       

        """Inits Solution with stack, queue, size, top, front and rear.

        Arguments:

          size: An integer to set the size of stack and queue.

        """

        self.stack = [None]*size

        self.queue = [None]*size

        self.size = size

        self.top = -1

        self.rear = -1

        self.front = -1


    def is_stack_empty(self):

        """

        Check whether the stack is empty.

        Returns:

          True if it is empty, else returns False.

        """

       

        return self.top==-1


    def is_queue_empty(self):

        """

        Check whether the queue is empty.

        Returns:

          True if it is empty, else returns False.

        """

        return self.rear<self.front


    def is_stack_full(self):

        """

        Check whether the stack is full.

        Returns:

          True if it is full, else returns False.

        """

        return self.top==(self.size-1)
