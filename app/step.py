from abc import ABC, abstractmethod
from os import environ

class Step(ABC):
    """
    An Abstract Base Class for a step in a workflow.
    Has two functions: `process` and `check`.
    Process returns `None` and check returns a `bool`.
    """
    @abstractmethod
    def process(self) -> None:
        """Processes the step."""
        pass

    @abstractmethod
    def success(self) -> bool:
        """Checks that the step was processed successfully."""
        pass

    def next(self) -> None:
        """Writes to GITHUB_OUTPUT to short-circuit subsequent steps."""
        if self.success():
            path = environ.get("GITHUB_OUTPUT", "/dev/null")

            with open(path, "a") as file:
                print("next=true", file=file)
