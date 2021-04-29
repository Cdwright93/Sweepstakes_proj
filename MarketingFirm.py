from Sweepstake import Sweepstake
from SweepstakesQueueManager import QueueManager
from SweepstakesStackManager import StackManager


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        sweepstake = Sweepstake()
        self.manager.insert_sweepstakes(sweepstake)
