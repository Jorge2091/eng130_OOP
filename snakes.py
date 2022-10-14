from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tounge = True

    def use_tongue_to_smell(self):
        return "if I can touch it, I can smell it"


smart_snake = Snake()
print(f"This function is called from parent class {smart_snake.hunt()}")
print(f"This function is called from the current class {smart_snake.use_tongue_to_smell()}")
print(f"This function is called from the gran parent class {smart_snake.breath()}")

# use the same .md file to add this code with your documentation
