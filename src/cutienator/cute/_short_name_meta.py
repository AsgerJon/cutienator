"""
ShortNameMeta gives the names of an enum of Qt to the class that holds
the enum, where C++ has them as well.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.waitaminute import TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict


class ShortNameMeta:
  """
  Gives the names of an enum of Qt to the class that holds the enum.
  In C++ a name of an enum is a name of whatever the enum is written
  inside as well: 'Qt::AlignLeft' is the 'AlignLeft' of
  'Qt::AlignmentFlag', and 'QEvent::Timer' the 'Timer' of
  'QEvent::Type'. So it is here:

    Qt.AlignLeft is Qt.AlignmentFlag.AlignLeft      # True
    QEvent.Timer is QEvent.Type.Timer               # True

  You never use it by name. The metaclasses of the enum classes and of
  the flags classes are built on it, 'Cute' and 'MetaCuteFlags'.

  Terms
  -----

  - The owner is the class whose body binds the enum class, as
    'Type = Type' in the body of 'QEvent', or as the class 'Qt' binds
    every enum of the namespace 'Qt'.
  - A scoped enum is one C++ declares as 'enum class'. C++ keeps its
    names inside the enum, and so does Python: 'Qt.TimerId.Invalid' is
    not 'Qt.Invalid'.

  You provide
  -----------

  - 'scoped=True' on the class statement of a scoped enum:
    'class TimerId(CuteNum, scoped=True)'. An enum that does not say
    so gives its names to its owner.

  What happens
  ------------

  Python tells every value of a class body the class it was bound in,
  through '__set_name__' of the class of that value. For an enum class
  that is its metaclass, and so this method. It binds each name of the
  enum on the owner, to the very member or value the enum has there.

  What to expect
  --------------

  - An owner may bind one enum class at two names, as Qt names the
    combinations of a flags enum apart: 'Alignment = AlignmentFlag'.
    Its names are bound once.
  - A name the body of the owner binds to something else is refused
    with 'TypeError' as the owner is made. Before Python 3.12 that
    reaches the class statement inside a 'RuntimeError'. C++ has no
    two things of one name in one class either.
  - A class built on the owner has the names as it has every other
    name of the owner, and so has every object of it.
  - The 'NULL' of a flags class is a name of the owner only where Qt
    names it, as 'None'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isScoped(cls) -> bool:
    """
    Says whether C++ keeps the names of the enum inside the enum.

    Provided by you, as 'scoped=True' on the class statement. Only
    the class statement of the enum itself counts, not that of a class
    it is built on.

    Raises
    ------

    TypeException
      'scoped' is given and is no 'bool'.
    """
    keywords = cls.__dict__.get('__keyword_arguments__', None) or dict()
    scoped = keywords.get('scoped', False)
    if not isinstance(scoped, bool):
      raise TypeException('scoped', scoped, bool)
    return scoped

  def getShortNames(cls) -> Dict[str, Any]:
    """
    Gives each name Qt wrote in the enum with what the enum has at it,
    in the order written. Each metaclass built on this class says it
    for its own kind of enum.
    """
    raise NotImplementedError

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __set_name__(cls, owner: type, name: str) -> None:
    """
    Binds the names of the enum on the class whose body binds the
    enum. Python calls this as that class is made. You never call it.

    Parameters
    ----------

    owner : type
      The class whose body binds the enum class.

    name : str
      The name the enum class is bound to there.

    Raises
    ------

    TypeError
      The owner holds something else at a name of the enum.
    """
    if cls.isScoped():
      return
    for shortName, value in cls.getShortNames().items():
      try:
        held = owner.__dict__[shortName]
      except KeyError:
        type.__setattr__(owner, shortName, value)
        continue
      if held is value:
        continue
      infoSpec = """'%s' holds the enum '%s' at '%s', and already holds
      something else at '%s', a name of that enum: %r."""
      info = infoSpec % (
          owner.__name__, cls.__name__, name, shortName, held,
      )
      raise TypeError(' '.join(info.split()))
