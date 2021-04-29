class MarketingFirm:
    def __init__(self):
        self.type = None

    def choose_manager_type(self):
        choice = ''
        if choice == 'stack':
            self.type = 'stack'
        if choice == 'queue':
            self.type = 'queue'
