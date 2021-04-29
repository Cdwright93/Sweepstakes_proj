import MarketingFirmCreator
from MarketingFirm import MarketingFirm


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        manager = MarketingFirmCreator.choose_manager_type()
        MarketingFirm(manager)
