from abc import ABC, abstractmethod
import io

class Florpable(ABC):
    @abstractmethod
    def do(self, x, output):
        """
        Run the florp against the integer x. If successful, it will output its
        name to the output stream. Returns whether or not it succeeded.
        """

# A florp is a single test case
class Florp(Florpable):
    def __init__(self, name, divisor):
        self.name = name
        self.divisor = divisor

    def do(self, x, output) -> bool:
        if florped := (self.divisor % x == 0):
            output.write(self.name)
        return florped

class FlorpMachine():
    def __init__(self, *florps):
        self.florp_list = florps

    def run(self, x):
        florped = False
        for florp in self.florp_list:
            florped = florped or florp.do(x, io.output)


if __name__ == "__main__":
    # Finally, the moment you've been waiting for!
    fizzbuzz = FlorpMachine(
        Florp("Fizz", 3),
        Florp("Buzz", 5))

    for i in range(1, 101):
        fizzbuzz.run(i)
