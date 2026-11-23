"""
QSequentialAnimationGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsequentialanimationgroup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractAnimation, QAnimationGroup, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEvent, QMetaObject, QPauseAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSequentialAnimationGroup(QAnimationGroup):
  """
  The cute side of Qt's QSequentialAnimationGroup: a plain Python object
  standing in front of one C++ QSequentialAnimationGroup.

  It is built on the cute 'QAnimationGroup', as Qt's
  QSequentialAnimationGroup is built on Qt's QAnimationGroup, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSequentialAnimationGroup that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'addPause',
  'insertPause', 'currentAnimation', 'duration', 'event',
  'updateCurrentTime', 'updateState', 'updateDirection'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSequentialAnimationGroup::~QSequentialAnimationGroup()': the
    destructor: Python never removes a C++ QSequentialAnimationGroup.

  What has no ritual
  ------------------

  11 of the 23 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found;
  1 a signal.

  What to expect
  --------------

  - The C++ QSequentialAnimationGroup is created at the first use, not by
    'QSequentialAnimationGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSequentialAnimationGroup.
  - Qt tells when it has removed the C++ QSequentialAnimationGroup. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QSequentialAnimationGroup::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsequentialanimationgroup.html#tr

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
    #  QString QSequentialAnimationGroup::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QSequentialAnimationGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSequentialAnimationGroup'

  #  A C++ QSequentialAnimationGroup Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSequentialAnimationGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSequentialAnimationGroup::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSequentialAnimationGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QSequentialAnimationGroup10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentAnimation(self) -> Optional[QAbstractAnimation]:
    """
    Calls Qt's 'QAbstractAnimation
    *QSequentialAnimationGroup::currentAnimation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#currentAnimation

    Returns
    -------

    Optional[QAbstractAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimation *QSequentialAnimationGroup::currentAnimation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QSequentialAnimationGroup16currentAnimationEv',
    )
    return QAbstractAnimation._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QSequentialAnimationGroup::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#duration
    """
    #  int QSequentialAnimationGroup::duration() const
    ritual = 'ritual_ZNK25QSequentialAnimationGroup8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QSequentialAnimationGroup8durationEv'
    return self.uglySide.call(ritual)

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QSequentialAnimationGroup::QSequentialAnimationGroup(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSequentialAnimationGroup::QSequentialAnimationGroup(QObject *parent)
    self._noteCreation(QSequentialAnimationGroup, lambda: Rituals.call(
        'ritual_ZN25QSequentialAnimationGroupC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(int)
  def addPause(self, msecs: int) -> Optional[QPauseAnimation]:
    """
    Calls Qt's 'QPauseAnimation *QSequentialAnimationGroup::addPause(int
    msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#addPause

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    Returns
    -------

    Optional[QPauseAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPauseAnimation *QSequentialAnimationGroup::addPause(int msecs)
    address = self.uglySide.call(
        'ritual_ZN25QSequentialAnimationGroup8addPauseEi', msecs,
    )
    from . import QPauseAnimation
    return QPauseAnimation._cuteAt(address)

  @overload(int, int)
  def insertPause(self, index: int, msecs: int) -> Optional[QPauseAnimation]:
    """
    Calls Qt's 'QPauseAnimation *QSequentialAnimationGroup::insertPause(int
    index, int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#insertPause

    Parameters
    ----------

    index : int
      Passed on as it is.

    msecs : int
      Passed on as it is.

    Returns
    -------

    Optional[QPauseAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPauseAnimation *QSequentialAnimationGroup::insertPause(int index, int
    #      msecs)
    address = self.uglySide.call(
        'ritual_ZN25QSequentialAnimationGroup11insertPauseEii', index, msecs,
    )
    from . import QPauseAnimation
    return QPauseAnimation._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSequentialAnimationGroup::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSequentialAnimationGroup::event(QEvent *event)
    ritual = 'ritual_ZN25QSequentialAnimationGroup5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QSequentialAnimationGroup5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(int)
  def updateCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QSequentialAnimationGroup::updateCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#updateCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSequentialAnimationGroup::updateCurrentTime(int a0)
    ritual = 'ritual_ZN25QSequentialAnimationGroup17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSequentialAnimationGroup17updateCurrentTimeEi')
    self.uglySide.call(ritual, a0)

  @overload(QAbstractAnimation.State, QAbstractAnimation.State)
  def updateState(
      self,
      newState: QAbstractAnimation.State,
      oldState: QAbstractAnimation.State,
  ) -> None:
    """
    Calls Qt's 'void
    QSequentialAnimationGroup::updateState(QAbstractAnimation::State
    newState, QAbstractAnimation::State oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimation.State
      Passed on as its number.

    oldState : QAbstractAnimation.State
      Passed on as its number.
    """
    #  void QSequentialAnimationGroup::updateState(QAbstractAnimation::State
    #      newState, QAbstractAnimation::State oldState)
    ritual = (
        'ritual_ZN25QSequentialAnimationGroup11updateStateEN18QAbstractAnim'
        'ation5StateES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSequentialAnimationGroup11updateStateEN18QAbstra'
          'ctAnimation5StateES1_')
    self.uglySide.call(ritual, newState.value, oldState.value)

  @overload(QAbstractAnimation.Direction)
  def updateDirection(self, direction: QAbstractAnimation.Direction) -> None:
    """
    Calls Qt's 'void
    QSequentialAnimationGroup::updateDirection(QAbstractAnimation::Direction
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#updateDirection

    Parameters
    ----------

    direction : QAbstractAnimation.Direction
      Passed on as its number.
    """
    #  void QSequentialAnimationGroup::updateDirection(QAbstractAnimation::
    #      Direction direction)
    ritual = (
        'ritual_ZN25QSequentialAnimationGroup15updateDirectionEN18QAbstract'
        'Animation9DirectionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSequentialAnimationGroup15updateDirectionEN18QAb'
          'stractAnimation9DirectionE')
    self.uglySide.call(ritual, direction.value)
