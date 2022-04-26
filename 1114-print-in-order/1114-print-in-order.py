class Foo:
    def __init__(self):
        self.f, self.s = False, False
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        i = 0
        while not self.f:
            i += 1  
        printSecond()
        self.s = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        i = 0
        while not self.s:
            i += 1
        printThird()