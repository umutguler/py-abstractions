"""
Basic RESTful abstractions for any implementation.
"""

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class Get(ABC):
    """Create resource abstractions."""
    @abstractmethod
    def get(self, resource, data):
        """Create a resource."""

# pylint: disable=too-few-public-methods
class Post(ABC):
    """Read resource abstractions."""
    @abstractmethod
    def post(self, resource, data):
        """Read a resource."""

# pylint: disable=too-few-public-methods
class Put(ABC):
    """Update resource abstractions."""
    @abstractmethod
    def put(self, resource, data):
        """Update a resource."""

# pylint: disable=too-few-public-methods
class Delete(ABC):
    """Delete resource abstractions."""
    @abstractmethod
    def delete(self, resource):
        """Delete a resource."""
