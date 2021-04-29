from Sweepstake import Sweepstake
from SweepstakesQueueManager import QueueManager
from SweepstakesStackManager import StackManager


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        if self.manager == StackManager:
            Sweepstake()
        if self.manager == QueueManager:
            Sweepstake()
