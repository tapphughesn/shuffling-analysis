import numpy as np

class deck(object):
    def __init__(self, n=52):
        self.n = n
        self.data = np.arange(n)
    
    def top_in_at_random(self, idx = None):
        if idx is not None:
            assert(idx >= 1)
            assert(idx <= self.n)
        if idx is None:
            idx = np.random.randint(1,self.n + 1)

        self.data = np.concatenate([
            self.data[1:idx+1],
            self.data[0:1],
            self.data[idx+1:]
        ])

d = deck(10)
print(d.data)

d.top_in_at_random(10)
print(d.data)

d.top_in_at_random(1)
print(d.data)

