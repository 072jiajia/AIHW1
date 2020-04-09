import math


class FibonacciHeapNode:
    def __init__(self, key, obj):
        self.key = key
        self.obj = obj
        self.parent = None
        self.child = None
        self.left = None
        self.right = None
        self.marked = False
        self.degree = 0

    def AddRight(self, NODE):
        if self.right is None:
            self.right = NODE
            self.left = NODE
            NODE.right = self
            NODE.left = self
        else:
            #   self <---> NODE <---> self.right
            self.right.left = NODE
            NODE.right = self.right
            self.right = NODE
            NODE.left = self

    def merge(self, NODE):
        if self.key < NODE.key:
            NODE.parent = self
            if self.child is None:
                self.child = NODE
                NODE.right = None
                NODE.left = None
            else:
                self.child.AddRight(NODE)
            self.degree += 1
            return self
        else:
            self.parent = NODE
            if NODE.child is None:
                NODE.child = self
                self.right = None
                self.left = None
            else:
                NODE.child.AddRight(self)
            NODE.degree += 1
            return NODE


class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.size = 0

    def empty(self):
        return self.min_node is None

    def Insert(self, key, obj):
        self.size += 1
        NODE = FibonacciHeapNode(key, obj)

        if self.min_node is None:
            self.min_node = NODE
        elif self.min_node.key > key:
            self.min_node.AddRight(NODE)
            self.min_node = NODE
        else:
            self.min_node.AddRight(NODE)

        return NODE

    def DecreaseKey(self, NODE, NewKey):
        NODE.key = NewKey
        if NODE.parent is not None:
            if NODE.key >= NODE.parent.key:
                return

        node = NODE
        while node.parent is not None:
            parent = node.parent
            self.__Cut__(node)
            self.min_node.AddRight(node)
            node = parent

            if parent.marked:
                parent.marked = False
            else:
                parent.marked = True
                break

        if self.min_node.key > NODE.key:
            self.min_node = NODE

    def IncreaseKey(self, NODE, NewKey):
        DELETEOBJ = NODE.obj
        self.DeleteNode(NODE)
        self.Insert(NewKey, DELETEOBJ)

    def DeleteNode(self, NODE):
        self.DecreaseKey(NODE, float('-inf'))
        self.ExtractMin()

    def ChangeKey(self, NODE, NewKey):
        if NewKey < NODE.key:
            self.DecreaseKey(NODE, NewKey)
        elif NewKey > NODE.key:
            self.IncreaseKey(NODE, NewKey)
        else:
            pass

    def __Cut__(self, NODE):
        if NODE.right is not None:
            if NODE.right == NODE.left:
                NODE.right.left = None
                NODE.right.right = None
            else:
                NODE.right.left = NODE.left
                NODE.left.right = NODE.right

        if NODE.parent.child == NODE:
            NODE.parent.child = NODE.right

        NODE.parent.degree -= 1
        NODE.parent = None

    def ExtractMin(self):
        min_obj = self.min_node.obj
        if self.size > 1:
            self.__BuildHeap__(self.__GetRootList__())
        elif self.size == 1:
            self.min_node = None
        else:
            raise RuntimeError("empty Heap (Fibonacci)")
        self.size -= 1
        return min_obj

    def __GetRootList__(self):
        List = []
        if self.min_node.right is not None:
            stop = self.min_node
            root = self.min_node.right

            while root != stop:
                List.append(root)
                root = root.right

        if self.min_node.child is not None:
            self.min_node.child.parent = None
            List.append(self.min_node.child)
            if self.min_node.child.right is not None:
                stop = self.min_node.child
                root = stop.right
                while root != stop:
                    root.parent = None
                    List.append(root)
                    root = root.right

        return List

    def __BuildHeap__(self, List):
        DEGREE = [None] * int(math.log(self.size) * 2)
        for R in List:
            while DEGREE[R.degree] is not None:
                R = R.merge(DEGREE[R.degree])
                DEGREE[R.degree - 1] = None

            DEGREE[R.degree] = R

        List = []

        for R in DEGREE:
            if R is None:
                continue
            List.append(R)

        self.min_node = List[0]

        if len(List) == 1:
            self.min_node.right = None
            self.min_node.left = None
            return

        List[-1].right = List[0]
        List[0].left = List[-1]

        for index in range(1, len(List)):
            List[index - 1].right = List[index]
            List[index].left = List[index - 1]

            if self.min_node.key > List[index].key:
                self.min_node = List[index]
