#TicTacToe
import random
class Game:
    def __init__(self):
        self.cpu_sign = None
        self.winner = None
        self.count = 1
        self.game_array = ["-","-","-","-","-","-","-","-","-"]
        self.cpu_array = []
        self.user_array = []
        self.winning_array = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.user_sign=None
        #self.game_array = [1,2,3,4,5,6,7,8,9]
    def display(self):
        for i in range(3):
            self._display(i)

    def _display(self,n):
        print(self.game_array[3*n],end="")
        print("|",end="")
        print(self.game_array[3*n+1],end="")
        print("|",end="")
        print(self.game_array[3*n+2])
        if n < 2:
            print("-----")

    def user_play(self):
        print("Turn No. : %d" % self.count)
        print("Please tell the position where you want to insert your sign.")
        user_input = int(input())
        if self.game_array[user_input-1] == "-":
            self.user_array.append(user_input)
            self.game_array[user_input-1] = self.user_sign
            self.display()
            self.count += 1
        else:
            print("User please enter a valid \\ unoccupied position")
            self.user_play()

        c = 0
        for i in self.game_array:
            if i == '-':
                c += 1
        if c == 0:
            self.winner = "No One"

        for i in self.winning_array:
            counting = 0
            for j in i:
                if self.game_array[j - 1] == self.user_sign:
                    counting += 1
            if counting == 3:
                self.winner == "User"

    def cpu_play(self):
        print("Turn No. : %d" % self.count)
        print("Cpu makes its move")
        if self.user_sign == "X":
            self.cpu_sign = "O"
        else:
            self.cpu_sign = "X"

        if self.count <= 2:
            x = random.randint(0,8)
            while self.game_array[x] != "-":
                x = random.randint(0,8)
            self.game_array[x] = self.cpu_sign
            self.cpu_array.append(x+1)
            self.count += 1

        elif self.count == 3:
            play_seq = None
            cpu_turn1 = self.cpu_array[0]
            user_turn1 = self.user_array[0]
            for i in self.winning_array:
                if user_turn1 not in i:
                    if cpu_turn1 in i:
                        play_seq=i
                        break
            play_seq.remove(cpu_turn1)
            for i in play_seq:
                if self.game_array[i-1] == "-":
                    self.game_array[i-1] = self.cpu_sign
                    self.cpu_array.append(i)
                    self.count += 1
                    break
                else:
                    pass

        elif self.count >= 4:
            temp_count = self.count
            test_count = 0
            two_moves = []
            for i in range(len(self.cpu_array)):
                for j in range(i + 1, len(self.cpu_array)):
                    two_moves.append([self.cpu_array[i], self.cpu_array[j]])
            counting = 0
            for i in self.winning_array:
                for j in two_moves:
                    for k in j:
                        if k in i:
                            counting += 1
                    if counting == 2:
                        for l in i:
                            if l not in j:
                                temp = l
                        if self.game_array[temp - 1] == "-" and temp_count == self.count:
                            self.game_array[temp - 1] = self.cpu_sign
                            self.cpu_array.append(temp)
                            self.winner = "CPU"
                            self.count += 1
                            test_count += 1
                    else:
                        counting = 0
                if counting == 2 and temp_count == self.count :
                    break

            if test_count == 0 and temp_count == self.count:
                two_moves = []
                for i in range(len(self.user_array)):
                    for j in range(i+1,len(self.user_array)):
                        two_moves.append([self.user_array[i],self.user_array[j]])
                for i in self.winning_array:
                    counting = 0
                    for j in two_moves:
                        for k in j:
                            if k in i:
                                counting += 1
                        if counting == 2:
                            for l in i:
                                if l not in j:
                                    temp = l
                            if self.game_array[temp-1] == "-" and temp_count == self.count:
                                self.game_array[temp - 1] = self.cpu_sign
                                self.cpu_array.append(temp)
                                self.count += 1
                        else:
                            counting = 0
                    if test_count != 0:
                        break

            if temp_count == self.count:
                for i in [1, 3, 5, 7, 9]:
                    if self.game_array[i-1] == "-":
                        self.game_array[i-1] = self.cpu_sign
                        self.cpu_array.append(i)
                        self.count += 1
                        break
                if temp_count == self.count:
                    for i in range(9):
                        if self.game_array[i] == "-":
                            self.game_array[i] = self.cpu_sign
                            self.cpu_array.append(i + 1)
                            self.count += 1
                            break


        self.display()
        c = 0
        for i in self.game_array:
            if i == "-":
                c += 1
        if c == 0:
            self.winner = "No One"





