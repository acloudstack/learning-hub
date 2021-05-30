# set

* A set is an unordered collection of items. 
  
* It can have any number of items and they may be of different types (integer, float, string etc.)
  
* Every set element is unique (no duplicates) and must be immutable (cannot be changed).

* However, a set itself is mutable. We can add or remove items from it.

* Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
  
* set of integers
  
        set1 = {1, 2, 3}
        print(set1)

        Output: {1, 2, 3}

* set of mixed datatypes
  
        set2 = {1.0, "Hello", "World", (1, 2, 3)}
        print(set2)

        Output: {1.0, (1, 2, 3), 'Hello', 'World'}