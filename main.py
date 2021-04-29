import MarketingFirmCreator
from MarketingFirm import MarketingFirm


class Simulation:
    def __init__(self):
        manager = MarketingFirmCreator.choose_manager_type()
        MarketingFirm(manager)


Simulation()
