# -*- coding: utf-8 -*-

"""Represents a basic game character."""

from typing import ProtProtocol

class GameCharacter(Protocol):
    """Basic representation of a game character."""
    
    def make_a_noise(self) -> None:
        """Let the character make a noise."""