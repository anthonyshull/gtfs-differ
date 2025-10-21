from abc import ABC, abstractmethod
from os import environ
from typing import Self

class Step(ABC):
    """
    An Abstract Base Class for a step in a workflow.
    Has two abstract methods: `process` and `success`.
    Process returns `Self` and success returns a `bool`.
    This allows for chaining the two together.
    """
    @abstractmethod
    def process(self) -> Self:
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
