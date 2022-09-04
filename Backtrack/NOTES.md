# Backtrack

Solving a backtracking problem is actually a traversal process of a decision tree. Now you only need to think about 3 terms:

- Path: the selection that have been made.
- Selection List: the selection you can currently make.
- End Condition: the condition under which you reach the bottom of the decision tree, and can no longer make a selection.

Here shows the pseudo code of the framework:

```python
result = []
def backtrack(Path, Selection List):
    if meet the End Condition:
        result.add(Path)
        return

    for selection in Selection List:
        select
        backtrack(Path, Selection List)
        deselect
```
