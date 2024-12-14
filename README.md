# lame-merge-sort-py
Perform a Merge sort on a list: 
1. listsplit(inlist)
  Purpose: Splits the input list recursively into smaller sublists until each sublist contains one or no elements, then merges them back in sorted order using the mergelist() function.
 Process:
  Divides the list into two halves (a and b).
  Recursively calls itself on both halves.
  Merges the sorted halves using mergelist().
2. mergelist(a, b)
  Purpose: Merges two sorted lists (a and b) into a single sorted list.
 Process:
  Uses a while loop to compare and pop elements from the lists.
  Adds smaller elements to the resulting list sortl.
  Handles duplicate elements by appending both.
  Extends the remaining elements of the longer list (if any) to the sorted list.
3. cleanlist(inlist)
  Purpose: Filters out non-numeric elements (like strings or objects) from the input list.
 Process:
  Iterates through the list and checks each element's type.
  Removes non-numeric elements (anything not int or float) and collects them in a separate list junk.
 Output:
  Returns a list: the cleaned list and the list of junk items.
4. mergesort(inlist, order=1, clean=1)
  Purpose: The main function that performs the sorting.
 Parameters:
  inlist: The list to be sorted.
  order: Determines the sorting order:
    1 (default): Ascending.
    2: Descending.
  clean: Determines whether to exclude junk:
    1 (default): Removes non-numeric elements.
    0: Retains non-numeric elements and appends them to the result.
Process:
  Cleans the list using cleanlist().
  Sorts the numeric elements using listsplit().
  Reverses the sorted list if order=2.
  Optionally adds back the junk elements if clean=0.
Observations
 
Strengths:

  Implements a recursive merge sort effectively.
  Handles non-numeric elements gracefully with the cleanlist function.
  Allows flexibility with sorting order and inclusion of junk.
 
Weaknesses:

  Inefficient pop(0) calls:
  The use of pop(0) in mergelist is inefficient because it shifts all elements in the list, making it O(n) for each operation.
  This can significantly slow down the algorithm for large lists.
  cleanlist modification in-place:
  Directly modifies the input list (inlist), which may not be ideal. A copy should be used to avoid side effects.
Redundant conditions in mergelist:
  The elif conditions for equal lengths are unnecessary since they can be combined into a single else block
