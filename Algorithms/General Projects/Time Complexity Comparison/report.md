## Table 1: Time Complexity Comparison

| Algorithm      | Best Time Complexity | Worst Time Complexity |
| -------------- | -------------------- | --------------------- |
| Linear Search  | O(1)                 | O(n)                  |
| Binary Sort    | O(1)                 | O(logn)               |
| Insertion Sort | O(n)                 | O(n^2)                |
| Selection Sort | O(n)                 | O(n^2)                |
| Bubble Sort    | O(n)                 | O(n^2)                |

## Table 2: Recorded Time for Algorithms

| Algorithm      | Time Complexity | Recorded Time |
| -------------- | --------------- | ------------- |
| Linear Search  | O(n)            | 2.289e-05     |
| Selection Sort | O(n^2)          | 5.412e-05     |
| Insertion Sort | O(n^2)          | 5.412e-05     |
| Bubble Sort    | O(n^2)          | 8.726e-05     |

## Table 3: Unique Data Check

| Algorithm      | Sorting by ID | Sorting by First Name | Sorting by Last Name |
| -------------- | ------------- | --------------------- | -------------------- |
| Selection Sort | 5.007e-05     | 6.437e-05             | 0.0001               |
| Insertion Sort | 2.289e-05     | 2.074e-05             | 3.290e-05            |
| Bubble Sort    | 4.148e-05     | 7.010e-05             | 0.0002               |

## Table 4: Identical Data Check

| Algorithm      | Sorting by ID          |
| -------------- | ---------------------- |
| Selection Sort | 7.08e-05 Seconds       |
| Insertion Sort | 2.86e-05 Seconds       |
| Bubble Sort    | 6.72e-05 Seconds       |

## Conclusion

### Table-1: How Fast Different Methods Work
In the first table, we looked at how fast or slow different ways of sorting and searching are. We learned that looking for an item in a list one-by-one (linear search) can take a while if the list is long. But if the list is sorted, a method called binary search can find an item much faster.

### Table-2: Time for Sorting and Searching Random Student Info
In the second table, we timed how long it took to sort and search a list of students with different names, IDs, and other details. The times were pretty close to what we expected from the first table. Searching was super fast because the list was small. For sorting, the time taken was almost the same for all methods because the student details were all mixed up (random).

### Table-3: Unique Data Check
The third table was interesting. Here, we sorted a list that was already in order. Some methods, like insertion sort and bubble sort, were faster because they could see that the list was already sorted. This shows that some methods are smarter than others when the list is already in some kind of order.

### Table-4: Identical Data Check
In the fourth table, every student had the same details. All the sorting methods took about the same time. This is because when everything is the same, it doesn't really matter how you sort it; it ends up being the same.
