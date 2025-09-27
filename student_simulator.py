import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.day = 0
        self.max_days = 365

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        return f"Gladness = {self.gladness}, Progress = {round(self.progress, 2)}"

    def live(self):
        self.day += 1
        day_str = f"Day {self.day} of {self.name} life"
        print(f"{day_str:=^50}")

        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

        result = self.end_of_day()
        self.is_alive()
        return result

    def __iter__(self):
        return self

    def __next__(self):
        if not self.alive or self.day >= self.max_days:
            raise StopIteration
        return self.live()

nick = Student("Nick")

for day_result in nick:
    print(day_result)