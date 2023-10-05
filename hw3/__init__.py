import random


def get_first_value():
    value = random.choice(["o", "x"])
    return value


class Place:
    def __init__(self):
        self.place = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]]

    def print_place(self):
        for i in self.place:
            print(i)

    def get_place(self):
        return self.place

    def change_place(self, position, value):
        if position <= 3:
            self.place[0][position - 1] = value
        elif position <= 6:
            self.place[1][position - 4] = value
        elif position <= 9:
            self.place[2][position - 7] = value

    def check_place(self, position):
        if position <= 3:
            if self.place[0][position - 1] == "-":
                return True
        elif position <= 6:
            if self.place[1][position - 4] == "-":
                return True
        elif position <= 9:
            if self.place[2][position - 7] == "-":
                return True
        return False

    def check_win(self, value):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.place[i][j] == value:
                    count += 1
                    if count == 3:
                        return True
                else:
                    count = 0
        if (self.place[0][0] == value) and (self.place[1][1] == value) and (self.place[2][2] == value):
            return True
        if (self.place[0][2] == value) and (self.place[1][1] == value) and (self.place[2][0] == value):
            return True
        if (self.place[0][0] == value) and (self.place[1][0] == value) and (self.place[2][0] == value):
            return True
        if (self.place[0][1] == value) and (self.place[1][1] == value) and (self.place[2][1] == value):
            return True
        if (self.place[0][2] == value) and (self.place[1][2] == value) and (self.place[2][2] == value):
            return True


class Game(Place):
    def game(self):
        count = 0
        p = Place()
        first = get_first_value()
        while count < 9:
            if first == "x":
                if count % 2 == 0:
                    game_value = "x"
                if count % 2 != 0:
                    game_value = "o"
            else:
                if count % 2 == 0:
                    game_value = "o"
                if count % 2 != 0:
                    game_value = "x"
            print(f"{game_value} move")
            position = int(input("Input position - "))
            if p.check_place(position):
                p.change_place(position, game_value)
                p.print_place()
                count += 1
                if p.check_win(game_value):
                    print(f"{game_value} is win")
                    break
            else:
                print("This position is filled")


start = Game()
start.game()
