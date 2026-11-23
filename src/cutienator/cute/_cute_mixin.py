"""
CuteMixin provides shape
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
import importlib
from typing import TYPE_CHECKING

from worktoy.desc import Field
from worktoy.dispatch import Dispatcher
from worktoy.mcls import BaseObject, BaseSpace

from ..occult import Rituals, Ugly

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional, Any, Callable, Dict, Tuple


class CuteMixin(BaseObject):
  """
  CuteMixin provides shape
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _addressOf(
      cuteSide: Optional[Any],
      qtClass: Optional[str] = None,
  ) -> Optional[int]:
    """
    Gives what a ritual takes in the place of a cute object that Qt
    takes by its address, as 'QObject *parent': the address of the C++
    object it stands for, or None for None, which C++ reads as no
    object. Asking makes the C++ object if it is not made yet.

    Where Qt takes a class that other classes are built on beside
    another, as 'QPaintDevice *', the class of Qt is named, and the
    address is that of the part of the object belonging to it; see
    '_addressAs'.

    Qt may keep an object it is handed by its address, and may remove
    it. So a C++ object that Python owned until now is Python's no
    more: it is never removed by Python after this. See 'Ugly.disown'.
    """
    if cuteSide is None:
      return None
    uglySide = cuteSide.uglySide
    uglySide.disown()
    if qtClass is None:
      return uglySide.getAddress()
    return cuteSide._addressAs(qtClass)

  @staticmethod
  def _valueOf(cuteSide: Any, qtClass: Optional[str] = None) -> int:
    """
    Gives what a ritual takes in the place of a cute object that Qt
    takes as a value, as 'const QSize &size': the address of the C++
    object it stands for. Asking makes the C++ object if it is not made
    yet.

    Qt copies a value it wants to keep, and knows nothing of the one it
    was handed once the ritual has run. So Python goes on owning its
    C++ object, and no None is taken: there is no such thing as no
    value. A class of Qt is named as for '_addressOf'.
    """
    if qtClass is None:
      return cuteSide.uglySide.getAddress()
    return cuteSide._addressAs(qtClass)

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

  @staticmethod
  def _findNamed(where: str) -> Any:
    """
    Gives the cute class or enum found at a place written as
    'QtGui:QPaintEvent' or 'QtCore:Qt.FocusPolicy': the part of Qt,
    and then the names leading to it. The part is brought in if it is
    not yet. The tables '__virtual_functions__' name classes that way,
    since a class file cannot bring in every class its functions are
    handed.
    """
    partName, _, dotted = where.partition(':')
    found = importlib.import_module('..%s' % partName, __package__)
    for word in dotted.split('.'):
      found = getattr(found, word)
    return found

  @staticmethod
  def _wroteItself(programClass: type, name: str) -> bool:
    """
    Says whether a class wrote a function of a name itself, in its body
    or put on it afterwards.

    That the name is in the class does not say so: worktoy gives every
    class a dispatcher of its own for each overloaded name it inherits.
    So an overloaded name counts when the namespace of the class has
    overloads of its own on record for it, and any other name when the
    class holds it.
    """
    try:
      held = programClass.__dict__[name]
    except KeyError:
      return False
    if not isinstance(held, Dispatcher):
      return True
    space = programClass.__dict__.get('__namespace__', None)
    if not isinstance(space, BaseSpace):
      return True
    return space.hasOverloads(name)

  @staticmethod
  def _cuteOfHanded(how: str, where: str, handed: Any) -> Any:
    """
    Turns one thing C++ hands a Python function into what the cute
    function takes in that place.

    Parameters
    ----------

    how : str
      What it is: 'number', 'text', 'enum', 'flags', 'address' or
      'value'.

    where : str
      Where its cute class or enum is found, as '_findNamed' reads it.
      Empty for a number and for text.

    handed : Any
      What C++ handed over: the number, the address of Qt's text, the
      number of the member or of the flags, or the address of the C++
      object.

    Returns
    -------

    Any
      The number itself, the text as a 'str', the member of the enum,
      the value of the flags, or the cute object standing for the C++
      object, None for no object. C++ says which
      class the object is of, so a cute object of another class found
      at the address stood for an object that was there before, and a
      new one is made: Qt hands one event first as a 'QEvent' and then
      as a 'QResizeEvent', and makes its events in places it uses over
      and over.
    """
    if how == 'number':
      return handed
    if how == 'text':
      return Rituals.takeText(handed)
    wanted = CuteMixin._findNamed(where)
    if how in ('enum', 'flags'):
      return wanted(handed)
    found = wanted._cuteAt(handed)
    if found is None or isinstance(found, wanted):
      return found
    return wanted._cuteAnew(handed)

  @staticmethod
  def _handBack(name: str, gives: Tuple[str, str, str], given: Any) -> Any:
    """
    Turns what a Python function called by Qt gave back into what C++
    takes back.

    Parameters
    ----------

    name : str
      The name of the function, as 'sizeHint', for the message.

    gives : Tuple[str, str, str]
      What Qt's function gives: the word of it as a row has it, what
      it is ('nothing', 'number', 'text', 'enum', 'flags', 'address'
      or 'value'), and where its cute class or enum is found.

    given : Any
      What the Python function gave back.

    Returns
    -------

    Any
      None for a function giving nothing, whatever the Python function
      gave. Else the number, the address of a text of Qt made from the
      'str', the number of the member or of the flags, or the address
      of the C++ object.

    Raises
    ------

    TypeError
      The Python function gave something else than Qt's function
      gives, as None where Qt's gives a 'bool'.
    """
    word, how, where = gives
    if how == 'nothing':
      return None
    if how == 'number':
      if word == 'bool':
        wanted = bool
      elif word in ('float', 'double'):
        wanted = float
      else:
        wanted = int
      fits = isinstance(given, (int, float) if wanted is float else wanted)
    elif how == 'text':
      wanted, fits = str, isinstance(given, str)
    else:
      wanted = CuteMixin._findNamed(where)
      fits = isinstance(given, wanted)
      if how == 'address' and given is None:
        fits = True
    if not fits:
      infoSpec = """'%s' has to give '%s', as Qt's own does, but gave
      '%s'."""
      info = infoSpec % (name, wanted.__name__, type(given).__name__)
      raise TypeError(' '.join(info.split()))
    if how == 'number':
      return given
    if how == 'text':
      return Rituals.giveText(given)
    if how in ('enum', 'flags'):
      return given.value
    if how == 'value':
      Rituals.keepGiven(given)
      return CuteMixin._valueOf(given)
    return CuteMixin._addressOf(given)

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
  #  In a class whose class of Qt is built on more than one class: for
  #  each class of Qt after the first, the ritual that gives where the
  #  part of an object belonging to it is. None in every other class.
  #  See '_addressAs'.
  __cast_rituals__: Optional[Dict[str, str]] = None
  #  In a class of Qt that has functions Qt calls itself, as
  #  'paintEvent': the ritual that hands an object of the class a
  #  Python function for one of them. A C++ object Python makes of such
  #  a class is of a C++ class of ours, built on the class of Qt. None
  #  in every other class. See '_takeOver'.
  __take_ritual__: Optional[str] = None
  #  The functions Qt calls itself that the class is the first to
  #  declare, and that a class of a program built on it may write anew.
  #  For each name, each function of that name: the key C++ knows it
  #  by, what it gives, and what it takes. None in every other class.
  __virtual_functions__: Optional[Dict[str, Any]] = None
  #  The functions Qt calls itself that the class is the first to
  #  declare and that cannot be handed to Python yet: for each name,
  #  each function of that name as Qt declares it. A class of a program
  #  that writes one anew is refused. None in every other class.
  __virtual_left_out__: Optional[Dict[str, Any]] = None

  #  Fallback Variables

  #  Private Variables
  __ugly_side__: Optional[object] = None
  #  What makes the C++ object, noted by the '__init__' that was called
  #  and kept until the first use. None when nothing was noted.
  __creation_call__: Optional[Callable] = None
  #  In a class of a program that wrote a function Qt calls itself: the
  #  function of C made for each, under its key. C++ holds the address
  #  of each alone, so they are kept for as long as the class lives.
  __taken_calls__: Optional[Dict[str, Any]] = None

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

  def _findCast(self, qtClass: str) -> Optional[str]:
    """
    Gives the ritual that leads from the address of the C++ object to
    the address of its part belonging to a class of Qt, or None when
    that part begins where the object begins.

    A class of Qt may be built on more than one class, as QWidget on
    QObject and QPaintDevice. An object of it holds a part for each.
    The part of the first begins where the object begins, and so do
    the parts of what that one is built on first, all the way up. The
    part of a further class begins somewhere inside the object, and
    C++ has to be asked where: the cute class names a ritual for each
    such class in '__cast_rituals__'. The part of a class that further
    class is built on begins where it begins.
    """
    for cuteClass in type(self).__mro__:
      casts = cuteClass.__dict__.get('__cast_rituals__', None)
      if not casts:
        continue
      for baseName, ritualName in casts.items():
        for baseClass in cuteClass.__mro__:
          if baseClass.__dict__.get('__qt_class__', None) == baseName:
            break
        else:
          continue
        for partClass in baseClass.__mro__:
          if partClass.__dict__.get('__qt_class__', None) == qtClass:
            return ritualName
    return None

  def _addressAs(self, qtClass: str) -> int:
    """
    Gives the address of the part of the C++ object that belongs to one
    class of Qt the object is built on, as 'QPaintDevice' for a
    QWidget. A function of that class of Qt has to be handed this
    address, and not the address of the object.

    Parameters
    ----------

    qtClass : str
      The class of Qt, as Qt names it: 'QPaintDevice'.

    Returns
    -------

    int
      The address of that part. It is the address of the object for a
      class the object is built on first, all the way up.
    """
    address = self.uglySide.getAddress()
    ritualName = self._findCast(qtClass)
    if ritualName is None:
      return address
    return Rituals.call(ritualName, address)

  def _callAs(self, qtClass: str, ritualName: str, *args: Any) -> Any:
    """
    Runs a ritual of one class of Qt on the C++ object, handing it the
    address of the part of the object that belongs to that class. A
    function of a class that others are built on beside another calls
    its ritual this way, as the functions of QPaintDevice do, since the
    object may be a QWidget.

    Parameters
    ----------

    qtClass : str
      The class of Qt the ritual belongs to: 'QPaintDevice'.

    ritualName : str
      The ritual.

    *args : Any
      What the ritual takes after the address.
    """
    return Rituals.call(ritualName, self._addressAs(qtClass), *args)

  def _notePartAddresses(self, ugly: Any) -> None:
    """
    Tells the Ugly of this object the address of each part of the C++
    object that begins somewhere inside it, so that an address C++
    hands out for such a part leads back to this cute object.
    """
    address = ugly.getAddress()
    for cuteClass in type(self).__mro__:
      casts = cuteClass.__dict__.get('__cast_rituals__', None)
      for ritualName in (casts or dict()).values():
        ugly.addPartAddress(Rituals.call(ritualName, address))

  def _findWritten(self) -> Tuple[Tuple[type, ...], Optional[type]]:
    """
    Tells the classes of a program in the class of this object from
    the cute classes the dev tooling wrote.

    Returns
    -------

    Tuple[Tuple[type, ...], Optional[type]]
      The classes of the program the object is of, the nearest first,
      and the nearest class the dev tooling wrote, which they are built
      on. No class of a program for an object of such a class itself,
      as a plain 'QWidget'. None in the second place when the object
      is of no class of Qt.
    """
    order = type(self).__mro__
    for place, cuteClass in enumerate(order):
      if '__qt_class__' in cuteClass.__dict__:
        return order[:place], cuteClass
    return order, None

  def _refuseLeftOut(self) -> None:
    """
    Refuses to make the object when a class of the program wrote a
    function Qt calls itself that cannot be handed to Python yet, as
    one taking text. '_createUglySide' calls this before the C++ object
    is made.

    Python would call the function the program wrote, and Qt would go
    on calling its own. So it is refused, loudly, where it would
    otherwise be wrong quietly.

    Raises
    ------

    NotImplementedError
      A class of the program wrote such a function. The message names
      the class and the function, as Qt declares it.
    """
    written, generated = self._findWritten()
    if not written or generated is None:
      return
    for holder in generated.__mro__:
      leftOut = holder.__dict__.get('__virtual_left_out__', None)
      for name, declarations in (leftOut or dict()).items():
        for programClass in written:
          if not self._wroteItself(programClass, name):
            continue
          infoSpec = """'%s' writes '%s' anew, a function Qt calls
          itself: %s. cutienator cannot hand that one to Python yet, so
          Qt would never call what '%s' wrote."""
          info = infoSpec % (
              programClass.__name__, name, '; '.join(declarations),
              programClass.__name__,
          )
          raise NotImplementedError(' '.join(info.split()))

  def _takeOver(self, ugly: Any) -> None:
    """
    Hands C++ a Python function for each function of Qt that a class
    of the program wrote anew, as 'paintEvent' in a class built on
    QWidget. '_createUglySide' calls this when the C++ object is made.

    Qt calls such a function itself, from C++. The C++ object Python
    made is of a C++ class of ours, in which each such function asks
    the Python function handed over for it, and runs Qt's own when
    none was. Only the functions a class of the program really wrote
    are handed over, so every other one costs nothing. It is settled
    here, once, for the life of the object.

    Parameters
    ----------

    ugly : Any
      The Ugly of the C++ object just made.

    Raises
    ------

    TypeError
      A class of the program wrote a function Qt calls itself, and the
      C++ class of ours takes no Python function for it: Qt keeps that
      function to itself in the class of Qt the program built on.
    """
    written, generated = self._findWritten()
    if generated is None:
      return
    takeRitual = generated.__dict__.get('__take_ritual__', None)
    if takeRitual is None:
      return
    ugly.setOurs()
    address = ugly.getAddress()
    for holder in generated.__mro__:
      table = holder.__dict__.get('__virtual_functions__', None)
      for name, variants in (table or dict()).items():
        if not any(self._wroteItself(one, name) for one in written):
          continue
        for key, gives, takes in variants:
          call = self._getTakenCall(key, name, gives, takes)
          handed = ctypes.cast(call, ctypes.c_void_p).value
          if Rituals.call(takeRitual, address, key.encode(), handed):
            continue
          infoSpec = """'%s' writes '%s' anew, a function Qt calls
          itself, and the C++ class behind '%s' takes no Python
          function for it, so Qt would never call what was written."""
          info = infoSpec % (type(self).__name__, name, generated.__name__)
          raise TypeError(' '.join(info.split()))

  def _createUglySide(self, ) -> None:
    """
    Creates the C++ object and the Ugly standing for it, by what the
    '__init__' that was called noted.

    'uglySide' calls this at its first read. In a value class the Ugly
    removes the C++ object when it goes itself. In a class that is a
    QObject, Qt watches the C++ object from here on. For an object of
    a class of a program, each function Qt calls itself that the
    program wrote anew is handed to C++; see '_takeOver'.

    Raises
    ------

    TypeError
      Nothing was noted: the class has no constructor of Qt that Python
      can call. Or a class of the program wrote a function that the C++
      class takes no Python function for; see '_takeOver'.

    NotImplementedError
      A class of the program wrote a function Qt calls itself that
      cannot be handed to Python yet; see '_refuseLeftOut'.
    """
    creationCall = self.__creation_call__
    if creationCall is None:
      infoSpec = """A '%s' cannot be made from Python: no ritual makes
      one. One is given by a function of another class."""
      info = infoSpec % type(self).__name__
      raise TypeError(' '.join(info.split()))
    self._refuseLeftOut()
    ugly = Ugly()
    ugly.setAddress(creationCall())
    if self.__delete_ritual__ is not None:
      ugly.setDeleteRitual(self.__delete_ritual__)
    if self.__watched_by_qt__:
      ugly.watch()
    ugly.setCuteSide(self)
    self._notePartAddresses(ugly)
    self._takeOver(ugly)
    #  Only now is the object made: when a function the program wrote
    #  was refused above, the next use raises the same once more.
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
  def _getTakenCall(
      cls,
      key: str,
      name: str,
      gives: Tuple[str, str, str],
      takes: Tuple[Tuple[str, str, str], ...],
  ) -> Any:
    """
    Gives the function of C that C++ calls in the place of one function
    of Qt this class of a program wrote anew, making it at the first
    asking and keeping it on the class; see '_createTakenCall'.
    """
    kept = cls.__dict__.get('__taken_calls__', None)
    if kept is None:
      kept = dict()
      type.__setattr__(cls, '__taken_calls__', kept)
    try:
      return kept[key]
    except KeyError:
      kept[key] = cls._createTakenCall(name, gives, takes)
      return kept[key]

  @classmethod
  def _createTakenCall(
      cls,
      name: str,
      gives: Tuple[str, str, str],
      takes: Tuple[Tuple[str, str, str], ...],
  ) -> Any:
    """
    Makes the function C++ calls in the place of one function of Qt
    that this class of a program wrote anew, as 'paintEvent'.

    What the function does when Qt calls it
    ---------------------------------------

    1. While an exception is kept that is still to be raised, it takes
       nothing: Qt runs its own function.
    2. It finds the cute object by the address C++ hands it. When
       Python has let go of that object, a 'RuntimeError' is kept: the
       function the program wrote went with the object, and running
       Qt's own in its place would hide that.
    3. It turns each thing handed over into what the cute function of
       that name takes, calls the function of the object by its name,
       and turns what that gives into what C++ takes back.
    4. Whatever is raised on the way is kept by
       'Rituals.keepException', which has it raised where Python was.

    Parameters
    ----------

    name : str
      The name of the function, as 'paintEvent'.

    gives : Tuple[str, str, str]
      What Qt's function gives: the word of it as a row has it, what
      it is ('nothing', 'number', 'text', 'enum', 'flags', 'address'
      or 'value'), and for the last four where its cute class or enum
      is found, as 'QtCore:QSize'.

    takes : Tuple[Tuple[str, str, str], ...]
      The same for each thing Qt's function takes.

    Returns
    -------

    Any
      The function of C, as 'Rituals.createCall' makes it.
    """
    nothing = None if gives[1] == 'nothing' else 0
    className = cls.__name__

    def called(selfAddress: int, *handed: Any) -> Any:
      """Called by C++ with the address of the object, what Qt's
      function takes, and the place to write 1 into for a call taken."""
      wasTaken = handed[-1]
      if Rituals.hasKeptException():
        return nothing
      try:
        cuteSide = Ugly.at(selfAddress).getCuteSide()
      except (LookupError, RuntimeError) as gone:
        infoSpec = """Qt called '%s' of a '%s' that Python has let go
        of. Its C++ object is still there and Qt still uses it, but the
        object the program made is gone, and the '%s' the program wrote
        with it. Keep the object for as long as Qt has it, as an
        attribute of the window it is in."""
        info = infoSpec % (name, className, name)
        error = RuntimeError(' '.join(info.split()))
        error.__cause__ = gone
        Rituals.keepException(error)
        return nothing
      try:
        turned = [
            CuteMixin._cuteOfHanded(how, where, one)
            for (_, how, where), one in zip(takes, handed[:-1])
        ]
        given = getattr(cuteSide, name)(*turned)
        back = CuteMixin._handBack(name, gives, given)
      except BaseException as exception:
        Rituals.keepException(exception)
        return nothing
      wasTaken[0] = 1
      return back

    words = (*(word for word, _, _ in takes),)
    return Rituals.createCall(gives[0], words, called)

  @classmethod
  def _findRealClass(cls, address: int) -> Any:
    """
    Gives the cute class of the C++ class a QObject at an address
    really is, when there is one and it is built on the class this is
    called on, and else the class this is called on.

    Qt hands an object over as the class a function names, as
    'QAbstractItemModel *' for 'QListWidget::model()', while the object
    is of a class built on that one, as 'QListModel'. Every QObject
    says which class it is, through its 'metaObject()'.
    """
    meta = Rituals.call('ritual_ZNK7QObject10metaObjectEv', address)
    name = Rituals.call('ritual_ZNK11QMetaObject9classNameEv', meta)
    name = name.decode('ascii', 'replace')
    if name == cls.__name__:
      return cls
    for partName in Rituals.getQtParts():
      part = importlib.import_module('..%s' % partName, __package__)
      try:
        found = getattr(part, name)
      except AttributeError:
        continue
      if isinstance(found, type) and issubclass(found, cls):
        return found
    return cls

  @classmethod
  def _cuteAnew(cls, address: int) -> Any:
    """
    Gives a new object of the class this is called on, made around the
    address of a C++ object that C++ made itself, whatever cute object
    stood at that address before. No C++ object is created for it, and
    its '__init__' does not run. In a class that is a QObject, Qt
    watches the C++ object from here on; see 'Ugly.watch'.

    '_cuteAt' ends with this when no cute object stands for the C++
    object yet.

    Parameters
    ----------

    address : int
      Where the C++ object is.
    """
    if cls.__watched_by_qt__:
      cls = cls._findRealClass(address)
    cuteSide = cls.__new__(cls)
    ugly = Ugly()
    ugly.setAddress(address)
    if cls.__watched_by_qt__:
      ugly.watch()
    ugly.setCuteSide(cuteSide)
    cuteSide.__ugly_side__ = ugly
    cuteSide._notePartAddresses(ugly)
    return cuteSide

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
    return cls._cuteAnew(address)

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
    cuteSide._notePartAddresses(ugly)
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
