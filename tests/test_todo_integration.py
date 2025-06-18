from lib.todo_list import *
from lib.todo import *

def test_add_todo_to_todolist():
    todo = Todo('go for a walk')
    todolist = TodoList()
    todolist.add(todo)
    assert todolist.incomplete() == ['go for a walk']
    
def test_add_multiple_todos_to_todolist():
    todo1 = Todo('go for a walk')
    todo2 = Todo('go to gym')
    todolist = TodoList()
    todolist.add(todo1)
    todolist.add(todo2)
    assert todolist.incomplete() == ['go for a walk', 'go to gym']
    
def test_complete_todos():
    todo1 = Todo('go for a walk')
    todo2 = Todo('go to gym')
    todolist = TodoList()
    todolist.add(todo1)
    todolist.add(todo2)
    todo1.mark_complete()
    assert todolist.incomplete() == ['go to gym']
    assert todolist.complete() == ['go for a walk']
    
def test_mark_all_todos_as_complete():
    todo1 = Todo('go for a walk')
    todo2 = Todo('go to gym')
    todolist = TodoList()
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.give_up()
    assert todolist.complete() == ['go for a walk', 'go to gym']