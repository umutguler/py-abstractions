"""
Basic CRUD abstractions for any implementation.
"""

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class Create(ABC):
    """Create resource abstractions."""
    @abstractmethod
    def create(self, resource, data):
        """Create a resource."""

# pylint: disable=too-few-public-methods
class Read(ABC):
    """Read resource abstractions."""
    @abstractmethod
    def read(self, resource):
        """Read a resource."""

# pylint: disable=too-few-public-methods
class Update(ABC):
    """Update resource abstractions."""
    @abstractmethod
    def update(self, resource, data):
        """Update a resource."""

# pylint: disable=too-few-public-methods
class Delete(ABC):
    """Delete resource abstractions."""
    @abstractmethod
    def delete(self, resource):
        """Delete a resource."""
