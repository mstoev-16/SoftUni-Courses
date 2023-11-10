from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        self.__add_entity(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        self.__add_entity(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        self.__add_entity(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_entity(self.plans, plan)

    def add_subscription(self, subscription: Subscription):
        self.__add_entity(self.subscriptions, subscription)

    def subscription_info(self, subscription_id):
        result = []
        subscription = self.__find_entity_by_id(subscription_id, self.subscriptions)
        customer = self.__find_entity_by_id(subscription.customer_id, self.customers)
        trainer = self.__find_entity_by_id(subscription.trainer_id, self.trainers)
        plan = self.__find_entity_by_id(subscription.exercise_id, self.plans)
        equipment = self.__find_entity_by_id(plan.equipment_id, self.equipment)
        result.append(repr(subscription))
        result.append(repr(customer))
        result.append(repr(trainer))
        result.append(repr(equipment))
        result.append(repr(plan))

        return '\n'.join(result)

    def __add_entity(self, collection, entity):
        if entity in collection:
            return
        collection.append(entity)

    def __find_entity_by_id(self, entity_id, collection):
        for entity in collection:
            if entity.id == entity_id:
                return entity
