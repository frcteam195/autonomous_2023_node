from abc import ABC, abstractmethod
from actions_node.default_actions.SeriesAction import SeriesAction

class AutoBase(ABC):
    @abstractmethod
    def getAction(self) -> SeriesAction:
        pass