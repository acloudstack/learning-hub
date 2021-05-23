  # List

* A list in Python is an orderd sequence of elements. 
  
* Elements in a list are called items
  
* It can have any number of items and they may be of different types (integer, float, string etc.)
  
* A list can also have another list as an item. This is called a nested list.
  
* List in Python is mutable. 
  
* Just as strings are defined as characters between quotes, lists are defined by having items(/elements/values0 between square brackets [ ] separated by commas ','


* Create a list:
  * Empty list mylist = []
  
  * list having integers: list_1 = [1, 2, 3]
  
  * list having mixed items: list_2 = [1, 'Hello']
  
  * another way 
            pow2 = [2 ** x for x in range(10)]
            print(pow2)
            Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

  * nested list: 
    * list_3 = [1, 'Hello', [1, 2, True]]  

* Access elements in a list:
  1. list is an order sequence
   
  2. The items can be accessed using index. Index must be an integer and starts from 0
            list_0 = [1, 'Hello', [24, 'string1], [1, 2, 3]]
            print(list_0[0]]
            print(list_0[1]]
            print(list_0[2]]
            print(list_0[2][0]]
            print(list_0[3]]

            Output:
            1
            'Hello'
            [24, 'string10]
            24
            [1,2,3]
          
  3. Negative index, the last item is at index -1
  
  4. Slice: We can access a range of items in a list
            list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

            list_1[0:3]
            Output: [0, 1, 2]

            list_1[:3]
            Output: [0, 1, 2]

            list_1[1:3]
            Output: [1, 2]

            list_1[-10:]
            Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  5. Reverse list using Slice notation:
        list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        reverse_list = list_1[::-1]
        print(reverse_list]
        Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

        reverse_list_2 = list_1[::-2]
        print(reverse_list_2]
        Output: [9, 7, 5, 3, 1]

* Number of items in a list: len()

* Modifying a list:

* Delete a list: del list_1

* list Methods:
  * count()
        list_1 = ['h', 'e', 'l', 'l', '0']

        print(list_1.count('h'))  # Output: 1
        print(list_1.index['l'))  # Output: 2
    * append()
    * insert()
    * extend()
    * pop()
    * remove()
    * clear()
    * index()
    * sort()
    * copy()
    * \+
    * \*
        
* list operations:
  * membership test:
        list_1 = ['h', 'e', 'l', 'l', '0']
        
        print('l' in list_1)
        print('t' in list_1)
        Output:
            True
            False

        print('l' not in list_1)
        print('t' not in list_1)
        Output:
            False
            True

  * iterating through a list:
        # for loop to iterate through a list
        list_names = ['Jane', 'Joe']
        for name in list_names:
            print("Hello", name)
        
        Output:
            Hello Jane
            Hello Joe

* Advantages of list over tuple:
