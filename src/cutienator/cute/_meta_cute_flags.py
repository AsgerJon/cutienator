"""
MetaCuteFlags is the metaclass of the flags classes of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.mcls import BaseMeta

from . import CuteFlagsSpace, ShortNameMeta


class MetaCuteFlags(ShortNameMeta, BaseMeta):
  """
  Gives the body of a flags class a 'CuteFlagsSpace' to run in, and
  gives the names of the flags to the class that holds the flags
  class; see 'ShortNameMeta'. You never use it by name: a flags class
  is based on 'CuteFlags'.

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

  def getShortNames(cls) -> dict:
    """
    Gives each name Qt wrote in the flags enum with the value the class
    has at it, in the order written. 'NULL' is among them only where
    Qt names it.
    """
    names = type.__getattribute__(cls, '__namespace__').getFlagNumbers()
    named = cls.__named_flags__
    return {name: named[name] for name in names}
