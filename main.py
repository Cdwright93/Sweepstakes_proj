import MarketingFirmCreator
from MarketingFirm import MarketingFirm


class Simulation:
    def __init__(self):
        MarketingFirm(MarketingFirmCreator.choose_manager_type())


Simulation()
