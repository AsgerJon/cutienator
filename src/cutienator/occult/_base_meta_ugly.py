"""
BaseMetaUgly provides a base metaclass for metaclasses assigned to a
particular shared library.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.mcls import BaseMeta

if TYPE_CHECKING:  # pragma: no cover, no mutate
  pass


class BaseMetaUgly(BaseMeta):
  """
  BaseMetaUgly provides a base metaclass for metaclasses assigned to a
  particular shared library.
  """

  @classmethod
  def getSharedObject(mcls, ) -> str:
    """
    Subclasses *must* implement this method to return the shared object
    file relevant for this sub metaclass.
    """
    raise NotImplementedError
