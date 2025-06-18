from lib.todo import *

def test_get_task():
    todo = Todo('go for a walk')
    assert todo.task == 'go for a walk'
    
def test_check_incomplete_task():
    todo = Todo('go for a walk')
    assert todo.complete == False
    
def test_check_complete_task():
    todo = Todo('go for a walk')
    todo.mark_complete()
    assert todo.complete == True