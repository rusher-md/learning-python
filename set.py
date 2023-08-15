# Python program to demonstrate deletion of elements in a set
# Creating an empty set and then add a list inside that set
# Create a frozenset

def create_set():
    my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    my_set.remove(4)
    print(my_set)


create_set()

# Creating an empty set and then add a list inside that set

def empty_set():
    my_set = set()
    my_set.add("red gear")
    print(type(my_set))


empty_set()

# Create a frozenset

def my_frozen():
    my_set = frozenset(["red", "gear", "company"])
    print("red" in my_set, "blue" in my_set)


my_frozen()

