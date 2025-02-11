# 🔄 Recursive Fibonacci Solver Naive Memoized Implementation

This project is a Python-based Fibonacci calculator that demonstrates both **naive (pure recursive)** and **eager (memoized recursive)** approaches. It showcases the difference in computational efficiency when solving problems recursively with and without memoization.

## 📌 Features
- **Naive Recursive Solution**: Implements Fibonacci calculation using a basic recursive approach.
- **Eager Recursive Solution**: Uses **memoization (dynamic programming)** to store previously computed values and optimize performance.
- **File-Based Input & Output**: Reads input numbers from a file and writes results to separate output files.
- **Efficiency Comparison**: The execution times of naive and eager approaches can be compared using large Fibonacci numbers.

Run the program with an input file containing Fibonacci sequence indices to compute:
   ```bash
   python3 fibonacci.py input.txt output_naive.txt output_eager.txt
