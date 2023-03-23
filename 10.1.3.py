from collections import MutableMapping


class DemoClass(MutableMapping):
    def __init__(self):
        pass

    def __contains__(self, k):
        try:
            if self[k]:
                return True
        except KeyError:
            return False

    def setdefault(self,k,d):
        try:
            return self[k]
        except KeyError:
            self[k] = d
            return d






