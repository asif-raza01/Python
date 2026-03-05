a=5
print(id(a))
b=5
print(id(b)) #This will return the same memory address as id(a) because small integers are cached by Python and both a and b reference the same object in memory.
#now remember this works for small integers (typically from -5 to 256) and some other immutable types like strings, but for larger integers or mutable types, Python may create separate objects in memory, resulting in different memory addresses.
c=1000000000  
print(id(c)) #This will likely return a different memory address than id(a) and id(b) because larger integers are not cached by Python and may be stored in different locations in memory.
d=1000000000 
print(id(d)) #This will likely return the same memory address as id(c) because Python may optimize memory usage by reusing the same object for identical immutable values, even if they are larger integers. However, this behavior can vary based on the implementation and version of Python being used.