# 🧠 Lame Merge Sort (Python)

A Python implementation of Merge Sort with additional features like data cleaning and sorting order control.

---

## ⚙️ Functions

### 1. `listsplit(inlist)`
**Purpose:**  
Recursively splits the input list into smaller sublists and merges them back in sorted order.

**Process:**  
- Divides the list into two halves `a` and `b`.
- Recursively sorts both halves using `listsplit()`.
- Merges them with `mergelist()`.

---

### 2. `mergelist(a, b)`
**Purpose:**  
Merges two sorted lists into a single sorted list.

**Process:**  
- Compares and pops the smallest elements from each list using a `while` loop.
- Handles duplicates by appending both.
- Appends any remaining elements from either list to the result.

---

### 3. `cleanlist(inlist)`
**Purpose:**  
Removes non-numeric elements from the input list.

**Process:**  
- Iterates through the list.
- Filters out non-`int` or `float` items.
- Returns two lists:
  - ✅ Cleaned numeric list.
  - 🚫 List of junk items.

---

### 4. `mergesort(inlist, order=1, clean=1)`
**Purpose:**  
Main function to perform the merge sort.

**Parameters:**
- `inlist`: List to be sorted.
- `order`: Sorting order:
  - `1` (default): Ascending.
  - `2`: Descending.
- `clean`: Handle non-numeric elements:
  - `1` (default): Remove them.
  - `0`: Keep and append them after sorting.

**Process:**
- Cleans the list using `cleanlist()`.
- Sorts the list via `listsplit()`.
- Reverses it if `order=2`.
- Adds back junk if `clean=0`.

---

## ✅ Strengths

- 🔁 Efficient recursive merge sort.
- 🧹 Handles non-numeric entries cleanly.
- 🔄 Flexible sorting order and junk inclusion.

---

## ⚠️ Weaknesses

- ❌ **Inefficient `pop(0)`**:  
  - Causes O(n) operations and performance issues on large lists.

- ❌ **Modifies input list in-place**:  
  - Side effects from `cleanlist()`. Should use a copy.

- ❌ **Redundant conditions in `mergelist()`**:  
  - Some branches can be simplified into a single `else` block.

---

## ✨ Suggestions for Improvement

- Replace `pop(0)` with index-based access or `collections.deque` for efficiency.
- Use a copy of `inlist` in `cleanlist()` to avoid mutation.
- Refactor `mergelist()` logic for clarity and performance.

---

Happy Sorting!
