"""RitualExpert is what every expert of 'RitualGenerator' is built on:
it knows the generator it works for."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from .._ritual_generator import RitualGenerator


class RitualExpert:
  """
  What every expert of 'RitualGenerator' is built on. The generator
  writes the ritual file of one class of Qt, and hands each part of
  that work to an expert: which way a function of Qt is reached, how a
  type crosses between Python and C++, what the compiler says of a
  file, and so on. An expert knows the generator it works for, and
  asks it for the class, the part, the tree, and for the other
  experts.

    expert = CopyExpert()
    expert.setGenerator(generator)
    expert.getGenerator()     # the generator

  The generator makes its experts itself, one of each kind, through
  'RitualGenerator.getExpert'; nobody else has to.

  You provide
  -----------

  - 'setGenerator': the generator the expert works for. Required.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  __ritual_generator__ = None  # type: Optional[RitualGenerator]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getGenerator(self) -> RitualGenerator:
    """
    Gives the generator the expert works for.

    Provided by you, through 'setGenerator'. Nothing fills it in for
    you.

    Raises
    ------

    MissingVariable
      'setGenerator' has not been called.
    """
    if self.__ritual_generator__ is None:
      from .._ritual_generator import RitualGenerator
      raise MissingVariable(self, '__ritual_generator__', RitualGenerator)
    return self.__ritual_generator__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setGenerator(self, generator: RitualGenerator) -> None:
    """
    Tells the expert which generator it works for.

    Required, and once: an expert works for one generator.

    Raises
    ------

    TypeException
      'generator' is not a 'RitualGenerator'.
    """
    from .._ritual_generator import RitualGenerator
    if not isinstance(generator, RitualGenerator):
      raise TypeException('generator', generator, RitualGenerator)
    self.__ritual_generator__ = generator

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which expert this is and for which generator."""
    clsName = type(self).__name__
    if self.__ritual_generator__ is None:
      return '<%s still waiting for: setGenerator>' % clsName
    return '<%s for %s>' % (clsName, self.__ritual_generator__)

  __repr__ = __str__
