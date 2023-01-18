from collections import namedtuple                                 # Importing namedtuple()
Index = namedtuple('Index', ['names', 'id'])                       # Creating a subclass named index to convert the given tuple to namedtuple
weekday = [('Nihal', 1),('Santosh', 2),('Manoj', 3),('Kavya', 4),('Shilpa', 5),('Tanushree', 6),('Maytree', 7)]
x = [Index(*el) for el in weekday]                                 # List comprehension to make all tuples into a namedtuple
print(x)
for i in x:
    print(i.names, i.id)                                           # Now i is an individual namedtuple(), printing out based on their 'key' names

