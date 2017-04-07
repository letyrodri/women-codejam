class MinPriorityQueue():
    elements = []

    def enqueue(self, priority, element):
        self.elements.append( (priority, element) )

    def dequeue(self):
        res = min(self.elements)
        self.elements.delete(res)

        return res

    def change_priority(self, priority, element):
        for e in self.elements:
            if e[1] == element:
                to_del = e

        self.elements.remove(e)
        self.elements.append( (priority, element))
