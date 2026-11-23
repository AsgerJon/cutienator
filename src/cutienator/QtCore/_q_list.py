"""
QList stands for the lists of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Iterator, Optional


class QList(CuteMixin, metaclass=MetaCute):
  """
  The lists of Qt. Qt has one class of list for each thing a list can
  hold, and so has cutienator: 'QList[QUrl]' is the class of the lists
  of QUrl, which C++ writes 'QList<QUrl>'.

    urls = QList[QUrl]([QUrl('a'), QUrl('b')])
    len(urls), urls[0]
    for url in urls: ...
    urls.append(QUrl('c'))

  This file is written by hand: Qt's QList is a pattern for classes and
  no class the dev tooling reads.

  Terms
  -----

  - A kind is one class of list: the lists of QUrl are one kind, the
    lists of QAction another. C++ has compiled code for the kinds its
    own functions hand around, and for no others.
  - The class of a kind is a cute class built on this one, standing in
    front of one C++ list of that kind.

  Where the kinds come from
  -------------------------

  - The class of a kind that holds a class of Qt is completed at the
    end of the file of that class, by 'createKind': there it learns
    its class and its rituals. It is made there as well, unless a
    class body named it before, as 'QList[QUrl]' with QUrl still a
    'WAIT'; then it was made on that line, by the name alone.
  - The list of text is 'QStringList', as Qt names it, in a file of its
    own. 'QList[str]' is that class.
  - Qt has names of its own for a few more kinds, as 'QModelIndexList'
    for 'QList[QModelIndex]'. Each is a second name for the same class.

  What to expect
  --------------

  - A list holds its own kind and nothing else. An element of another
    class is refused with 'TypeError', on the line that hands it over.
  - 'QList[...]' with something Qt has no list of raises 'TypeError'.
  - A function of Qt that takes a list takes a list or tuple of Python
    as well: the list of Qt is made from it, every element checked,
    and the call is refused when one does not fit.
  - A function of Qt that gives a list gives an object of the class of
    its kind. It reads as a list of Python reads: 'len', '[index]' and
    'for'. It is a copy, which Python owns: changing it changes nothing
    in Qt.
  - A list of objects Qt hands out by their address, as
    'QList[QAction]', holds the addresses. The objects have to be kept
    for as long as the list is used, as anywhere else.
  - A list never waits for what it holds. In the body of a class
    whose file does not bring in QUrl, 'QList[QUrl]' is the class of
    that kind all the same, named after the class it will hold. The
    first time it needs that class, to make a C++ list or to hand out
    an element, it brings the file of the class in itself. So an empty
    list goes through a function that takes a list of QUrl whether or
    not the program ever made a QUrl.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  In the class of a kind: the name of the class a list of the kind
  #  holds, as 'QUrl'; that class, once its file is brought in; how one
  #  element crosses to C++ ('value', 'address' or 'text'); and the
  #  rituals of the list, under 'make', 'add', 'size', 'at' and 'drop'.
  #  None in 'QList' itself.
  __element_name__: Optional[str] = None
  __element_class__: Optional[type] = None
  __element_crossing__: Optional[str] = None
  __list_rituals__: Optional[Dict[str, str]] = None
  #  On 'QList' itself: the class of each kind collected so far, under
  #  the name of what the kind holds.
  __list_kinds__: Optional[Dict[str, type]] = None
  #  The kinds that hold no class of Qt, each under the name of what it
  #  holds, with the name it has in QtCore. They are brought in when
  #  asked for.
  __plain_kinds__ = {'str': 'QStringList'}

  #  Fallback Variables

  #  Private Variables
  #  What a list was made of, kept until its C++ list is made.
  __kept_elements__: Optional[list] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _getKinds(cls) -> Dict[str, type]:
    """Gives the classes of the kinds collected so far, each under the
    name of what it holds. Kept on 'QList' itself, since a program has
    one such table."""
    if QList.__list_kinds__ is None:
      type.__setattr__(QList, '__list_kinds__', dict())
    return QList.__list_kinds__

  @classmethod
  def _getKind(cls) -> type:
    """
    Gives the class of the kind a class of lists is of: the class
    itself, or the class of a kind it is built on.

    Raises
    ------

    TypeError
      The class is 'QList' itself, which is of no kind.
    """
    for one in cls.__mro__:
      if one.__dict__.get('__element_name__', None) is not None:
        return one
    infoSpec = """A list is of one kind, as QList[QUrl]([...]). 'QList'
    alone says nothing of what the list holds."""
    raise TypeError(' '.join(infoSpec.split()))

  @classmethod
  def _getMadeKind(cls) -> type:
    """
    Gives the class of the kind a class of lists is of, completed: it
    knows the class it holds and its rituals.

    A kind a class body named before the class it holds was brought in
    knows only the name of that class. The file of the class is brought
    in here, and ends with 'createKind', which completes the kind.

    Raises
    ------

    TypeError
      The class is 'QList' itself. Or no part of Qt has a class of the
      name, or its file completes no such kind: Qt has no list of it.
    """
    kind = cls._getKind()
    if kind.__element_class__ is None:
      name = kind.__element_name__
      for partName in Rituals.getComponents():
        package = importlib.import_module('..%s' % partName, __package__)
        if name in package.__class_files__:
          getattr(package, name)
          break
    if kind.__element_class__ is None:
      infoSpec = """Qt has no list of '%s' that cutienator knows."""
      raise TypeError(infoSpec % kind.__element_name__)
    return kind

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def __class_getitem__(cls, element: Any) -> Any:
    """
    Gives the class of the lists of one kind: 'QList[QUrl]'.

    Parameters
    ----------

    element : Any
      What the lists hold: a cute class, or 'str' for text. Or a
      'WAIT' for a class that is not brought in yet: the class of the
      kind is then given by the name alone, and completed later.

    Raises
    ------

    TypeError
      Qt has no list of 'element' that cutienator knows, or the class
      subscripted is the class of a kind already.
    """
    if cls is not QList:
      infoSpec = """'%s' is the class of one kind of list already."""
      raise TypeError(infoSpec % cls.__name__)
    late = isinstance(element, WAIT)
    if late:
      name = element.getWaitingName()
    else:
      name = getattr(element, '__name__', None)
    infoSpec = """Qt has no list of '%s' that cutienator knows."""
    if not isinstance(name, str) or not (late or isinstance(element, type)):
      raise TypeError(infoSpec % (element,))
    kinds = cls._getKinds()
    if name not in kinds and name in cls.__plain_kinds__:
      package = importlib.import_module('..QtCore', __package__)
      getattr(package, cls.__plain_kinds__[name])
    if name not in kinds and late:
      kinds[name] = cls._createNamedKind(name)
    try:
      kind = kinds[name]
    except KeyError:
      raise TypeError(infoSpec % name) from None
    if not late and kind.__element_class__ is not element:
      #  Another class of the same name, as one of a program.
      raise TypeError(infoSpec % name)
    return kind

  @classmethod
  def __cast_as__(cls, value: Any) -> Any:
    """
    Says what a signature naming one kind of list takes in the place of
    a list of that kind: a list or tuple of Python whose every element
    fits. worktoy asks this when a call hands a function something else
    than a list of the kind.

    Returns
    -------

    Any
      A new list of the kind made of the elements, or 'NotImplemented'
      for anything else, and for a list or tuple with an element the
      kind does not hold.
    """
    if cls.__element_name__ is None:
      return NotImplemented
    if not isinstance(value, (list, tuple)):
      return NotImplemented
    try:
      return cls(value)
    except TypeError:
      return NotImplemented

  def __len__(self) -> int:
    """Gives how many elements the list holds."""
    return self.size()

  def __getitem__(self, index: int) -> Any:
    """Gives the element at a place, counted from the end for a
    negative one."""
    if isinstance(index, int) and index < 0:
      index += self.size()
    return self.at(index)

  def __iter__(self) -> Iterator:
    """Gives the elements, the first first."""
    for index in range(self.size()):
      yield self.at(index)

  def __str__(self) -> str:
    """Shows the list as it is made: its kind and its elements."""
    shown = ', '.join(str(element) for element in self)
    return '%s([%s])' % (self._getKind().__name__, shown)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _createNamedKind(cls, name: str) -> type:
    """Makes the class of the lists of one kind by the name of the
    class it holds alone. 'createKind' completes it."""
    space = dict(__qt_class__='QList<%s>' % name, __element_name__=name)
    return type(cls)('QList[%s]' % name, (cls,), space)

  @classmethod
  def createKind(
      cls,
      element: type,
      crossing: str,
      name: Optional[str] = None,
      **rituals: str,
  ) -> type:
    """
    Completes the class of the lists of one kind, making it first when
    no class body named it yet. The class files the dev tooling writes
    call this at their end, for a class some list of Qt holds.

    Parameters
    ----------

    element : type
      The cute class the lists hold.

    crossing : str
      How one element crosses to C++: 'value' for a copy, 'address' for
      the address of an object.

    name : Optional[str]
      The name Qt has for the kind, as 'QModelIndexList'. Without one
      the class is named as it is asked for: 'QList[QUrl]'.

    **rituals : str
      The rituals of the list: 'make', 'add', 'size', 'at' and 'drop'.

    Returns
    -------

    type
      The class of the kind, which 'QList[element]' gives.
    """
    kinds = cls._getKinds()
    try:
      kind = kinds[element.__name__]
    except KeyError:
      kind = cls._createNamedKind(element.__name__)
      kinds[element.__name__] = kind
    type.__setattr__(kind, '__element_class__', element)
    type.__setattr__(kind, '__element_crossing__', crossing)
    type.__setattr__(kind, '__list_rituals__', rituals)
    type.__setattr__(kind, '__delete_ritual__', rituals['drop'])
    if name is not None:
      type.__setattr__(kind, '__name__', name)
      type.__setattr__(kind, '__qualname__', name)
    return kind

  @classmethod
  def collect(cls, kind: type) -> type:
    """Collects the class of a kind written by hand, as 'QStringList',
    under the name of what it holds, and gives it back."""
    cls._getKinds()[kind.__element_name__] = kind
    return kind

  @classmethod
  def _cuteOwning(cls, address: int) -> Any:
    """Gives a new list around a C++ list a ritual made for Python, as
    'CuteMixin._cuteOwning' does, completing the kind first if need
    be."""
    cls._getMadeKind()
    return super()._cuteOwning(address)

  @overload()
  def __init__(self) -> None:
    """Makes an empty list. The C++ list is made at the first use."""
    kind = self._getMadeKind()
    make = kind.__list_rituals__['make']
    self._noteCreation(kind, lambda: Rituals.call(make))

  @overload(list)
  @overload(tuple)
  def __init__(self, elements: Any) -> None:
    """
    Makes a list of the elements of a list or tuple of Python. Each is
    checked here, on the line that makes the list. The C++ list is made
    at the first use.

    Raises
    ------

    TypeError
      An element is not of what the kind holds.
    """
    kind = self._getMadeKind()
    rituals = kind.__list_rituals__
    handed = [self._handOver(element) for element in elements]

    def create() -> int:
      """Makes the C++ list and adds each element."""
      address = Rituals.call(rituals['make'])
      for one in handed:
        Rituals.call(rituals['add'], address, one)
      self.__kept_elements__ = None
      return address

    #  What was handed over for an element is the address of its C++
    #  object, so the elements are kept until the C++ list is made.
    self.__kept_elements__ = [*elements]
    self._noteCreation(kind, create)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _handOver(self, element: Any) -> Any:
    """
    Turns an element into what the rituals of the list take in its
    place, and refuses one the kind does not hold.

    Raises
    ------

    TypeError
      The element is not of what the kind holds.
    """
    kind = self._getMadeKind()
    wanted, crossing = kind.__element_class__, kind.__element_crossing__
    if not isinstance(element, wanted):
      infoSpec = """A '%s' holds '%s' and nothing else, but was handed
      '%s'."""
      info = infoSpec % (
          kind.__name__, wanted.__name__, type(element).__name__)
      raise TypeError(' '.join(info.split()))
    if crossing == 'value':
      return CuteMixin._valueOf(element)
    if crossing == 'address':
      return CuteMixin._addressOf(element)
    return element

  def _takeBack(self, given: Any) -> Any:
    """Turns what a ritual of the list gives for an element into the
    element: a new cute object around a copy, the cute object standing
    for an address, or the text itself."""
    kind = self._getMadeKind()
    wanted, crossing = kind.__element_class__, kind.__element_crossing__
    if crossing == 'value':
      return wanted._cuteOwning(given)
    if crossing == 'address':
      return wanted._cuteAt(given)
    return given

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

  def size(self) -> int:
    """Calls Qt's 'qsizetype QList::size() const'."""
    return self.uglySide.call(self._getMadeKind().__list_rituals__['size'])

  def at(self, index: int) -> Any:
    """
    Calls Qt's 'const T &QList::at(qsizetype i) const'.

    Qt ends the program for a place the list does not have, so such a
    place is refused here.

    Raises
    ------

    TypeError
      'index' is not an 'int'.

    IndexError
      The list has no such place.
    """
    if isinstance(index, bool) or not isinstance(index, int):
      infoSpec = """A place in a list is an 'int', but received '%s'."""
      raise TypeError(infoSpec % type(index).__name__)
    size = self.size()
    if not 0 <= index < size:
      infoSpec = """The list has %d elements and no place %d."""
      raise IndexError(infoSpec % (size, index))
    ritual = self._getMadeKind().__list_rituals__['at']
    return self._takeBack(self.uglySide.call(ritual, index))

  def append(self, element: Any) -> None:
    """
    Calls Qt's 'void QList::append(const T &value)'.

    Raises
    ------

    TypeError
      The element is not of what the kind holds.
    """
    ritual = self._getMadeKind().__list_rituals__['add']
    self.uglySide.call(ritual, self._handOver(element))
