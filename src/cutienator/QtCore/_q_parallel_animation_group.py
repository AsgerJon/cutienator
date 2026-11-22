"""
QParallelAnimationGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qparallelanimationgroup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractAnimation, QAnimationGroup, QObject

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


class QParallelAnimationGroup(QAnimationGroup):
  """
  The cute side of Qt's QParallelAnimationGroup: a plain Python object
  standing in front of one C++ QParallelAnimationGroup.

  It is built on the cute 'QAnimationGroup', as Qt's QParallelAnimationGroup
  is built on Qt's QAnimationGroup, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QParallelAnimationGroup that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'duration',
  'event', 'updateCurrentTime', 'updateState', 'updateDirection'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QParallelAnimationGroup::~QParallelAnimationGroup()': the
    destructor: Python never removes a C++ QParallelAnimationGroup.

  What has no ritual
  ------------------

  9 of the 18 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QParallelAnimationGroup is created at the first use, not by
    'QParallelAnimationGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QParallelAnimationGroup.
  - Qt tells when it has removed the C++ QParallelAnimationGroup. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QParallelAnimationGroup::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qparallelanimationgroup.html#tr

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
    #  QString QParallelAnimationGroup::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QParallelAnimationGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QParallelAnimationGroup'

  #  A C++ QParallelAnimationGroup Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QParallelAnimationGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QParallelAnimationGroup::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QParallelAnimationGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QParallelAnimationGroup10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QParallelAnimationGroup::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroup.html#duration
    """
    #  int QParallelAnimationGroup::duration() const
    ritual = 'ritual_ZNK23QParallelAnimationGroup8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QParallelAnimationGroup8durationEv'
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
    'QParallelAnimationGroup::QParallelAnimationGroup(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroup.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QParallelAnimationGroup::QParallelAnimationGroup(QObject *parent)
    self._noteCreation(QParallelAnimationGroup, lambda: Rituals.call(
        'ritual_ZN23QParallelAnimationGroupC1EP7QObject',
        self._addressOf(parent),
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
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QParallelAnimationGroup::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qparallelanimationgroup.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QParallelAnimationGroup::event(QEvent *event)
    return self.uglySide.call(
        'ritual_own_ZN23QParallelAnimationGroup5eventEP6QEvent',
        self._addressOf(event),
    )

  @overload(int)
  def updateCurrentTime(self, currentTime: int) -> None:
    """
    Calls Qt's 'void QParallelAnimationGroup::updateCurrentTime(int
    currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroup.html#updateCurrentTime

    Parameters
    ----------

    currentTime : int
      Passed on as it is.
    """
    #  void QParallelAnimationGroup::updateCurrentTime(int currentTime)
    self.uglySide.call(
        'ritual_own_ZN23QParallelAnimationGroup17updateCurrentTimeEi',
        currentTime,
    )

  @overload(QAbstractAnimation.State, QAbstractAnimation.State)
  def updateState(
      self,
      newState: QAbstractAnimation.State,
      oldState: QAbstractAnimation.State,
  ) -> None:
    """
    Calls Qt's 'void
    QParallelAnimationGroup::updateState(QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroup.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimation.State
      Passed on as its number.

    oldState : QAbstractAnimation.State
      Passed on as its number.
    """
    #  void QParallelAnimationGroup::updateState(QAbstractAnimation::State
    #      newState, QAbstractAnimation::State oldState)
    self.uglySide.call(
        'ritual_own_ZN23QParallelAnimationGroup11updateStateEN18QAbstractAn'
        'imation5StateES1_',
        newState.value, oldState.value,
    )

  @overload(QAbstractAnimation.Direction)
  def updateDirection(self, direction: QAbstractAnimation.Direction) -> None:
    """
    Calls Qt's 'void
    QParallelAnimationGroup::updateDirection(QAbstractAnimation::Direction
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroup.html#updateDirection

    Parameters
    ----------

    direction : QAbstractAnimation.Direction
      Passed on as its number.
    """
    #  void QParallelAnimationGroup::updateDirection(QAbstractAnimation::
    #      Direction direction)
    self.uglySide.call(
        'ritual_own_ZN23QParallelAnimationGroup15updateDirectionEN18QAbstra'
        'ctAnimation9DirectionE',
        direction.value,
    )
