Algorithm Analysis
====================

-- regarding Big-O efficiency of Python data struture List operations. The depth that we can go here is amazing ( and more valuable ) than just considering this on a Pythonic level. They big question is 'why' and 'how' did them implement these things in C language to achieve these results. This is a dive we should do


Questions
--------------

- Two common operations are indexing and assigning to an index position. Both of these operations take the same amount of time no matter how large the list becomes. When an operation like this is independent of the size of the list they are O(1). How did they achieve this?


Review
--------------

- Logarithmn Math related to division

- Anagram variations and analysis

- Popping timeit and efficiency


Homework
-------------

-- Look at how a Linked-List and Map are implemented in C to she some light on why list operations are O(n) versus O(1)

-- Can we find any information about Python ( C API ) implements things to match up what we learned above

-- Interview questions/problems from books that ask about Big-O notation and comprehension::

        Question: [ Searching through an array] Given a sorted array of integers, how can you find the location of a particular integer 
        x?
            Good answer: Use binary search.  Compare the number in the middle of the arra
            y 
            with x.  If it is equal, we are done.  If the number is greater, we know to look in the 
            second half of the array.  If it is smaller, we know to look in the first half.  We can 
            repeat the search on the appropriate half of the array by comparing the middle
            element of that array with x, once again narrowing our search by a factor of 2.  We 
            repeat this process until we find x.  This algorithm takes O(log n) time.

            Not ‐ so ‐ good answer: Go through each number in order and compare it to x.  This 
            algorithm takes O (n) time.



Show-and-Tell from Homework
---------------------------------

Graph the known(s) of Big-O effeiciency for Python List and Dict Operators that you care about::

    list index Get Set

    dict Get Set

Big-O efficiency of DFS and BFS::

    - read about these efficiencies ( http://bigocheatsheet.com/ )

    - then build different solutions ( recursive, Stack, Queue, state machine )

    - graph them for worst, best and average cases

    - what are the Big-O efficiences of each solution? Do they correspond with what we read about?

Use Project Euler problems and guess what the Big-O Efficiency is:: 

    - https://projecteuler.net/problem=1

    - https://projecteuler.net/problem=3

    - https://projecteuler.net/problem=5

    - https://projecteuler.net/problem=8

    - write solutions ( read about the answers ) 

    - guess ( write it down ) what he Big-O efficiency is 

    - graph them and see if your solutions correspond to the guesses

    - optimize them?

Look for deeper explanations regarding C Python implementations::

    - read about Linked List and Hashes in C book

    - try to find information about how Python implements these at this level





