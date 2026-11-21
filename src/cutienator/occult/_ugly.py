"""
Ugly encapsulates the C++ representation of something cute.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import weakref
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import Rituals

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
    ugly.setDeleteRitual(name)    # only for a copy Python owns
    ugly.watch()                  # only for a QObject

  Terms
  -----

  - The address is the number saying where the C++ object is in memory.
  - The cute side is the Python object people use, as a 'QObject'.
  - A ritual is one plainly named function in cutienator's own shared
    object, run through 'Rituals'.
  - Python owns a C++ object when the object is a copy that nothing in
    C++ knows of: one Python made of a class that can be copied, as a
    'QSize', or one a ritual made to hand a value back. Nothing but
    Python can ever remove such an object, so Python does.

  You provide
  -----------

  Two things, each through its setter, when the C++ object is created:

  - 'setAddress': where the C++ object is. Once only.
  - 'setCuteSide': the cute object this stands behind.

  And a third for a C++ object Python owns:

  - 'setDeleteRitual': the ritual that removes the C++ object.

  For a C++ object that is a QObject you also call 'watch', once.

  What to expect
  --------------

  - 'call' puts the address first, so a cute class never handles one.
  - 'Ugly.at' turns an address that C++ handed back into the Ugly
    standing for it. That is how 'child.parent()' gives the very cute
    object you already hold.
  - An Ugly keeps neither side alive. When its cute object goes, the
    Ugly goes too.
  - A C++ object Python does not own is left as it is, always. That is
    every 'QObject' and whatever else Qt hands out by its address: Qt
    may still use it, so Python never removes it.
  - A C++ object Python owns is removed when its Ugly goes, by the
    ritual given to 'setDeleteRitual'. It is not removed as the program
    ends: by then Qt may be gone, and the system takes the memory back
    anyway.
  - Python stops owning a C++ object for good at 'disown'. The cute
    side calls that when it hands the address to Qt as an address,
    since Qt may then keep it. From there on the object is left as it
    is, as any other.
  - Qt removes a QObject when it sees fit: a parent removes its
    children when it goes. After 'watch', Qt itself tells when it has
    removed the C++ object, through a QPointer, Qt's own watcher of a
    QObject. 'isGone' then says so, 'getAddress' and 'call' raise
    'RuntimeError' in the place of handing C++ an address where nothing
    is any more, and 'Ugly.at' no longer finds this Ugly.
  - Only a QObject can be watched. For any other C++ object Python does
    not own, nothing notices when C++ deletes it, and an address held
    here can go bad.
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

  #  The three rituals of Qt's 'QPointer<QObject>' a QObject is watched
  #  by: the one making a watcher of a QObject, the one asking it
  #  whether the QObject is gone, and the one removing the watcher.
  __watch_make_ritual__ = 'ritual_ZN8QPointerI7QObjectEC1IvEEPS0_'
  __watch_ask_ritual__ = 'ritual_ZNK8QPointerI7QObjectE6isNullEv'
  __watch_drop_ritual__ = 'ritual_ZN8QPointerI7QObjectED1Ev'

  #  Fallback Variables

  #  Private Variables
  __cpp_address__ = None  # type: Optional[int]
  __cute_side__ = None  # type: Optional[weakref.ref]
  __delete_ritual__ = None  # type: Optional[str]
  #  Runs the delete ritual when this Ugly goes, for as long as Python
  #  owns the C++ object.
  __delete_watch__ = None  # type: Optional[weakref.finalize]
  #  Where the C++ QPointer watching the C++ object is, after 'watch'.
  __watcher_address__ = None  # type: Optional[int]

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

    RuntimeError
      Qt has removed the C++ object, which is known after 'watch'. The
      address is of no use any more, so none is given.
    """
    if self.__cpp_address__ is None:
      raise MissingVariable(self, '__cpp_address__', int)
    if self.isGone():
      infoSpec = """Qt has removed the C++ object at %s, so the cute
      object in front of it stands for nothing any more. Qt removes a
      QObject together with its parent, and after 'deleteLater'."""
      info = infoSpec % hex(self.__cpp_address__)
      raise RuntimeError(' '.join(info.split()))
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

  def getDeleteRitual(self) -> Optional[str]:
    """
    Gives the name of the ritual that removes the C++ object, or None
    for a C++ object Python does not own.

    Provided by you, through 'setDeleteRitual'. It is None again after
    'disown'.
    """
    return self.__delete_ritual__

  def isOwned(self) -> bool:
    """Says whether Python owns the C++ object, and so removes it when
    this Ugly goes."""
    return False if self.__delete_ritual__ is None else True

  def isWatched(self) -> bool:
    """Says whether Qt watches the C++ object, which it does after
    'watch'."""
    return False if self.__watcher_address__ is None else True

  def isGone(self) -> bool:
    """
    Says whether Qt has removed the C++ object.

    Found for you, by asking the QPointer that 'watch' made. Without
    'watch' nothing can tell, and the answer is False.
    """
    if self.__watcher_address__ is None:
      return False
    return Rituals.call(self.__watch_ask_ritual__, self.__watcher_address__)

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

  def setDeleteRitual(self, ritualName: str) -> None:
    """
    Tells this Ugly that Python owns its C++ object, and which ritual
    removes it.

    Only for a copy nothing in C++ knows of. From here on the C++
    object is removed when this Ugly goes, which is when its cute
    object goes. It is not removed as the program ends. Call it after
    'setAddress', once.

    Parameters
    ----------

    ritualName : str
      The ritual of the destructor of the class, as
      'ritual_ZN5QSizeD1Ev' for Qt's '~QSize()'.

    Raises
    ------

    TypeException
      'ritualName' is not text.

    MissingVariable
      'setAddress' has not been called on this Ugly.

    RuntimeError
      A delete ritual has been set on this Ugly already, also when
      'disown' was called since.
    """
    if not isinstance(ritualName, str):
      raise TypeException('ritualName', ritualName, str)
    address = self.getAddress()
    if self.__delete_watch__ is not None:
      infoSpec = """A delete ritual has been set on the Ugly of the C++
      object at %s already. It is set once, and after 'disown' the
      object cannot be taken back."""
      raise RuntimeError(' '.join((infoSpec % hex(address)).split()))
    self.__delete_ritual__ = ritualName
    #  The watch holds the name and the address, and not this Ugly, which
    #  it would otherwise keep from ever going.
    watch = weakref.finalize(self, Rituals.call, ritualName, address)
    watch.atexit = False
    self.__delete_watch__ = watch

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
      itself, or the cute object that stood for it no longer exists, or
      Qt has removed the object an Ugly stood for there, and what is at
      the address now is another one.
    """
    try:
      ugly = cls.__by_address__[address]
    except KeyError as keyError:
      infoSpec = """No Ugly stands for the C++ object at %s. Either C++
      created that object itself, or its cute object no longer exists."""
      info = ' '.join((infoSpec % hex(address)).split())
      raise LookupError(info) from keyError
    if ugly.isGone():
      infoSpec = """Qt has removed the C++ object an Ugly stood for at
      %s. What is there now is another object."""
      raise LookupError(' '.join((infoSpec % hex(address)).split()))
    return ugly

  def watch(self) -> None:
    """
    Has Qt watch the C++ object, so that this Ugly knows when Qt has
    removed it.

    Only for a C++ object that is a QObject: nothing else can be
    watched, and trying ends the program. Call it after 'setAddress',
    once. It makes a C++ QPointer of the object, which Python owns: it
    is removed when this Ugly goes, and not as the program ends.

    Raises
    ------

    MissingVariable
      'setAddress' has not been called on this Ugly.

    RuntimeError
      This Ugly has its C++ object watched already.
    """
    address = self.getAddress()
    if self.__watcher_address__ is not None:
      infoSpec = """Qt already watches the C++ object at %s for this
      Ugly."""
      raise RuntimeError(' '.join((infoSpec % hex(address)).split()))
    watcher = Rituals.call(self.__watch_make_ritual__, address)
    self.__watcher_address__ = watcher
    dropRitual = self.__watch_drop_ritual__
    removal = weakref.finalize(self, Rituals.call, dropRitual, watcher)
    removal.atexit = False

  def addPartAddress(self, address: int) -> None:
    """
    Tells this Ugly one more address its C++ object is known by, and
    lets 'Ugly.at' find it by that address as well.

    A C++ object of a class built on more than one class holds one
    part for each of them, and C++ hands out the address of a part
    where it means the object: a function giving a 'QPaintDevice *'
    gives the address of that part of a QWidget. The cute side adds
    the address of each such part, so that the address leads back to
    the one cute object. 'getAddress' still gives the address
    'setAddress' was given.

    Parameters
    ----------

    address : int
      The address of one part of the C++ object, as the ritual that
      asks C++ for it returned it. It may be the address 'setAddress'
      was given, when the part begins where the object begins.

    Raises
    ------

    TypeException
      'address' is not an 'int'.

    ValueError
      'address' is zero or negative, which is no place in memory.

    MissingVariable
      'setAddress' has not been called on this Ugly.
    """
    if isinstance(address, bool) or not isinstance(address, int):
      raise TypeException('address', address, int)
    if address <= 0:
      infoSpec = """An address is a positive whole number, but received
      %d."""
      raise ValueError(' '.join((infoSpec % address).split()))
    if self.__cpp_address__ is None:
      raise MissingVariable(self, '__cpp_address__', int)
    type(self).__by_address__[address] = self

  def disown(self) -> None:
    """
    Tells this Ugly that Python no longer owns its C++ object. From
    here on the C++ object is left as it is when this Ugly goes.

    The cute side calls this when it hands the address to Qt as an
    address: Qt may keep the object, and may remove it itself. It
    cannot be taken back. On an Ugly whose C++ object Python does not
    own it does nothing.
    """
    if self.__delete_watch__ is not None:
      self.__delete_watch__.detach()
    self.__delete_ritual__ = None

  def call(self, ritualName: str, *args: Any) -> Any:
    """
    Runs one ritual on the C++ object this Ugly stands for.

    Parameters
    ----------

    ritualName : str
      The name of the ritual, as its ritual file has it:
      'ritual_ZNK7QObject6parentEv'.

    *args : Any
      What the ritual takes after the address of the object, which is
      put first for you. Another object is passed as its address, from
      'getAddress', or as 'None' for no object. Text is passed as a
      'str'.

    Returns
    -------

    Any
      What the ritual returns. An address comes back as an 'int', or
      'None' when C++ answered with no object. Text comes back as a
      'str'.

    Raises
    ------

    MissingVariable
      'setAddress' has not been called on this Ugly.

    RuntimeError
      Qt has removed the C++ object, which is known after 'watch'.

    LookupError
      'Rituals' lists no ritual of that name.
    """
    return Rituals.call(ritualName, self.getAddress(), *args)
