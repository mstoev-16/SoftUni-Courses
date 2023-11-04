from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for current_task in self.tasks:
            if current_task.name == new_task.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for current_task in self.tasks:
            if current_task.name == task_name:
                current_task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        unfinished_tasks = [task for task in self.tasks if not task.completed]
        removed_tasks = len(self.tasks) - len(unfinished_tasks)
        self.tasks = unfinished_tasks
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        if self.tasks:
            temp_list = [f"{task.details()}" for task in self.tasks]
            return result + '\n'.join(temp_list)
        return result.strip()


# task = Task("Tst", "27.04.2020")
# print(task.change_name("New name"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())