# Fizz Buzz Program
class FizzBuzz:
    def __init__(self, limit):
        self.limit = limit

    def run(self):
        for i in range(1, self.limit + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)


# Example
obj = FizzBuzz(100)
obj.run()