"""
CppBox implements the descriptor protocol to lazily create the occult C++
object.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from worktoy.desc import AttriBox

if TYPE_CHECKING:  # pragma: no cover, no mutate
  pass

T = TypeVar('T')


class CppBox(AttriBox):
  """
  CppBox implements the descriptor protocol to lazily create the occult C++
  object.
  """
