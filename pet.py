import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        """
        Reduces hunger by 3, but never lets it go below 0.
        Increases happiness by 1 but doesn't go beyond 10.
        """
        if self.hunger >= 3:
            self.hunger -= 3
        else:
            self.hunger = 0
        self.happiness = min(self.happiness + 1, 10)
        time.sleep(2)
        print(f"{self.name} has eaten🎉.")
        time.sleep(1)

    def sleep(self):
        """Increases energy by 5 but doesn't go beyond 10."""
        self.energy = min(self.energy + 5, 10)
        time.sleep(1)
        print(f"{self.name} has slept💤💤.")

    def play(self):
        """Decreases energy by 2 and increases happiness by 2."""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print("You played with your pet.")
        else:
            print(f"{self.name} is too tired to play😔.")

    def get_status(self):
        """Prints the current status of the pet."""
        print(f"\n{self.name}'s current status: \n🍚 Hunger: {self.hunger}\n⚡ Energy: {self.energy}\n🐱 Happiness: {self.happiness}\n🎃 Tricks: {', '.join(self.tricks) if self.tricks else f'{self.name} doesn\'t know any tricks yet.'}")
        time.sleep(2)

    def train(self, trick):
        """Teach the pet a new trick."""
        if trick in self.tricks:
            print(f"{self.name} already knows '{trick}'.")
        else:
            self.tricks.append(trick)
            print(f"\nSuccessfully taught {self.name} the trick '{trick}🎉'!")
            time.sleep(2)

    def show_tricks(self):
        """Show the pet's tricks."""
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet😔.")
        else:
            print(f"\n{self.name}'s tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. 🎃 {trick}")