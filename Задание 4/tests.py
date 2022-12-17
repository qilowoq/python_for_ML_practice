import unittest
from task_manager import TaskManager

class TestComplex(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = TaskManager()

    def test_add_and_delete_task(self):
        task = self.manager.create_task('Go to them gym', 'Pump musclues')
        result = self.manager.get_task_by_id(task.get_id())
        self.assertEqual(result, task)
        self.manager.remove_task_by_id(task.get_id())
        result = self.manager.get_task_by_id(task.get_id())
        self.assertEqual(result, None)

    def test_add_and_delete_complex_task(self):
        complex_task = self.manager.create_complex_task('Go to them gym', 'Pump musclues')
        result = self.manager.get_complex_task_by_id(complex_task.get_id())
        self.assertEqual(result, complex_task)
        self.manager.remove_complex_task_by_id(complex_task.get_id())
        result = self.manager.get_complex_task_by_id(complex_task.get_id())
        self.assertEqual(result, None)

    def test_add_and_delete_subtask(self):
        complex_task = self.manager.create_complex_task('Go to them gym', 'Pump musclues')
        subtask = self.manager.create_subtask(complex_task.get_id(), 'drink caffeine', '1 gram)))))))))))')
        result = self.manager.get_subtask_by_id(subtask.get_id())
        self.assertEqual(result, subtask)
        self.manager.get_subtask_by_id(subtask.get_id())
        result = self.manager.get_subtask_by_id(complex_task.get_id())
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()