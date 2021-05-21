class Client:
    group = []
    addres = ()  # ip+port


    def _init_(self):
        self.group = []
        self.group.append('all')


    def is_in_group(self, group):
        for gr in self.group:
            if gr == group:
                return True
        return False


    def set_client(self, groups, addres):
        self.group=groups
        self.addres = addres