from MarketingFirm import MarketingFirm
from SweepstakesStackManager import StackManager
from SweepstakesQueueManager import QueueManager


def choose_manager_type():
    choice = input("Would you like to use a stack or a queue manager?")
    if choice == 'stack':
        manager = StackManager()
        return manager
    if choice == 'queue':
        manager = QueueManager()
        return manager
