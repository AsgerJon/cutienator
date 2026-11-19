"""
CuteMixin provides shape
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.desc import Field
from worktoy.mcls import BaseObject

from ..occult import Rituals, Ugly

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional, Any, Callable, Tuple


class CuteMixin(BaseObject):
  """
  CuteMixin provides shape
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _addressOf(cuteSide: Optional[Any]) -> Optional[int]:
    """
    Gives what a ritual takes in the place of a cute object that Qt
    takes by its address, as 'QObject *parent': the address of the C++
    object it stands for, or None for None, which C++ reads as no
    object. Asking makes the C++ object if it is not made yet.

    Qt may keep an object it is handed by its address, and may remove
    it. So a C++ object that Python owned until now is Python's no
    more: it is never removed by Python after this. See 'Ugly.disown'.
    """
    if cuteSide is None:
      return None
    uglySide = cuteSide.uglySide
    uglySide.disown()
    return uglySide.getAddress()

  @staticmethod
  def _valueOf(cuteSide: Any) -> int:
    """
    Gives what a ritual takes in the place of a cute object that Qt
    takes as a value, as 'const QSize &size': the address of the C++
    object it stands for. Asking makes the C++ object if it is not made
    yet.

    Qt copies a value it wants to keep, and knows nothing of the one it
    was handed once the ritual has run. So Python goes on owning its
    C++ object, and no None is taken: there is no such thing as no
    value.
    """
    return cuteSide.uglySide.getAddress()

  @staticmethod
  def _bytesOf(text: Optional[str]) -> Optional[bytes]:
    """
    Gives what a ritual takes in the place of text: the text as bytes,
    or None for None, which C++ reads as no text.
    """
    if text is None:
      return None
    return text.encode()

  @staticmethod
  def _startTextsOf(texts: list) -> Tuple[int, int]:
    """
    Gives what a ritual takes in the place of the texts a program was
    started with, as 'sys.argv': where their count is kept, and where
    the first of them is. Qt reads both for as long as its application
    lives, so 'Rituals' keeps them for as long as Python runs.
    """
    return Rituals.keepStartTexts(texts)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The ritual removing a C++ object of the class, in a class whose C++
  #  objects are values: Python then owns each one it makes, and each
  #  copy a ritual hands it. None in every other class, whose C++
  #  objects Python never removes.
  __delete_ritual__: Optional[str] = None
  #  Whether a C++ object of the class is a QObject, which Qt can watch
  #  and tell the removal of. True in the cute QObject and so in every
  #  class built on it.
  __watched_by_qt__: bool = False

  #  Fallback Variables

  #  Private Variables
  __ugly_side__: Optional[object] = None
  #  What makes the C++ object, noted by the '__init__' that was called
  #  and kept until the first use. None when nothing was noted.
  __creation_call__: Optional[Callable] = None

  #  Public Variables
  uglySide: Field[object] = Field()

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _noteCreation(self, cuteClass: type, creationCall: Callable) -> None:
    """
    Notes what makes the C++ object, until the first use. Every
    '__init__' that a program wrote for a constructor of Qt ends with
    this.

    A cute class has the '__init__' functions of the class it is built
    on as well, and those make the C++ object of that class. A
    'QThread' made as a 'QObject' is made would stand in front of a C++
    object that is no QThread, so such a call is refused here.

    Parameters
    ----------

    cuteClass : type
      The cute class whose constructor of Qt was chosen.

    creationCall : Callable
      Called with nothing at the first use. It gives the address of the
      new C++ object.

    Raises
    ------

    TypeError
      The object is of a cute class standing for another class of Qt
      than 'cuteClass'.
    """
    for cls in type(self).__mro__:
      if '__qt_class__' in cls.__dict__:
        break
    else:
      cls = cuteClass
    if cls is not cuteClass:
      infoSpec = """A '%s' cannot be made with what a '%s' is made
      with: Qt's %s has no such constructor that Python can call."""
      info = infoSpec % (cls.__name__, cuteClass.__name__, cls.__name__)
      raise TypeError(' '.join(info.split()))
    self.__creation_call__ = creationCall

  def _createUglySide(self, ) -> None:
    """
    Creates the C++ object and the Ugly standing for it, by what the
    '__init__' that was called noted.

    'uglySide' calls this at its first read. In a value class the Ugly
    removes the C++ object when it goes itself. In a class that is a
    QObject, Qt watches the C++ object from here on.

    Raises
    ------

    TypeError
      Nothing was noted: the class has no constructor of Qt that Python
      can call.
    """
    creationCall = self.__creation_call__
    if creationCall is None:
      infoSpec = """A '%s' cannot be made from Python: no ritual makes
      one. One is given by a function of another class."""
      info = infoSpec % type(self).__name__
      raise TypeError(' '.join(info.split()))
    ugly = Ugly()
    ugly.setAddress(creationCall())
    if self.__delete_ritual__ is not None:
      ugly.setDeleteRitual(self.__delete_ritual__)
    if self.__watched_by_qt__:
      ugly.watch()
    ugly.setCuteSide(self)
    self.__ugly_side__ = ugly
    self.__creation_call__ = None

  @uglySide.GET
  def _getUglySide(self, **kwargs) -> object:
    if self.__ugly_side__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createUglySide()
      return self._getUglySide(_recursion=True)
    return self.__ugly_side__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _cuteAt(cls, address: Optional[int]) -> Optional[Any]:
    """
    Gives the cute object standing for the C++ object at an address
    that a ritual gave back. A cute function giving an object back ends
    with this:

      address = self.uglySide.call('ritual_ZNK7QObject6threadEv')
      return QThread._cuteAt(address)

    What comes back
    ---------------

    - None, when the address is None: C++ answered with no object.
    - The cute object that stands for that C++ object already, when
      there is one. It is given as it is, whatever class it has.
    - Otherwise a new object of the class this is called on, made
      around the address. No C++ object is created for it, and its
      '__init__' does not run: it stands for an object C++ made itself,
      as the thread Python runs in. In a class that is a QObject, Qt
      watches the C++ object from here on; see 'Ugly.watch'.

    Nothing keeps a cute object made here alive but the one who asked
    for it. Asked again after it is gone, a new one is made.

    Parameters
    ----------

    address : Optional[int]
      What the ritual gave back: an address, or None.

    Returns
    -------

    Optional[Any]
      A cute object, or None.
    """
    if address is None:
      return None
    try:
      return Ugly.at(address).getCuteSide()
    except LookupError:
      pass
    cuteSide = cls.__new__(cls)
    ugly = Ugly()
    ugly.setAddress(address)
    if cls.__watched_by_qt__:
      ugly.watch()
    ugly.setCuteSide(cuteSide)
    cuteSide.__ugly_side__ = ugly
    return cuteSide

  @classmethod
  def _cuteOwning(cls, address: int) -> Any:
    """
    Gives a new cute object around a C++ object that a ritual has just
    made as a copy for Python. A cute function giving a value back ends
    with this:

      address = self.uglySide.call('ritual_ZNK5QSize10transposedEv')
      return QSize._cuteOwning(address)

    What comes back
    ---------------

    A new object of the class this is called on, made around the
    address. Its '__init__' does not run. Python owns the C++ object:
    it is removed when the cute object goes, by the ritual the class
    names in '__delete_ritual__', and it is not removed as the program
    ends.

    Parameters
    ----------

    address : int
      What the ritual gave back: where the copy is.

    Returns
    -------

    Any
      The cute object.

    Raises
    ------

    TypeError
      The class names no '__delete_ritual__': its C++ objects are no
      values, and Python owns none of them.
    """
    if cls.__delete_ritual__ is None:
      infoSpec = """'%s' names no '__delete_ritual__', so Python owns no
      C++ object of it. An object Qt hands out by its address is given
      to '_cuteAt'."""
      raise TypeError(' '.join((infoSpec % cls.__name__).split()))
    cuteSide = cls.__new__(cls)
    ugly = Ugly()
    ugly.setAddress(address)
    ugly.setDeleteRitual(cls.__delete_ritual__)
    ugly.setCuteSide(cuteSide)
    cuteSide.__ugly_side__ = ugly
    return cuteSide

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
