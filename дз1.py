import random


class Student:

  def __init__(self, name="Alex"):
    self.name = name
    self.money = 1000  # Initial money
    self.energy = 50  # Energy level
    self.knowledge = 0  # Knowledge level
    self.day = 1  # Current day of the year

  def study(self):
    """Method for studying: increases knowledge, but spends energy and money."""
    print(
        f"[Day {self.day}] {self.name} is studying hard... 📚 (Knowledge +15)"
    )
    self.knowledge += 15
    self.energy -= 10
    self.money -= 50

  def work(self):
    """Method for working: earns money, but spends energy."""
    print(f"[Day {self.day}] {self.name} is going to work. 💻 (Money +300)")
    self.money += 300
    self.energy -= 20

  def rest(self):
    """Method for resting: restores energy, but costs money."""
    print(f"[Day {self.day}] {self.name} is resting and having fun. 🌴 (Energy +25)")
    self.energy += 25
    self.money -= 100

  def live_day(self):
    """Student behavior logic during a single day based on their state."""
    print(
        f"\n--- Day {self.day} | Balance: {self.money} | Knowledge:"
        f" {self.knowledge} | Energy: {self.energy} ---"
    )

    # Decision-making logic
    if self.money < 200:
      self.work()
    elif self.knowledge < (self.day * 5) and self.energy > 15:
      self.study()
    elif self.energy < 25:
      self.rest()
    else:
      action = random.choice([self.study, self.work, self.rest])
      action()

    # Survival check
    if self.money < 0:
      print(f"⚠️ {self.name} went broke! Working extra shifts to survive.")
      self.money += 400

    self.day += 1

  def live_year(self):
    """Run simulation for a full year (365 days)."""
    print(
        f"=== Simulation of student life for {self.name} (1 year) has started"
        " ==="
    )

    while self.day <= 100:
      self.live_day()

    print("\n=== Year successfully completed! ===")
    print(f"Final results for {self.name}:")
    print(f"💰 Final capital: {self.money}")
    print(f"📖 Knowledge level: {self.knowledge}")
    print(f"⚡ Energy level: {self.energy}")


# Run the simulation
if __name__ == "__main__":
  student = Student("Max")
  student.live_year()