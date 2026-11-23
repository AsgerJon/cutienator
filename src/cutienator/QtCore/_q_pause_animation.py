"""
QPauseAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpauseanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractAnimation, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPauseAnimation(QAbstractAnimation):
  """
  The cute side of Qt's QPauseAnimation: a plain Python object standing in
  front of one C++ QPauseAnimation.

  It is built on the cute 'QAbstractAnimation', as Qt's QPauseAnimation is
  built on Qt's QAbstractAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPauseAnimation that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'duration',
  'setDuration', 'event', 'updateCurrentTime'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPauseAnimation::~QPauseAnimation()': the destructor: Python never
    removes a C++ QPauseAnimation.

  What has no ritual
  ------------------

  9 of the 18 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QPauseAnimation is created at the first use, not by
    'QPauseAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPauseAnimation.
  - Qt tells when it has removed the C++ QPauseAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QPauseAnimation::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpauseanimation.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPauseAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QPauseAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPauseAnimation'

  #  A C++ QPauseAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPauseAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPauseAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpauseanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPauseAnimation::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QPauseAnimation10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QPauseAnimation::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpauseanimation.html#duration
    """
    #  int QPauseAnimation::duration() const
    ritual = 'ritual_ZNK15QPauseAnimation8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPauseAnimation8durationEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDuration(self, msecs: int) -> None:
    """
    Calls Qt's 'void QPauseAnimation::setDuration(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpauseanimation.html#setDuration

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QPauseAnimation::setDuration(int msecs)
    self.uglySide.call('ritual_ZN15QPauseAnimation11setDurationEi', msecs)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QPauseAnimation::QPauseAnimation(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpauseanimation.html#QPauseAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPauseAnimation::QPauseAnimation(QObject *parent)
    self._noteCreation(QPauseAnimation, lambda: Rituals.call(
        'ritual_ZN15QPauseAnimationC1EP7QObject', self._addressOf(parent),
    ))

  @overload(int)
  @overload(int, QObject)
  @overload(int, NoneType)
  def __init__(self, msecs: int, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QPauseAnimation::QPauseAnimation(int
    msecs, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpauseanimation.html#QPauseAnimation

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPauseAnimation::QPauseAnimation(int msecs, QObject *parent)
    self._noteCreation(QPauseAnimation, lambda: Rituals.call(
        'ritual_ZN15QPauseAnimationC1EiP7QObject',
        msecs, self._addressOf(parent),
    ))

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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QPauseAnimation::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qpauseanimation.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPauseAnimation::event(QEvent *e)
    ritual = 'ritual_ZN15QPauseAnimation5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPauseAnimation5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(int)
  def updateCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QPauseAnimation::updateCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpauseanimation.html#updateCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QPauseAnimation::updateCurrentTime(int a0)
    ritual = 'ritual_ZN15QPauseAnimation17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPauseAnimation17updateCurrentTimeEi'
    self.uglySide.call(ritual, a0)
