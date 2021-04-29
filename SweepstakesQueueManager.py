from data_queue import Queue
from Sweepstake import Sweepstake


class QueueManager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstakes):
        self.queue.enqueue(sweepstakes)


    def get_sweepstakes(self):
        return self.queue.dequeue()
