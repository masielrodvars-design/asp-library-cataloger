"""
Base classes for enrichment services.

An enrichment service adds intelligence to a BookProfile.
Different implementations may use:
- Simple rules
- OpenAI
- Anthropic
- Local AI
- Human review
"""


from abc import ABC, abstractmethod


class EnrichmentService(ABC):

    @abstractmethod
    def generate_summary(self, book, metadata):
        pass

    @abstractmethod
    def generate_themes(self, book, metadata):
        pass