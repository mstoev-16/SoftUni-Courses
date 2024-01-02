from abc import ABC, abstractmethod


class WorkingType(ABC):
    @abstractmethod
    def work(self):
        pass


class EatingType(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(WorkingType, EatingType):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break")


class SuperWorker(WorkingType, EatingType):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break")


class BaseManager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, WorkingType), "`worker` must be of type {}".format(WorkingType)
        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, EatingType), "`worker` must be of type {}".format(EatingType)
        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(WorkingType):
    def work(self):
        print("I'm a robot. I'm working....")


manager1 = BreakManager()
manager2 = WorkManager()

worker1 = Worker()
worker2 = SuperWorker()
worker3 = Robot()

manager1.set_worker(worker1)
manager1.lunch_break()
manager1.set_worker(worker2)
manager1.lunch_break()
# manager1.set_worker(worker3)
# manager1.lunch_break()


manager2.set_worker(worker1)
manager2.manage()
manager2.set_worker(worker2)
manager2.manage()
manager2.set_worker(worker3)
manager2.manage()
