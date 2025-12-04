import math


line = ""
combo = []
start = 0
num = 0;

class Dial:
    def __init__(self, position):
        self.position = position
        self.dial_size = 100  
        self.num = 0;
 
    # def turn_right(self, steps):

    #     if self.position!= 0 and self.position + steps >= self.dial_size + 1:
    #         self.num += 1
    #     self.position = (self.position + steps) % self.dial_size

    # def turn_left(self, steps):
    #     if steps >= self.dial_size:
    #         turn_left_overflow(steps)
    #     self.position = (self.position - steps) % self.dial_size

    def get_position(self):
        return self.position

    def return_num(self):
        return self.num
    
    def turn_left(self, steps):
        if steps >= self.dial_size:
            overflow_turns = steps // self.dial_size
            self.num += overflow_turns
        remaining_steps = steps % self.dial_size
        if self.position!= 0 and self.position - remaining_steps < 0:
            self.num += 1
        self.position = (self.position - remaining_steps) % self.dial_size
        

    def turn_right(self, steps):
        if steps >= self.dial_size:
            overflow_turns = steps // self.dial_size
            self.num += overflow_turns
        remaining_steps = steps % self.dial_size
        if self.position!= 0 and self.position + remaining_steps >= self.dial_size + 1:
            self.num += 1
        self.position = (self.position + remaining_steps) % self.dial_size
    

dial = Dial(50)

with open('main\\day1\\comboText.txt') as f:
    print("running")
    for line in f:
        line = line.rstrip('\n')
        if line and line[0] == 'R':
            dial.turn_right(int(line[1:]));
            

        if line and line[0] == 'L':
            dial.turn_left(int(line[1:]));
            

        if dial.get_position() == 0:
            num += 1
            print("Reset ", line)
        print(line)
    print(num + dial.return_num())
    


