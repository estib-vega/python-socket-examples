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
        # value must be int
        try:
            self.counter = int(value)
            print('set to:', self.counter)
            return self.counter
        except:
            print('could not set value')
            return '---set_value() param must be an int'  
    
    def reset(self):
        self.counter = 0
        print('reseted')
        return self.counter

    def exponentialize(self):
        self.counter *= self.counter
        print('exponentialized')
        return self.counter
