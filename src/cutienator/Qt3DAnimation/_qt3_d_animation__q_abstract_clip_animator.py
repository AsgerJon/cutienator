"""
Qt3DAnimation::QAbstractClipAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qabstractclipanimator.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractClipAnimator(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DAnimation::QAbstractClipAnimator: a plain Python
  object standing in front of one C++ Qt3DAnimation::QAbstractClipAnimator.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DAnimation::QAbstractClipAnimator is built on Qt's Qt3DCore::QComponent,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAbstractClipAnimator that has a
  ritual and that Python can call so far, 20 names in all: 'metaObject',
  'tr', 'isRunning', 'channelMapper', 'loopCount', 'clock', 'normalizedTime',
  'setRunning', 'setChannelMapper', 'setLoopCount', 'setClock',
  'setNormalizedTime', 'start', 'stop', 'runningChanged',
  'channelMapperChanged', 'loopCountChanged', 'clockChanged',
  'normalizedTimeChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QAbstractClipAnimator::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QAbstractClipAnimator::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QAbstractClipAnimator::~QAbstractClipAnimator()':
    the destructor: Python never removes a C++
    Qt3DAnimation::QAbstractClipAnimator.
  - Qt's 'Qt3DAnimation::QAbstractClipAnimator::QAbstractClipAnimator(
    QAbstractClipAnimatorPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QAbstractClipAnimatorPrivate
    *Qt3DAnimation::QAbstractClipAnimator::d_func() const': takes in Python
    what 'QAbstractClipAnimatorPrivate
    *Qt3DAnimation::QAbstractClipAnimator::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAbstractClipAnimator is created at the first use,
    not by 'Qt3DAnimation::QAbstractClipAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAbstractClipAnimator.
  - Qt tells when it has removed the C++
    Qt3DAnimation::QAbstractClipAnimator. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  #  The enums Qt writes inside Qt3DAnimation::QAbstractClipAnimator, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Loops(CuteNum):
    """
    The enum 'Qt3DAnimation::QAbstractClipAnimator::Loops' of Qt, with the 1
    names Qt gives in it.
    """

    Infinite = Kee[int](-1)

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
    Calls Qt's 'QString Qt3DAnimation::QAbstractClipAnimator::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html#tr

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
    #  QString Qt3DAnimation::QAbstractClipAnimator::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAbstractClipAnimator'

  #  A C++ Qt3DAnimation::QAbstractClipAnimator Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QAbstractClipAnimator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DAnimation::QAbstractClipAnimator::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QAbstractClipAnimator::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::QAbstractClipAnimator::isRunning()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html#isRunning
    """
    #  bool Qt3DAnimation::QAbstractClipAnimator::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator9isRunningEv',
    )

  def channelMapper(self) -> Optional[Qt3DAnimation.QChannelMapper]:
    """
    Calls Qt's 'Qt3DAnimation::QChannelMapper
    *Qt3DAnimation::QAbstractClipAnimator::channelMapper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Returns
    -------

    Optional[Qt3DAnimation.QChannelMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DAnimation::QChannelMapper
    #      *Qt3DAnimation::QAbstractClipAnimator::channelMapper() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator13channelMapperEv',
    )
    return Qt3DAnimation.QChannelMapper._cuteAt(address)

  def loopCount(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::QAbstractClipAnimator::loopCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html#loopCount
    """
    #  int Qt3DAnimation::QAbstractClipAnimator::loopCount() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator9loopCountEv',
    )

  def clock(self) -> Optional[Qt3DAnimation.QClock]:
    """
    Calls Qt's 'Qt3DAnimation::QClock
    *Qt3DAnimation::QAbstractClipAnimator::clock() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html#clock

    Returns
    -------

    Optional[Qt3DAnimation.QClock]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DAnimation::QClock *Qt3DAnimation::QAbstractClipAnimator::clock()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator5clockEv',
    )
    return Qt3DAnimation.QClock._cuteAt(address)

  def normalizedTime(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAbstractClipAnimator::normalizedTime()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html
    """
    #  float Qt3DAnimation::QAbstractClipAnimator::normalizedTime() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QAbstractClipAnimator14normalizedTimeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAbstractClipAnimator::setRunning(bool
    running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::setRunning(bool running)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator10setRunningEb',
        running,
    )

  @overload(WAIT['Qt3DAnimation.QChannelMapper'])
  @overload(NoneType)
  def setChannelMapper(
      self,
      channelMapper: Optional[Qt3DAnimation.QChannelMapper],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractClipAnimator::setChannelMapper(Qt3DAnimation::
    QChannelMapper *channelMapper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    channelMapper : Optional[Qt3DAnimation.QChannelMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::setChannelMapper(
    #      Qt3DAnimation::QChannelMapper *channelMapper)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator16setChannelMapperE'
        'PNS_14QChannelMapperE',
        self._addressOf(channelMapper),
    )

  @overload(int)
  def setLoopCount(self, loops: int) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAbstractClipAnimator::setLoopCount(int
    loops)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::setLoopCount(int loops)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator12setLoopCountEi',
        loops,
    )

  @overload(WAIT['Qt3DAnimation.QClock'])
  @overload(NoneType)
  def setClock(self, clock: Optional[Qt3DAnimation.QClock]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractClipAnimator::setClock(Qt3DAnimation::QClock
    *clock)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html#setClock

    Parameters
    ----------

    clock : Optional[Qt3DAnimation.QClock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::setClock(Qt3DAnimation::
    #      QClock *clock)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator8setClockEPNS_6QClo'
        'ckE',
        self._addressOf(clock),
    )

  @overload(float)
  def setNormalizedTime(self, timeFraction: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractClipAnimator::setNormalizedTime(float
    timeFraction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    timeFraction : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::setNormalizedTime(float
    #      timeFraction)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator17setNormalizedTime'
        'Ef',
        timeFraction,
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

  @overload()
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QAbstractClipAnimator::QAbstractClipAnimator(Qt3DCore::
    QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QAbstractClipAnimator::QAbstractClipAnimator(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QAbstractClipAnimator, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimatorC1EPN8Qt3DCore5QNod'
        'eE',
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

  def start(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAbstractClipAnimator::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html#start
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::start()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator5startEv',
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAbstractClipAnimator::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html#stop
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::stop()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator4stopEv',
    )

  @overload(bool)
  def runningChanged(self, running: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractClipAnimator::runningChanged(bool running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::runningChanged(bool
    #      running)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator14runningChangedEb',
        running,
    )

  @overload(WAIT['Qt3DAnimation.QChannelMapper'])
  @overload(NoneType)
  def channelMapperChanged(
      self,
      channelMapper: Optional[Qt3DAnimation.QChannelMapper],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractClipAnimator::channelMapperChanged(
    Qt3DAnimation::QChannelMapper *channelMapper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    channelMapper : Optional[Qt3DAnimation.QChannelMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::channelMapperChanged(
    #      Qt3DAnimation::QChannelMapper *channelMapper)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator20channelMapperChan'
        'gedEPNS_14QChannelMapperE',
        self._addressOf(channelMapper),
    )

  @overload(int)
  def loopCountChanged(self, loops: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractClipAnimator::loopCountChanged(int loops)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::loopCountChanged(int loops)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator16loopCountChangedE'
        'i',
        loops,
    )

  @overload(WAIT['Qt3DAnimation.QClock'])
  @overload(NoneType)
  def clockChanged(self, clock: Optional[Qt3DAnimation.QClock]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractClipAnimator::clockChanged(Qt3DAnimation::QClock
    *clock)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    clock : Optional[Qt3DAnimation.QClock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::clockChanged(
    #      Qt3DAnimation::QClock *clock)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator12clockChangedEPNS_'
        '6QClockE',
        self._addressOf(clock),
    )

  @overload(float)
  def normalizedTimeChanged(self, index: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractClipAnimator::normalizedTimeChanged(float
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html

    Parameters
    ----------

    index : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractClipAnimator::normalizedTimeChanged(float
    #      index)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator21normalizedTimeCha'
        'ngedEf',
        index,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QAbstractClipAnimatorPrivate]:
    """
    Calls Qt's 'QAbstractClipAnimatorPrivate
    *Qt3DAnimation::QAbstractClipAnimator::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimator.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractClipAnimatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractClipAnimatorPrivate
    #      *Qt3DAnimation::QAbstractClipAnimator::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QAbstractClipAnimator6d_funcEv',
    )
    return Qt3DAnimation.QAbstractClipAnimatorPrivate._cuteAt(address)
