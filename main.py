import pandas as pd

#BFS Ladder
#by Ella Mohanram
#January 27, 2022

read_txt = pd.read_csv("fivewords")
txt_list = read_txt.values.tolist()
word_list = []
for word in txt_list:
    word_list.append([word[0].lower(), -1])

class Dictionary:
    def __init__(self):
        self.word_dict = dict(word_list)

    def set_value(self, check_word):
        self.word_dict[check_word] = 1

    def is_used(self, check_word):
        check_word_value = self.word_dict.get(check_word)
        if check_word_value == -1:
            return True
        else:
            return False

    def print_dictionary(self):
        print(self.word_dict)

    def get_neighbors(self, check_word):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        neighbors = []

        for letter_in_word in check_word:
            for letter_in_alphabet in alphabet:
                maybe_word = check_word.replace(letter_in_word, letter_in_alphabet)
                if maybe_word in self.word_dict:
                    if self.is_used(maybe_word) == True:
                        neighbors.append(maybe_word)
                        self.set_value(maybe_word)

        return neighbors

#finds word ladders through breadth-first search
#parameters: start word and end word
#returns list containing word ladder and count of nodes visited
class bfs_ladder:

    #constructor function that initializes class attributes
    def __init__(self):
        self.queue = []
        self.dictionary = Dictionary()
        self.count = 0
        self.show_ladders = False

    #creates word ladders
    #parameters: start word and end word
    #returns: word ladder or "No path to goal"
    def get_ladder(self, start_word, end_word):
        self.queue.append([start_word])
        self.dictionary.is_used(start_word)
        self.dictionary.set_value(start_word)

        while len(self.queue) > 0:
            current_node = self.queue[0]
            current_node_word = self.queue[0][-1]
            self.queue.pop(0)

            current_word_neighbors = self.dictionary.get_neighbors(current_node_word)
            current_word_neighbors_length = len(current_word_neighbors)

            for i in range(current_word_neighbors_length - 1):
                current_node_copy = current_node.copy()
                current_word_neighbor = current_word_neighbors[i]
                current_node_copy.append(current_word_neighbor)

                self.count += 1

                if self.show_ladders == True:
                    print(current_node_copy)
                else:
                    pass

                if current_word_neighbor == end_word:
                    return current_node_copy
                else:
                    self.queue.append(current_node_copy)

        return 'No path to goal.'

    #resets initialized class attributes
    def reset(self):
        self.queue = []
        self.dictionary = Dictionary()
        self.count = 0

    #takes user input and returns word ladder
    #returns: solution and new run
    def run(self):
        start_word, end_word = input("Enter start and end word: ").split()

        show_ladder = input("Do you want to see the ladders (Y/N): ")
        if show_ladder == 'Y':
            self.show_ladders = True
        else:
            self.show_ladders = False

        solution = self.get_ladder(start_word, end_word)

        print("Enter starting word: " + start_word)
        print("Enter ending word: " + end_word)
        print("Nodes visited: " + str(self.count))
        print("Solution: " + str(solution))
        print("\n")

        self.reset()
        self.run()

run = bfs_ladder()
run.run()




