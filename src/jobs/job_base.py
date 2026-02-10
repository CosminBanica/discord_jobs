from abc import ABC, abstractmethod


class Job(ABC):
    interval: str  # Should be 'hourly' or 'daily' in subclasses

    @abstractmethod
    def run(self):
        pass
