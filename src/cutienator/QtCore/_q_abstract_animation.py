"""
QAbstractAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAnimationGroup, QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAnimation(QObject):
  """
  The cute side of Qt's QAbstractAnimation: a plain Python object standing in
  front of one C++ QAbstractAnimation.

  It is built on the cute 'QObject', as Qt's QAbstractAnimation is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractAnimation that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'state', 'group',
  'direction', 'setDirection', 'currentTime', 'currentLoopTime', 'loopCount',
  'setLoopCount', 'currentLoop', 'duration', 'totalDuration', 'start',
  'pause', 'resume', 'setPaused', 'stop', 'setCurrentTime'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractAnimation::~QAbstractAnimation()': the destructor: Python
    never removes a C++ QAbstractAnimation.

  What has no ritual
  ------------------

  23 of the 43 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 5 protected; 4 a signal; 3 private; 2 forbidden; 1 a template;
  1 the class is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QAbstractAnimation is created at the first use, not by
    'QAbstractAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractAnimation.
  - Qt tells when it has removed the C++ QAbstractAnimation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstractAnimation, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DeletionPolicy(CuteNum):
    """
    The enum 'QAbstractAnimation::DeletionPolicy' of Qt, with the 2 names Qt
    gives in it.
    """

    KeepWhenStopped = Kee[int](0)
    DeleteWhenStopped = Kee[int](1)

  class Direction(CuteNum):
    """
    The enum 'QAbstractAnimation::Direction' of Qt, with the 2 names Qt gives
    in it.
    """

    Forward = Kee[int](0)
    Backward = Kee[int](1)

  class State(CuteNum):
    """
    The enum 'QAbstractAnimation::State' of Qt, with the 3 names Qt gives in
    it.
    """

    Stopped = Kee[int](0)
    Paused = Kee[int](1)
    Running = Kee[int](2)

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
    Calls Qt's 'QString QAbstractAnimation::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#tr

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
    #  QString QAbstractAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QAbstractAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractAnimation10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def state(self) -> State:
    """
    Calls Qt's 'State QAbstractAnimation::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QAbstractAnimation::state() const
    return QAbstractAnimation.State(self.uglySide.call(
        'ritual_ZNK18QAbstractAnimation5stateEv',
    ))

  def group(self) -> Optional[QAnimationGroup]:
    """
    Calls Qt's 'QAnimationGroup *QAbstractAnimation::group() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#group

    Returns
    -------

    Optional[QAnimationGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationGroup *QAbstractAnimation::group() const
    address = self.uglySide.call('ritual_ZNK18QAbstractAnimation5groupEv')
    from . import QAnimationGroup
    return QAnimationGroup._cuteAt(address)

  def direction(self) -> Direction:
    """
    Calls Qt's 'Direction QAbstractAnimation::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#direction

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  Direction QAbstractAnimation::direction() const
    return QAbstractAnimation.Direction(self.uglySide.call(
        'ritual_ZNK18QAbstractAnimation9directionEv',
    ))

  def currentTime(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimation::currentTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimation.html#currentTime
    """
    #  int QAbstractAnimation::currentTime() const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractAnimation11currentTimeEv',
    )

  def currentLoopTime(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimation::currentLoopTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimation.html#currentLoopTime
    """
    #  int QAbstractAnimation::currentLoopTime() const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractAnimation15currentLoopTimeEv',
    )

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimation::loopCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#loopCount
    """
    #  int QAbstractAnimation::loopCount() const
    return self.uglySide.call('ritual_ZNK18QAbstractAnimation9loopCountEv')

  def currentLoop(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimation::currentLoop() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimation.html#currentLoop
    """
    #  int QAbstractAnimation::currentLoop() const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractAnimation11currentLoopEv',
    )

  def duration(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimation::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#duration
    """
    #  int QAbstractAnimation::duration() const
    return self.uglySide.call('ritual_ZNK18QAbstractAnimation8durationEv')

  def totalDuration(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimation::totalDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimation.html#totalDuration
    """
    #  int QAbstractAnimation::totalDuration() const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractAnimation13totalDurationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Direction)
  def setDirection(self, direction: Direction) -> None:
    """
    Calls Qt's 'void QAbstractAnimation::setDirection(Direction direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimation.html#setDirection

    Parameters
    ----------

    direction : Direction
      Passed on as its number.
    """
    #  void QAbstractAnimation::setDirection(Direction direction)
    self.uglySide.call(
        'ritual_ZN18QAbstractAnimation12setDirectionENS_9DirectionE',
        direction.value,
    )

  @overload(int)
  def setLoopCount(self, loopCount: int) -> None:
    """
    Calls Qt's 'void QAbstractAnimation::setLoopCount(int loopCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimation.html#setLoopCount

    Parameters
    ----------

    loopCount : int
      Passed on as it is.
    """
    #  void QAbstractAnimation::setLoopCount(int loopCount)
    self.uglySide.call(
        'ritual_ZN18QAbstractAnimation12setLoopCountEi', loopCount,
    )

  @overload(bool)
  def setPaused(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractAnimation::setPaused(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#setPaused

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractAnimation::setPaused(bool a0)
    self.uglySide.call('ritual_ZN18QAbstractAnimation9setPausedEb', a0)

  @overload(int)
  def setCurrentTime(self, msecs: int) -> None:
    """
    Calls Qt's 'void QAbstractAnimation::setCurrentTime(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimation.html#setCurrentTime

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QAbstractAnimation::setCurrentTime(int msecs)
    self.uglySide.call(
        'ritual_ZN18QAbstractAnimation14setCurrentTimeEi', msecs,
    )

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

  @overload()
  @overload(DeletionPolicy)
  def start(
      self,
      policy: DeletionPolicy = DeletionPolicy.KeepWhenStopped,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractAnimation::start(QAbstractAnimation::DeletionPolicy policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#start

    Parameters
    ----------

    policy : DeletionPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      DeletionPolicy.KeepWhenStopped.
    """
    #  void QAbstractAnimation::start(QAbstractAnimation::DeletionPolicy
    #      policy)
    self.uglySide.call(
        'ritual_ZN18QAbstractAnimation5startENS_14DeletionPolicyE',
        policy.value,
    )

  def pause(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimation::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#pause
    """
    #  void QAbstractAnimation::pause()
    self.uglySide.call('ritual_ZN18QAbstractAnimation5pauseEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimation::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#resume
    """
    #  void QAbstractAnimation::resume()
    self.uglySide.call('ritual_ZN18QAbstractAnimation6resumeEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimation::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimation.html#stop
    """
    #  void QAbstractAnimation::stop()
    self.uglySide.call('ritual_ZN18QAbstractAnimation4stopEv')
