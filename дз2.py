import random


class Pet:

  def __init__(self, name="Barsik"):
    self.name = name
    self.hunger = 50  # Pet hunger level
    self.happiness = 50  # Pet happiness level

  def eat(self):
    """The pet eats, decreasing its hunger level."""
    self.hunger -= 20
    if self.hunger < 0:
      self.hunger = 0
    print(f"🐾 Pet {self.name} is eating food. 🍖 (Hunger: {self.hunger})")

  def play(self):
    """The pet plays, increasing its happiness level."""
    self.happiness += 20
    print(
        f"🐾 Pet {self.name} is playing happily! 🎾 (Happiness:"
        f" {self.happiness})"
    )


class Student:

  def __init__(self, name="Alex", pet_name="Barsik"):
    self.name = name
    self.money = 1200  # Initial money
    self.energy = 60  # Energy level
    self.knowledge = 0  # Knowledge level
    self.pet = Pet(pet_name)  # Composition: Student has a Pet
    self.day = 1

  def study(self):
    print(f"[Day {self.day}] {self.name} is studying hard. 📚 (Knowledge +15)")
    self.knowledge += 15
    self.energy -= 15
    self.money -= 50

  def work(self):
    print(
        f"[Day {self.day}] {self.name} is working at a part-time job. 💻 (Money"
        " +350)"
    )
    self.money += 350
    self.energy -= 25

  def feed_pet(self):
    """Student spends money and feeds the pet."""
    print(
        f"[Day {self.day}] {self.name} is buying food and feeding"
        f" {self.pet.name}."
    )
    self.money -= 70
    self.pet.eat()

  def play_with_pet(self):
    """Student plays with the pet, spending energy, but boosting happiness."""
    print(f"[Day {self.day}] {self.name} is playing with {self.pet.name}. ❤️")
    self.energy -= 10
    self.pet.play()

  def rest(self):
    print(f"[Day {self.day}] {self.name} is resting and sleeping. 🌴 (Energy +30)")
    self.energy += 30
    self.money -= 80

  def live_day(self):
    print(
        f"\n--- Day {self.day} | {self.name}: Money={self.money},"
        f" Energy={self.energy}, Knowledge={self.knowledge} ---"
    )

    # Interaction logic between student and pet
    if self.money < 250:
      self.work()
    elif self.pet.hunger > 60:
      self.feed_pet()
    elif self.pet.happiness < 40:
      self.play_with_pet()
    elif self.knowledge < (self.day * 6) and self.energy > 20:
      self.study()
    elif self.energy < 30:
      self.rest()
    else:
      action = random.choice([self.study, self.work, self.play_with_pet])
      action()

    # Survival check
    if self.money < 0:
      print(f"⚠️ {self.name} is out of cash! Taking emergency night shifts.")
      self.money += 500

    self.day += 1

  def live_year(self):
    print(
        f"=== Simulation of {self.name} and his pet {self.pet.name} has started"
        " ==="
    )
    while self.day <= 365:
      self.live_day()

    print("\n=== Year successfully completed! ===")
    print(f"Final stats for {self.name}:")
    print(f"💰 Money: {self.money}")
    print(f"📖 Knowledge: {self.knowledge}")
    print(f"🐾 Pet {self.pet.name} status: Happiness={self.pet.happiness}")


if __name__ == "__main__":
  student = Student("Max", "Tom")
  student.live_year()


