"""
QStyleAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QStyleAnimation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractAnimation, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTime = WAIT['QTime']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyleAnimation(QAbstractAnimation):
  """
  The cute side of Qt's QStyleAnimation: a plain Python object standing in
  front of one C++ QStyleAnimation.

  It is built on the cute 'QAbstractAnimation', as Qt's QStyleAnimation is
  built on Qt's QAbstractAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStyleAnimation that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'target', 'duration',
  'setDuration', 'delay', 'setDelay', 'startTime', 'setStartTime',
  'frameRate', 'setFrameRate', 'updateTarget', 'start', 'isUpdateNeeded',
  'updateCurrentTime'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QStyleAnimation::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QStyleAnimation::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QStyleAnimation::~QStyleAnimation()': the destructor: Python never
    removes a C++ QStyleAnimation.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QStyleAnimation is created at the first use, not by
    'QStyleAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStyleAnimation.
  - Qt tells when it has removed the C++ QStyleAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QStyleAnimation, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FrameRate(CuteNum):
    """
    The enum 'QStyleAnimation::FrameRate' of Qt, with the 5 names Qt gives in
    it.
    """

    DefaultFps = Kee[int](0)
    SixtyFps = Kee[int](1)
    ThirtyFps = Kee[int](2)
    TwentyFps = Kee[int](3)
    FifteenFps = Kee[int](4)

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
    Calls Qt's 'QString QStyleAnimation::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#tr

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
    #  QString QStyleAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QStyleAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleAnimation'

  #  A C++ QStyleAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStyleAnimation'

  #  The functions Qt calls itself that QStyleAnimation is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isUpdateNeeded': (
          ('_ZNK15QStyleAnimation14isUpdateNeededEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStyleAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStyleAnimation::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QStyleAnimation10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QStyleAnimation::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QStyleAnimation::target() const
    address = self.uglySide.call('ritual_ZNK15QStyleAnimation6targetEv')
    return QObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QStyleAnimation::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#duration
    """
    #  int QStyleAnimation::duration() const
    ritual = 'ritual_ZNK15QStyleAnimation8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QStyleAnimation8durationEv'
    return self.uglySide.call(ritual)

  def delay(self) -> int:
    """
    Calls Qt's 'int QStyleAnimation::delay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#delay
    """
    #  int QStyleAnimation::delay() const
    return self.uglySide.call('ritual_ZNK15QStyleAnimation5delayEv')

  def startTime(self) -> QTime:
    """
    Calls Qt's 'QTime QStyleAnimation::startTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#startTime

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QStyleAnimation::startTime() const
    address = self.uglySide.call('ritual_ZNK15QStyleAnimation9startTimeEv')
    from ..QtCore import QTime
    return QTime._cuteOwning(address)

  def frameRate(self) -> FrameRate:
    """
    Calls Qt's 'FrameRate QStyleAnimation::frameRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#frameRate

    Returns
    -------

    FrameRate
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FrameRate(number)' gives.
    """
    #  FrameRate QStyleAnimation::frameRate() const
    return QStyleAnimation.FrameRate(self.uglySide.call(
        'ritual_ZNK15QStyleAnimation9frameRateEv',
    ))

  def isUpdateNeeded(self) -> bool:
    """
    Calls Qt's 'bool QStyleAnimation::isUpdateNeeded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleanimation.html#isUpdateNeeded
    """
    #  bool QStyleAnimation::isUpdateNeeded() const
    ritual = 'ritual_ZNK15QStyleAnimation14isUpdateNeededEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QStyleAnimation14isUpdateNeededEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QStyleAnimation::setDuration(int duration)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#setDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QStyleAnimation::setDuration(int duration)
    self.uglySide.call('ritual_ZN15QStyleAnimation11setDurationEi', duration)

  @overload(int)
  def setDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QStyleAnimation::setDelay(int delay)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#setDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QStyleAnimation::setDelay(int delay)
    self.uglySide.call('ritual_ZN15QStyleAnimation8setDelayEi', delay)

  @overload(QTime)
  def setStartTime(self, time: QTime) -> None:
    """
    Calls Qt's 'void QStyleAnimation::setStartTime(QTime time)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#setStartTime

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.
    """
    #  void QStyleAnimation::setStartTime(QTime time)
    self.uglySide.call(
        'ritual_ZN15QStyleAnimation12setStartTimeE5QTime',
        self._valueOf(time),
    )

  @overload(FrameRate)
  def setFrameRate(self, fps: FrameRate) -> None:
    """
    Calls Qt's 'void QStyleAnimation::setFrameRate(FrameRate fps)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#setFrameRate

    Parameters
    ----------

    fps : FrameRate
      Passed on as its number.
    """
    #  void QStyleAnimation::setFrameRate(FrameRate fps)
    self.uglySide.call(
        'ritual_ZN15QStyleAnimation12setFrameRateENS_9FrameRateE', fps.value,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, target: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QStyleAnimation::QStyleAnimation(QObject
    *target)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleanimation.html#QStyleAnimation

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStyleAnimation::QStyleAnimation(QObject *target)
    self._noteCreation(QStyleAnimation, lambda: Rituals.call(
        'ritual_ZN15QStyleAnimationC1EP7QObject',
        self._addressOf(target, 'QObject'),
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

  def updateTarget(self) -> None:
    """
    Calls Qt's 'void QStyleAnimation::updateTarget()'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#updateTarget
    """
    #  void QStyleAnimation::updateTarget()
    self.uglySide.call('ritual_ZN15QStyleAnimation12updateTargetEv')

  def start(self) -> None:
    """
    Calls Qt's 'void QStyleAnimation::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleanimation.html#start
    """
    #  void QStyleAnimation::start()
    self.uglySide.call('ritual_ZN15QStyleAnimation5startEv')

  @overload(int)
  def updateCurrentTime(self, time: int) -> None:
    """
    Calls Qt's 'void QStyleAnimation::updateCurrentTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleanimation.html#updateCurrentTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QStyleAnimation::updateCurrentTime(int time)
    ritual = 'ritual_ZN15QStyleAnimation17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QStyleAnimation17updateCurrentTimeEi'
    self.uglySide.call(ritual, time)
