# Python Binary Search Tree

A Python implementation of a dynamic binary search tree (BST) with functionality for insertion, deletion, traversal, and key-value management. This project demonstrates fundamental data structure principles and is accompanied by comprehensive unit tests.

## Features
- **Dynamic Node Management** – Add, remove, and retrieve nodes dynamically.
- **Key-Value Storage** – Store data as key-value pairs.
- **Traversals** – In-order traversal for sorted output.
- **Custom Node Class** – Encapsulates node properties and relationships.
- **Error Handling** – Handles invalid keys with appropriate exceptions.
- **Unit Tests** – Comprehensive tests for tree operations.

## Installation
### Prerequisites
- Python 3.x

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Python-Binary-Search-Tree.git
   cd Python-Binary-Search-Tree
   ```
2. Run the main program:
   ```bash
   python3 bst.py
   ```

## How to Use
### Example Usage:
1. Insert key-value pairs into the tree:
   ```python
   bst.insert(11, "banana")
   bst.insert(6, "apple")
   bst.insert(12, "carrot")
   ```
2. Retrieve a value by its key:
   ```python
   print(bst.get(11))  # Output: "banana"
   ```
3. Remove a key:
   ```python
   bst.remove(6)
   ```
4. Perform in-order traversal:
   ```python
   bst.inorder_traversal_print()
   ```

## File Structure
```
📂 Python-Binary-Search-Tree
├── 📄 bst.py          # Binary Search Tree implementation
├── 📄 node.py         # Node class for tree structure
├── 📄 test.py         # Unit tests for tree operations
├── 📄 utils.py        # Utility functions for testing and validation
```

## Unit Testing
To run the tests, execute the following command:
```bash
python3 test.py
```

## Contributing
Feel free to fork this repository and submit pull requests for improvements, additional features, or bug fixes.

## License
This project is open-source and available under the MIT License.

---
🌳 *Learn, experiment, and master binary search tree data structures with Python!*

