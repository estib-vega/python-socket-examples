class Counter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1
        print('incremented to:', self.counter)
        return self.counter

    def decrement(self):
        self.counter -= 1
        print('decremented to:', self.counter)
        return self.counter
    
    def set_value(self, value):
        self.counter = value
        print('set to:', self.counter)
        return self.counter
    
    def reset(self):
        self.counter = 0
        print('reseted')
        return self.counter
