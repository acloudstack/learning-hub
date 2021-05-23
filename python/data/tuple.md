# tuple 
* A tuple is a ordered sequence of elements. 
  
* Because tuples are immutable, their values cannot be modified. It is formatted as below.
  
* A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.
  
* Just as lists are defined by having items(/elements/values) between square brackets [ ], a tuple is defined by having items(/elements/values) between brackets(/parentheses) ( ) separated by commas ','
  
* Create a tuple:
  * Empty tuple mytuple = ()
  
  * tuple having integers: tuple_1 = (1, 2, 3)
  
  * tuple having mixed items: tuple_2 = (1, 'Hello')
  
  * Create a tuple having just one element
            tuple_with_one_element = (1,) or

            tuple_with_one_element = 1,
            print(tuptuple_with_one_element)

            Output:
            (1,)

  * nested tuple: 
    * tuple_3 = (1, 'Hello', (1, 2, True))
  
    * tuple_person = ('Joe', ('joe@example.com', '+1 123 456 7890))
  
  * tuple packing and unpacking:
    * Packing: a tuple can also be defined as 
            tuple_4 = 1, 2, 3, 'Hello'
            print(tuple_4) 
            
            Output:
            (1, 2, 3, 'Hello') 

    * Unpacking: We can define a statement like this 
            a, b, c, d = tuple_4
            print(a)
            print(a)
            print(a)
            print(a)
            
            Output:
            1
            2
            3
            'Hello'

* Access elements in a tuple:
  1. Tuple is an order sequence
   
  2. The items can be accessed using index. Index must be an integer and starts from 0
            tuple_0 = (1, 'Hello', (24, 'string1), [1, 2, 3])
            print(tuple_0[0])
            print(tuple_0[1])
            print(tuple_0[2])
            print(tuple_0[2][0])
            print(tuple_0[3])

            Output:
            1
            'Hello'
            (24, 'string10)
            24
            [1,2,3]
          
  3. Negative index, the last item is at index -1
  
  4. Slice: We can access a range of items in a tuple
            tuple_1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

            tuple_1[0:3]
            Output: (0, 1, 2)

            tuple_1[:3]
            Output: (0, 1, 2)

            tuple_1[1:3]
            Output: (1, 2)

            tuple_1[-10:]
            Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

  5. Reverse tuple using Slice notation:
        tuple_1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        reverse_tuple = tuple_1[::-1]
        print(reverse_tuple)
        Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

        reverse_tuple_2 = tuple_1[::-2]
        print(reverse_tuple_2)
        Output: (9, 7, 5, 3, 1)

* Number of items in a tuple: len()

* Modifying a tuple:

* Delete a tuple: del tuple_1

* tuple Methods:
  * count
        tuple_1 = ('h', 'e', 'l', 'l', '0')

        print(my_tuple.count('h'))  # Output: 1
        print(my_tuple.index('l'))  # Output: 2

* tuple operations:
  * membership test:
        tuple_1 = ('h', 'e', 'l', 'l', '0')
        
        print('l' in tuple_1)
        print('t' in my_tuple)
        Output:
            True
            False

        print('l' not in tuple_1)
        print('t' not in tuple_1)
        Output:
            False
            True

  * iterating through a tuple:
        # for loop to iterate through a tuple
        tuple_names = ('Jane', 'Joe')
        for name in tuple_names:
            print("Hello", name)
        
        Output:
            Hello Jane
            Hello Joe

* Advantages of tuple over list:
