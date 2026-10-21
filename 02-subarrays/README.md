excalidraw link : https://excalidraw.com/#json=GFi45rq3F54uoGDsN0XBR,_DJPO0iVcCjiUJeumpBtbg (open in incognito)
my  note in arc excalidraw

# DSA Winter Camp — Study Notes: Subarrays

**Instructor:** Dhruv  
**Topic:** Subarrays, carry-forward technique, contribution technique  
**Source basis:** Supplied Wispr Flow transcript, Zoom-native transcript, `print-subarrays.py`, and `subarrays.excalidraw`.

---

## 1. Core definition

An **array** stores a sequence of elements. A **subarray** is a *contiguous* part of an array.

For `A = [1, 2, 4, 6, 9]`, valid subarrays include:

- `[1, 2]`
- `[2, 4, 6]`
- `[4, 6, 9]`
- `[1, 2, 4, 6, 9]`
- `[9]`

`[1, 4]` is **not** a subarray because it skips an element. (It is a subsequence, a different concept.)

Represent a subarray by its inclusive endpoints `(L, R)`, where `0 <= L <= R < n`.

## 2. Number of subarrays

For each starting index `L`, the ending index `R` can be any index from `L` to `n - 1`.

- Start at index `0`: `n` choices.
- Start at index `1`: `n - 1` choices.
- …
- Start at index `n - 1`: `1` choice.

Therefore:

\[
n + (n-1) + \cdots + 1 = \frac{n(n+1)}{2}
\]

For `n = 5`, there are `5 * 6 / 2 = 15` subarrays. The count is **Θ(n²)**.

## 3. Questions/problems discussed in class

1. What is a subarray, and how is it represented using start/end indices?
2. How many subarrays does an array of size `n` contain?
3. Print every subarray.
4. Print the sum of each subarray separately.
5. Why is recomputing each subarray's sum an `O(n³)` solution, and how can it be reduced to `O(n²)`?
6. Find the maximum element of every subarray.
7. Find the minimum element of every subarray.
8. Find the **total sum of all subarray sums**:
   - Brute-force / repeated-sum approach: `O(n³)`.
   - Carry-forward approach: `O(n²)`.
   - Contribution technique: `O(n)`.
9. How do input constraints guide the required time complexity?
10. How should you present a solution in an interview? Start with a correct baseline, state its complexity, then optimize.

---

## 4. Pattern A — Enumerate all subarrays

Use two nested loops:

- Outer loop chooses the left/start index `L`.
- Inner loop chooses the right/end index `R`, beginning at `L`.

Python:

```python
def print_all_subarrays(arr):
    n = len(arr)

    for L in range(n):
        for R in range(L, n):
            print(arr[L:R + 1])
```

**Why `R + 1` in the slice?** Python slices exclude their ending index, while the subarray endpoint `R` is inclusive.

**Complexity:**
- There are `n(n + 1) / 2 = O(n²)` subarrays.
- Printing/copying a subarray can take up to `O(n)` time.
- Total time to print every element of every subarray: **`O(n³)`** in the worst case.
- Auxiliary space for the loop itself: `O(1)`, excluding output and any temporary slice created by Python.

Important distinction: choosing all `(L, R)` pairs takes `O(n²)`; doing `O(n)` work for each pair raises the total to `O(n³)`.

## 5. Pattern B — Sum of each subarray using carry-forward

### Baseline idea

For every `(L, R)`, start a separate loop and sum `arr[L:R + 1]`. This repeats work and costs `O(n³)` overall.

### Carry-forward idea

For a fixed start `L`, the next subarray extends the previous one by exactly one element:

- `[1]` → sum `1`
- `[1, 2]` → previous sum `1` + incoming element `2` = `3`
- `[1, 2, 4]` → previous sum `3` + incoming element `4` = `7`

Reset the running sum when `L` changes. For each `L`, add `arr[R]` as `R` advances.

```python
def print_subarray_sums(arr):
    n = len(arr)

    for L in range(n):
        running_sum = 0
        for R in range(L, n):
            running_sum += arr[R]
            print(running_sum)
```

**Complexity:** `O(n²)` time, `O(1)` auxiliary space.

**Carry-forward rule:** when extending a subarray on the right, update the maintained state using only the incoming element, instead of recalculating the entire subarray.

## 6. Pattern C — Maximum/minimum of each subarray

Maintain a running maximum or minimum for each fixed `L`. Initialize it from the first element of that subarray, `arr[L]`, not `0` or a value carried over from the previous start.

```python
def print_subarray_maxima(arr):
    n = len(arr)

    for L in range(n):
        current_max = arr[L]
        for R in range(L, n):
            current_max = max(current_max, arr[R])
            print(current_max)
```

For minimum, replace `max` with `min` and rename the state to `current_min`.

**Why initialize with `arr[L]`?** Arrays may contain only negative values. Starting at `0` can produce an incorrect maximum for a subarray such as `[-10, -4]`. Resetting for every `L` is also necessary so values from an earlier subarray do not leak into the next one.

**Complexity:** `O(n²)` time and `O(1)` auxiliary space.

---

## 7. Pattern D — Total sum of all subarray sums

This is different from printing each subarray's sum. We need one number: add together the sum of every possible subarray.

For `A = [1, 2, 4, 6, 9]`, the individual subarray sums, grouped by starting index, are:

```text
1, 3, 7, 13, 22
2, 6, 12, 21
4, 10, 19
6, 15
9
```

Their total is **150**.

### Approach 1: Recompute every subarray sum — `O(n³)`

Enumerate `(L, R)` and run another loop from `L` through `R` to calculate each sum. Add each calculated sum to the answer. This is correct but repeats work.

### Approach 2: Carry-forward — `O(n²)`

For each fixed `L`, keep a running sum. Every time the subarray is extended, add the new running sum to the global answer.

```python
def total_subarray_sum_n2(arr):
    n = len(arr)
    answer = 0

    for L in range(n):
        running_sum = 0
        for R in range(L, n):
            running_sum += arr[R]
            answer += running_sum

    return answer
```

For `[1, 2, 4, 6, 9]`, this returns `150`.

**Complexity:** `O(n²)` time, `O(1)` auxiliary space.

### Approach 3: Contribution technique — `O(n)`

Instead of summing each subarray, count how many subarrays contain each individual element.

For an element `arr[i]` at zero-based index `i`:

- **Choices for the left endpoint:** `i + 1` (indices `0` through `i`).
- **Choices for the right endpoint:** `n - i` (indices `i` through `n - 1`).
- **Number of subarrays containing `arr[i]`:** `(i + 1) * (n - i)`.
- **Contribution of this element:** `arr[i] * (i + 1) * (n - i)`.

Thus:

\[
\boxed{\text{Total} = \sum_{i=0}^{n-1} arr[i](i+1)(n-i)}
\]

For `A = [1, 2, 4, 6, 9]`:

| `i` | `arr[i]` | Left choices `i + 1` | Right choices `n - i` | Contribution |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 5 | `1 * 1 * 5 = 5` |
| 1 | 2 | 2 | 4 | `2 * 2 * 4 = 16` |
| 2 | 4 | 3 | 3 | `4 * 3 * 3 = 36` |
| 3 | 6 | 4 | 2 | `6 * 4 * 2 = 48` |
| 4 | 9 | 5 | 1 | `9 * 5 * 1 = 45` |
| | | | **Total** | **150** |

Corrected Python implementation:

```python
def total_subarray_sum(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        total += arr[i] * (i + 1) * (n - i)

    return total


a = [1, 2, 4, 6, 9]
print(total_subarray_sum(a))  # 150
```

**Complexity:** `O(n)` time and `O(1)` auxiliary space.

### Why the contribution formula works

Every subarray that contains `arr[i]` must:

1. Start at an index at or before `i`: `i + 1` choices.
2. End at an index at or after `i`: `n - i` choices.

Each left choice can pair with every right choice, so multiplication gives the number of subarrays containing that element. In the sum of all subarray sums, that element is counted once for each such subarray.

This is the key mental shift: **count how many times each element contributes, rather than constructing every subarray.**

---

## 8. Complexity and constraints

The lecture uses a rough competitive-programming estimate of around `10⁸` simple operations per second. Treat this as a heuristic, not a guarantee: actual limits depend on the language, operation costs, judge, and time limit.

| `n` | `n²` | `n³` | Practical implication |
|---:|---:|---:|---|
| 100 | `10⁴` | `10⁶` | Both are often feasible |
| 500 | `250,000` | `125,000,000` | `n³` may be borderline or too slow |
| 3,000 | `9,000,000` | `27,000,000,000` | Prefer `n²` or better |
| 5,000 | `25,000,000` | `125,000,000,000` | `n²` may be feasible depending on limits |
| 100,000 | `10¹⁰` | `10¹⁵` | Neither `n²` nor `n³` is feasible; seek linear or near-linear |

Do not judge an algorithm by Big-O alone. Check the maximum constraints, the exact work inside each loop, and the time limit.

## 9. Technique comparison

| Task | Main technique | Time |
|---|---|---:|
| Enumerate all `(L, R)` endpoints | Two nested loops | `O(n²)` |
| Print every subarray's elements | Two loops + print each range | `O(n³)` total output work |
| Sum each subarray separately, recomputing from scratch | Three-loop equivalent | `O(n³)` |
| Sum each subarray separately, carrying the sum forward | Carry-forward | `O(n²)` |
| Find each subarray's maximum/minimum | Carry-forward state | `O(n²)` |
| Total sum of all subarray sums, using carry-forward | Running sum + global answer | `O(n²)` |
| Total sum of all subarray sums | Contribution technique | `O(n)` |

---

## 10. Interview approach from the lecture

When asked a problem you have not seen before:

1. State a straightforward correct solution.
2. Explain the algorithm and its time complexity.
3. Identify repeated work or the bottleneck.
4. Improve the solution step by step.
5. Explain why the optimized approach is correct.

For this problem, the progression is `O(n³)` → `O(n²)` → `O(n)`. Do not hide a valid baseline solution while searching silently for the optimal one.

## 11. Code review: your attached `print-subarrays.py`

The code contains the lecture's main approaches. A few points to retain:

- The `ans += s` version is the `O(n²)` carry-forward solution for the **total** of all subarray sums.
- In `totalSubarraySum(arr, n)`, the formula is correct, but the function uses the outer variable `a[i]` rather than its parameter `arr[i]`. That makes the function depend on a global variable and breaks its intended generality. Use `arr[i]`.
- The parameter `n` is optional in Python if you derive it with `len(arr)`.
- The sample `[1, 2, 4, 6, 9]` should produce `150` for the total sum of all subarray sums.

## 12. Quick revision checklist

Before moving on, make sure you can answer these without looking:

- [ ] Define a subarray and distinguish it from a subsequence.
- [ ] Derive `n(n + 1) / 2`.
- [ ] Write the `(L, R)` loops without an off-by-one error.
- [ ] Explain why printing all subarray contents takes `O(n³)` total work.
- [ ] Explain why resetting the running sum for each `L` gives an `O(n²)` algorithm.
- [ ] Implement subarray maximum and minimum, including all-negative arrays.
- [ ] Derive `(i + 1)(n - i)` by counting left and right endpoint choices.
- [ ] Implement the contribution formula and verify that the example returns `150`.
- [ ] Explain the progression from brute force to optimized solution.

### One-line memory hooks

- **Subarray:** contiguous range `[L, R]`.
- **Count:** `n(n + 1) / 2`.
- **Carry-forward:** extend the range; update state with the incoming element.
- **Contribution:** `arr[i] * (i + 1) * (n - i)`.
