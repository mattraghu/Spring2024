# Some C++ Notes

## Maps

### Format

```cpp
map<keyType, valueType> mapName;
```

### Example

```cpp
map<string, int> testMap;
testMap["test"] = 1;
testMap["test2"] = 2;
```

## Pointers

Pointers are variables that store the memory address of another variable.

You can use the `&` operator to get the memory address of a variable and the `*` operator to get the value at the memory address.

When you declare a variable, you can declare it as a pointer by using the `*` operator. This will allow the compiler to know that the variable is a pointer and not a regular variable.

### Format

```cpp
int *ptr; // pointer to an integer
int x = 5;
ptr = &x; // ptr now holds the memory address of x

cout << *ptr; // prints the value at the memory address of x (5)
```

If you want to create a pointer to a pointer, you can use the `**` operator.

### Format

```cpp
int **ptr; // pointer to a pointer to an integer
int x = 5;
int *ptr2 = &x;
ptr = &ptr2; // ptr now holds the memory address of ptr2

cout << **ptr; // prints the value at the memory address of ptr2 (5)
```

## References

References are similar to pointers, but they are not variables that store memory addresses. Instead, they are aliases for other variables.

You can use the `&` operator to create a reference to a variable.

### Format

```cpp
int x = 5;
int &ref = x; // ref is now an alias for x

cout << ref; // prints the value of x (5)
```

## Auto

The `auto` keyword is used to automatically deduce the type of a variable at compile time.

### Format

```cpp
auto x = 5; // x is an integer
auto y = 5.0; // y is a double
```

## Advanced For Loop

Say we have a map

```cpp
map<string, int> testMap;
testMap["test"] = 1;
testMap["test2"] = 2;
```

How do we iterate through it?

```cpp
for (auto const& x : testMap) {
    cout << x.first << " " << x.second << endl;
}
```

The `:` tells the compiler that for each element in the map, we want to do something with it. `x` is a reference to the current element in the map. `x.first` is the key and `x.second` is the value.

In this case, the auto keyword will cause x to automatically have the type of the elements in the map (which is a pair of strings and integers).

It is important to make it a **const reference** because we don't want to modify the elements in the map accidentally.
