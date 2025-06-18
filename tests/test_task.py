from lib.tasks import *
import pytest

def test_empty_tasklist():
    tasklist = Tasklist()
    assert tasklist.get_tasks() == 'no tasks'

def test_a_single_task_added():
    tasklist = Tasklist()
    tasklist.add_task('do laundry')
    assert tasklist.get_tasks() == ['do laundry']

def test_multiple_tasks_added():
    tasklist = Tasklist()
    tasklist.add_task('do laundry')
    assert tasklist.get_tasks() == ['do laundry']
    tasklist.add_task('go for a walk')
    assert tasklist.get_tasks() == ['do laundry', 'go for a walk']

def test_complete_task():
    tasklist = Tasklist()
    tasklist.add_task('do laundry')
    tasklist.add_task('go for a walk')
    tasklist.get_tasks() == ['do laundry', 'go for a walk']
    tasklist.complete_task('go for a walk')
    assert tasklist.get_tasks() == ['do laundry']

def test_complete_task_not_in_tasklist():
    tasklist = Tasklist()
    tasklist.add_task('do laundry')
    tasklist.add_task('go for a walk')
    tasklist.get_tasks() == ['do laundry', 'go for a walk']
    with pytest.raises(Exception) as e:
        tasklist.complete_task('cook')
    assert str(e.value) == 'task not in list'
