"""
CuteFlags is the one base of every flags enum of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import KeeMeta

from . import DoorNumber, MetaCuteFlags

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Iterator, List, Optional, Tuple


class CuteFlags(metaclass=MetaCuteFlags):
  """
  The base of every flags enum of Qt. A subclass names its flags with
  their numbers, the way the header of Qt writes them:

    class AlignmentFlag(CuteFlags):
      AlignLeft = 0x0001
      AlignLeading = AlignLeft
      AlignTop = 0x0020
      AlignVCenter = 0x0080
      AlignHCenter = 0x0004
      AlignCenter = AlignVCenter | AlignHCenter

    both = AlignmentFlag.AlignLeft | AlignmentFlag.AlignTop

  What to expect
  --------------

  - Every number is a value of the class. A value is made the first
    time its number is asked for, and kept: one number is one object,
    so 'AlignmentFlag(0x21) is both'. Nothing is made up front but the
    names Qt gives.
  - A is A: a value is only itself. It is never an 'int', and its
    number is 'both.value', or 'int(both)'. Two names for one number
    are one object.
  - 'NULL' is the value of no flag at all, in every flags class. Where
    Qt names it, as 'NoModifier', both names hold it.
  - '|', '&' and '^' take two values of one class and give a value of
    that class; '~' gives the value of every other bit. A value of
    another class, or a bare number, is refused.
  - 'AlignmentFlag.AlignTop in both' says whether every bit of the
    first is set in the second. A value is truthy unless it is 'NULL'.
  - Calling the class gives a value: of a number, of a name, or 'NULL'
    for nothing.
  - Tolerance: '==' and '+' answer for the number, so
    'box.exec() == StandardButton.Yes' holds and a value plus 1 is a
    plain number. The hash follows the number, as it has to. Among
    values A is still A: values of two classes are never equal.
  - In a signature, as '@overload(AlignmentFlag)', a value is taken,
    and so is a number or a name that Qt gave a name; any other number
    is said out loud: 'setAlignment(AlignmentFlag(0x21))'.
  - A value is never changed, and neither is the name of a flag on its
    class.

  A flags class is based on 'CuteFlags' and on no flags class that has
  flags of its own.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  #  How many bits the C++ number of the class has, and whether it has a
  #  sign; see 'CuteFlagsSpace.getNumberLayout'.
  __flag_bits__: int = 32
  __flag_signed__: bool = True
  #  The value at each name of the class, 'NULL' among them.
  __named_flags__: Optional[Dict[str, Any]] = None
  #  Every value of the class made so far, by its number.
  __known_flags__: Optional[Dict[int, Any]] = None
  #  The values Qt named, each once, in the order written.
  __listed_flags__: Tuple[Any, ...] = ()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CLASS HOOKS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def __class_init__(
      cls,
      name: str,
      bases: tuple,
      space: Any,
      **kwargs,
  ) -> None:
    """
    Gives a flags class that has just been made its values: one at each
    name of its body, and 'NULL'. worktoy calls this at the end of the
    class statement. You never call it.

    Parameters
    ----------

    name : str
      The name of the class just made.

    bases : tuple
      The classes it is built on.

    space : Any
      The 'CuteFlagsSpace' its body ran in, which holds the name and
      the number of each flag.

    Raises
    ------

    TypeError
      The class is built on a flags class that has flags of its own.
    """
    for base in cls.__mro__[1:]:
      if isinstance(base, MetaCuteFlags) and base.__listed_flags__:
        infoSpec = """The flags class '%s' is built on '%s', which has
        flags of its own. Qt builds no flags enum on another, and a
        flags class is based on 'CuteFlags'."""
        info = infoSpec % (name, base.__name__)
        raise TypeError(' '.join(info.split()))
    bits, signed = space.getNumberLayout()
    named, known, listed = dict(), dict(), []
    type.__setattr__(cls, '__flag_bits__', bits)
    type.__setattr__(cls, '__flag_signed__', signed)
    type.__setattr__(cls, '__named_flags__', named)
    type.__setattr__(cls, '__known_flags__', known)
    for flagName, number in space.getFlagNumbers().items():
      flags = cls._getKnown(number, flagName)
      named[flagName] = flags
      if not any(flags is held for held in listed):
        listed.append(flags)
      type.__setattr__(cls, flagName, flags)
    null = cls._getKnown(0, 'NULL')
    named['NULL'] = null
    type.__setattr__(cls, 'NULL', null)
    type.__setattr__(cls, '__listed_flags__', (*listed,))

  @classmethod
  @overload()
  def __class_call__(cls) -> Any:
    """Gives 'NULL', the value of no flag at all."""
    return cls._getKnown(0)

  @classmethod
  @overload(int)
  def __class_call__(cls, number: int) -> Any:
    """
    Gives the value of a number, as 'AlignmentFlag(0x21)'. Any number
    is a value of the class, whether Qt named it or not.

    Raises
    ------

    TypeError
      The number is a 'bool'.
    """
    if number is True or number is False:
      infoSpec = """%r is a 'bool', and no number of '%s'."""
      raise TypeError(infoSpec % (number, cls.__name__))
    return cls._getKnown(number)

  @classmethod
  @overload(str)
  def __class_call__(cls, name: str) -> Any:
    """
    Gives the value at a name, as "AlignmentFlag('AlignTop')". The name
    is written as Qt writes it.

    Raises
    ------

    ValueError
      The class has no such name.
    """
    try:
      return cls.__named_flags__[name]
    except KeyError:
      infoSpec = """'%s' has no flag named '%s'."""
      raise ValueError(infoSpec % (cls.__name__, name))

  @classmethod
  @overload(THIS)
  def __class_call__(cls, flags: Any) -> Any:
    """
    Gives a value of the class back as it is.

    Raises
    ------

    TypeError
      The value is one of another flags class.
    """
    if isinstance(flags, cls):
      return flags
    infoSpec = """%s is no value of '%s'."""
    raise TypeError(infoSpec % (flags, cls.__name__))

  @classmethod
  def __class_iter__(cls) -> Iterator:
    """Goes through the values Qt named, each once, in the order
    written."""
    return iter(cls.__listed_flags__)

  @classmethod
  def __class_len__(cls) -> int:
    """Counts the values Qt named, each once."""
    return len(cls.__listed_flags__)

  @classmethod
  def __class_contains__(cls, item: Any) -> bool:
    """Says whether something is a value of the class."""
    return True if isinstance(item, cls) else False

  @classmethod
  def __class_setattr__(cls, name: str, value: Any) -> None:
    """
    Refuses to bind anything else at the name of a flag, as
    'AlignmentFlag.AlignLeft = 5' would.

    Raises
    ------

    AttributeError
      The name holds a value of flags.
    """
    cls._refuseFlagName(name)
    type.__setattr__(cls, name, value)

  @classmethod
  def __class_delattr__(cls, name: str) -> None:
    """
    Refuses to remove the name of a flag from its class.

    Raises
    ------

    AttributeError
      The name holds a value of flags.
    """
    cls._refuseFlagName(name)
    type.__delattr__(cls, name)

  @classmethod
  def __cast_as__(cls, value: Any) -> Any:
    """
    Says what a signature naming the class takes in the place of a
    value: a number Qt gave a name, or such a name. worktoy asks this
    when a call gives something else than a value of the class.

    Returns
    -------

    Any
      The value, or 'NotImplemented' for anything the class does not
      take: a number Qt gave no name, a name it does not have, and the
      number of a member that came in through a door; see 'DoorNumber'.
    """
    if isinstance(value, DoorNumber):
      return NotImplemented
    if type(value) is int:
      known = cls.__known_flags__.get(cls._wrap(value), None)
      if known is None or known.name is None:
        return NotImplemented
      return known
    if type(value) is str:
      return cls.__named_flags__.get(value, NotImplemented)
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _refuseFlagName(cls, name: str) -> None:
    held = cls.__dict__.get(name, None)
    if isinstance(held, CuteFlags):
      infoSpec = """'%s.%s' is a flag, and the name of a flag is never
      bound to anything else."""
      info = infoSpec % (cls.__name__, name)
      raise AttributeError(' '.join(info.split()))

  @classmethod
  def _wrap(cls, number: int) -> int:
    """
    Brings a number into the C++ number of the class, as C++ itself
    does when a number has more bits than fit: with 32 bits and a sign,
    0xffffffff is -1.
    """
    bits = cls.__flag_bits__
    number &= (1 << bits) - 1
    if cls.__flag_signed__ and number >> (bits - 1):
      number -= 1 << bits
    return number

  @classmethod
  def _getKnown(cls, number: int, name: Optional[str] = None) -> Any:
    """
    Gives the one value of a number, making it the first time. The name
    is taken only then, so the first name written for a number stays
    its name.
    """
    number = cls._wrap(number)
    known = cls.__known_flags__
    try:
      return known[number]
    except KeyError:
      self = object.__new__(cls)
      object.__setattr__(self, 'value', number)
      object.__setattr__(self, 'name', name)
      known[number] = self
      return self

  def _getParts(self) -> List[str]:
    """
    Gives the words the text of a value is made of: its name, or the
    names of its single flags, and what is left over as a number.
    """
    if self.name is not None:
      return [self.name]
    mask = (1 << type(self).__flag_bits__) - 1
    rest, parts = self.value & mask, []
    for flags in type(self).__listed_flags__:
      number = flags.value & mask
      if number and not number & (number - 1) and rest & number:
        parts.append(flags.name)
        rest &= ~number
    if rest:
      parts.append(hex(rest))
    return parts

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __or__(self, other: Any) -> Any:
    if type(other) is not type(self):
      return NotImplemented
    return type(self)(self.value | other.value)

  def __and__(self, other: Any) -> Any:
    if type(other) is not type(self):
      return NotImplemented
    return type(self)(self.value & other.value)

  def __xor__(self, other: Any) -> Any:
    if type(other) is not type(self):
      return NotImplemented
    return type(self)(self.value ^ other.value)

  def __invert__(self) -> Any:
    return type(self)(~self.value)

  def __contains__(self, other: Any) -> bool:
    """
    Says whether every bit of another value of the class is set in this
    one, as 'testFlag' of Qt does: 'NULL' is in 'NULL' alone.
    """
    if type(other) is not type(self):
      return False
    if not other.value:
      return False if self.value else True
    return True if self.value & other.value == other.value else False

  def __bool__(self) -> bool:
    return True if self.value else False

  def __int__(self) -> int:
    return self.value

  def __eq__(self, other: Any) -> Any:
    """
    A is A: among the values of flags and the members of enums, a value
    is equal to itself alone. Tolerance: against anything else it
    answers as its number does, so 'box.exec() == StandardButton.Yes'
    holds. A 'bool' is no number of it.
    """
    if isinstance(other, CuteFlags) or isinstance(type(other), KeeMeta):
      return True if self is other else False
    if type(other) is bool:
      return False
    return self.value == other

  def __hash__(self) -> int:
    """The hash of the number, since a value is equal to its number."""
    return hash(self.value)

  def __add__(self, other: Any) -> Any:
    """Tolerance: a value plus a number is a plain number."""
    return self.value + other

  def __radd__(self, other: Any) -> Any:
    return other + self.value

  def __setattr__(self, name: str, value: Any) -> None:
    infoSpec = """%s is never changed."""
    raise AttributeError(infoSpec % (self,))

  def __delattr__(self, name: str) -> None:
    infoSpec = """%s is never changed."""
    raise AttributeError(infoSpec % (self,))

  def __reduce__(self) -> tuple:
    return type(self), (self.value,)

  def __copy__(self) -> Any:
    return self

  def __deepcopy__(self, memo: Any) -> Any:
    return self

  def __str__(self) -> str:
    return '<%s>.%s' % (type(self).__name__, '|'.join(self._getParts()))

  __repr__ = __str__
