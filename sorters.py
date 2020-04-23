class BaseSorter:

    def __init__(self, data):
        self.data = data


class BubbleSorter(BaseSorter):

    def __iter__(self):
        for _ in self.data:
            for ix, x in enumerate(self.data[:-1]):
                if self.data[ix + 1] < x:
                    self.data[ix], self.data[ix + 1] = self.data[ix + 1], self.data[ix]

                yield self.data, [ix]


class ElijahSorter(BaseSorter):

    @staticmethod
    def max_and_ix(list):
        current_max = list[0]
        current_ix = 0
        for ix, elem in enumerate(list):
            if elem > current_max:
                current_max = elem
                current_ix = ix

        return current_max, current_ix

    def __iter__(self):
        for ix, x in enumerate(self.data):
            if ix+1 == len(self.data):
                break
            biggest, max_ix = self.max_and_ix(self.data[:-ix-1])
            self.data.insert(-ix-1, biggest)
            self.data.remove(biggest)
            
            yield self.data, [len(self.data)-ix-2]

