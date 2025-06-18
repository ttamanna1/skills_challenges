# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Tasklist:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets tasklist as a list
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Returns list of tasks
        # Side-effects
        #   
        pass # No code here yet

    def completed_task(self):
        # Returns:
        #   deletes task when complete
        # Side-effects:
        #   Throws an exception if no task in list
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given an empty tasklist
#it returns a string 'no tasks'
"""
tasklist = Tasklist()
tasklist() == 'no tasks'

"""
Given a task was added
#returns the task in a list
"""
tasklist = Tasklist()
tasklist.add_task('do laundry') == ['do laundry']

"""
Given multiple tasks were added
#returns the tasks in a list
"""
tasklist = Tasklist()
tasklist.add_task('do laundry') == ['do laundry']
tasklist.add_task('go for a walk') == ['do laundry', 'go for a walk']

"""
Given a task was completed
#deletes the task and returns the list with remaining tasks
"""
tasklist = Tasklist()
tasklist.add_task('do laundry') == ['do laundry']
tasklist.add_task('go for a walk') == ['do laundry', 'go for a walk']
tasklist.completed_task('do laundry') == ['go for a walk']

"""
Given a user tries to complete a task that is nt in the tasklist
#raises error
"""
tasklist = Tasklist(['do laundry'])
tasklist.completed_task('go for a walk') == 'Task not in list'

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
