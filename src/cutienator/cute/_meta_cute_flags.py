"""
MetaCuteFlags is the metaclass of the flags classes of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.mcls import BaseMeta

from . import CuteFlagsSpace


class MetaCuteFlags(BaseMeta):
  """
  Gives the body of a flags class a 'CuteFlagsSpace' to run in, and
  nothing else. You never use it by name: a flags class is based on
  'CuteFlags'.

  Everything a flags class does is in 'CuteFlags' itself, through the
  class hooks of worktoy, so this metaclass implements no operation and
  takes none over.
  """

  @classmethod
  def __prepare__(mcls, name: str, bases: tuple, **kwargs) -> CuteFlagsSpace:
    """
    Gives the namespace the body of a flags class runs in: a new
    'CuteFlagsSpace'. Python calls this at every class statement of a
    flags class, before the body runs.
    """
    return CuteFlagsSpace(mcls, name, bases, **kwargs)
