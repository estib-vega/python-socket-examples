class Counter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1
        return self.counter

    def decrement(self):
        self.counter -= 1
        return self.counter
    
    def set_value(self, value):
        self.counter = value
        return self.counter
    
    def reset(self):
        self.counter = 0
        return self.counter
