"""
Ugly encapsulates the C++ representation of something cute.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import weakref
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from .occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional, Any


class Ugly:
  """
  Stands for one C++ object on behalf of its cute side: it holds the
  address of the C++ object and runs rituals on it. The cute classes
  reach C++ through this class and nothing else.

    ugly = Ugly()
    ugly.setAddress(address)      # what the creating ritual returned
    ugly.setCuteSide(cute)
    ugly.call(ritualName)         # the address is passed for you
    Ugly.at(address)              # the Ugly standing for that address

  Terms
  -----

  - The address is the number saying where the C++ object is in memory.
  - The cute side is the Python object people use, as a 'QObject'.
  - A ritual is one plainly named function in cutienator's own shared
    object, run through 'Rituals'.

  You provide
  -----------

  Two things, each through its setter, when the C++ object is created:

  - 'setAddress': where the C++ object is. Once only.
  - 'setCuteSide': the cute object this stands behind.

  What to expect
  --------------

  - 'call' puts the address first, so a cute class never handles one.
  - 'Ugly.at' turns an address that C++ handed back into the Ugly
    standing for it. That is how 'child.parent()' gives the very cute
    object you already hold.
  - An Ugly keeps neither side alive. When its cute object goes, the
    Ugly goes too, and the C++ object is left as it is.
  - Nothing deletes a C++ object yet, and nothing notices when C++
    deletes one. An address held here can therefore go bad.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Every Ugly with an address, under that address. Held weakly.
  __by_address__ = weakref.WeakValueDictionary()

  #  Fallback Variables

  #  Private Variables
  __cpp_address__ = None  # type: Optional[int]
  __cute_side__ = None  # type: Optional[weakref.ref]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getAddress(self) -> int:
    """
    Gives where the C++ object is in memory.

    Provided by you, through 'setAddress'. Nothing fills it in for you.

    Raises
    ------

    MissingVariable
      'setAddress' has not been called on this Ugly.
    """
    if self.__cpp_address__ is None:
      raise MissingVariable(self, '__cpp_address__', int)
    return self.__cpp_address__

  def getCuteSide(self) -> Any:
    """
    Gives the cute object this Ugly stands behind.

    Provided by you, through 'setCuteSide'. Nothing fills it in for you.

    Raises
    ------

    MissingVariable
      'setCuteSide' has not been called on this Ugly.

    RuntimeError
      The cute object no longer exists.
    """
    if self.__cute_side__ is None:
      raise MissingVariable(self, '__cute_side__', object)
    cuteSide = self.__cute_side__()
    if cuteSide is None:
      infoSpec = """The cute object this Ugly stood behind no longer
      exists."""
      raise RuntimeError(' '.join(infoSpec.split()))
    return cuteSide

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setAddress(self, address: int) -> None:
    """
    Tells this Ugly where its C++ object is, and lets 'Ugly.at' find it
    by that address.

    Required before 'call'. It can be called once: an Ugly stands for
    one C++ object for as long as it exists.

    Parameters
    ----------

    address : int
      What the ritual creating the C++ object returned. A positive
      whole number.

    Raises
    ------

    TypeException
      'address' is not an 'int'.

    ValueError
      'address' is zero or negative, which is no place in memory.

    RuntimeError
      An address has been set on this Ugly already.
    """
    if isinstance(address, bool) or not isinstance(address, int):
      raise TypeException('address', address, int)
    if address <= 0:
      infoSpec = """An address is a positive whole number, but received
      %d."""
      raise ValueError(' '.join((infoSpec % address).split()))
    if self.__cpp_address__ is not None:
      infoSpec = """This Ugly already stands for the C++ object at %s and
      cannot be moved to %s."""
      info = infoSpec % (hex(self.__cpp_address__), hex(address))
      raise RuntimeError(' '.join(info.split()))
    self.__cpp_address__ = address
    type(self).__by_address__[address] = self

  def setCuteSide(self, cuteSide: Any) -> None:
    """
    Tells this Ugly which cute object it stands behind.

    Required before 'getCuteSide'. The cute object is not kept alive by
    this. Calling it again replaces the cute object given before.

    Parameters
    ----------

    cuteSide : Any
      The cute object, as a 'QObject'. It must allow weak references,
      which every worktoy object does.
    """
    self.__cute_side__ = weakref.ref(cuteSide)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says where the C++ object is, or that no address is set yet."""
    clsName = type(self).__name__
    if self.__cpp_address__ is None:
      return '<%s with no address yet>' % clsName
    where = hex(self.__cpp_address__)
    return '<%s of the C++ object at %s>' % (clsName, where)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def at(cls, address: int) -> Ugly:
    """
    Gives the Ugly standing for the C++ object at an address.

    Use it on an address a ritual returned, to get from C++ back to the
    Python side: 'Ugly.at(address).getCuteSide()'.

    Parameters
    ----------

    address : int
      An address a ritual returned.

    Returns
    -------

    Ugly
      The one Ugly whose 'setAddress' was given that address.

    Raises
    ------

    LookupError
      No Ugly stands for that address. Either C++ created the object
      itself, or the cute object that stood for it no longer exists.
    """
    try:
      return cls.__by_address__[address]
    except KeyError as keyError:
      infoSpec = """No Ugly stands for the C++ object at %s. Either C++
      created that object itself, or its cute object no longer exists."""
      info = ' '.join((infoSpec % hex(address)).split())
      raise LookupError(info) from keyError

  def call(self, ritualName: str, *args: Any) -> Any:
    """
    Runs one ritual on the C++ object this Ugly stands for.

    Parameters
    ----------

    ritualName : str
      The name of the ritual, as 'Declaration.getRitualName' gives
      it: 'ritual_ZNK7QObject6parentEv'.

    *args : Any
      What the ritual takes after the address of the object, which is
      put first for you. Another object is passed as its address, from
      'getAddress', or as 'None' for no object.

    Returns
    -------

    Any
      What the ritual returns. An address comes back as an 'int', or
      'None' when C++ answered with no object.

    Raises
    ------

    MissingVariable
      'setAddress' has not been called on this Ugly.

    LookupError
      'Rituals' lists no ritual of that name.
    """
    return Rituals.call(ritualName, self.getAddress(), *args)
