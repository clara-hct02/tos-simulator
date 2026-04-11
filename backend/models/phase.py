from abc import ABC, abstractmethod

class Phase(ABC):

    @abstractmethod
    def next_phase(self):
        pass

