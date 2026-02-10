from abc import ABC, abstractmethod


class Job(ABC):
    interval: str  # Should be '6h' or '1d' in subclasses

    @abstractmethod
    def run(self):
        pass
