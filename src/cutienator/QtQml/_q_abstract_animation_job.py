"""
QAbstractAnimationJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qabstractanimationjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractAnimationJob to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from . import QInheritedListNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug
  from . import QAnimationGroupJob, QAnimationJobChangeListener
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAnimationJobChangeListener = WAIT['QAnimationJobChangeListener']
  QDebug = WAIT['QDebug']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAnimationJob(QInheritedListNode):
  """
  The cute side of Qt's QAbstractAnimationJob: a plain Python object standing
  in front of one C++ QAbstractAnimationJob.

  It is built on the cute 'QInheritedListNode', as Qt's QAbstractAnimationJob
  is built on Qt's QInheritedListNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractAnimationJob that has a ritual and that
  Python can call so far, 40 names in all: 'group', 'loopCount',
  'setLoopCount', 'totalDuration', 'duration', 'direction', 'setDirection',
  'currentTime', 'currentLoopTime', 'currentLoop', 'state', 'isRunning',
  'isStopped', 'isPaused', 'setDisableUserControl', 'setEnableUserControl',
  'userControlDisabled', 'setCurrentTime', 'start', 'pause', 'resume',
  'stop', 'complete', 'addAnimationChangeListener',
  'removeAnimationChangeListener', 'isGroup', 'isRenderThreadJob',
  'isRenderThreadProxy', 'updateCurrentTime', 'updateLoopCount',
  'updateState', 'updateDirection', 'topLevelAnimationLoopChanged',
  'debugAnimation', 'fireTopLevelAnimationLoopChanged', 'setState',
  'finished', 'stateChanged', 'currentLoopChanged', 'currentTimeChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractAnimationJob::~QAbstractAnimationJob()': the destructor:
    Python never removes a C++ QAbstractAnimationJob.
  - Qt's 'QDebug operator<<(QDebug a0, const QAbstractAnimationJob *job)': an
    operator between other classes, written inside this one.

  What has no ritual
  ------------------

  3 of the 46 functions Qt declares: 2 forbidden; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QAbstractAnimationJob is created at the first use, not by
    'QAbstractAnimationJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractAnimationJob.
  - Each name of Qt's QAbstractAnimationJob that has no cute function yet,
    'directionChanged', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QAbstractAnimationJob, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ChangeType(CuteFlags):
    """
    The flags enum 'QAbstractAnimationJob::ChangeType' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QAbstractAnimationJob::ChangeTypes'.
    """

    Completion = 0x1
    StateChange = 0x2
    CurrentLoop = 0x4
    CurrentTime = 0x8

  ChangeTypes = ChangeType

  class Direction(CuteNum):
    """
    The enum 'QAbstractAnimationJob::Direction' of Qt, with the 2 names Qt
    gives in it.
    """

    Forward = Kee[int](0)
    Backward = Kee[int](1)

  class State(CuteNum):
    """
    The enum 'QAbstractAnimationJob::State' of Qt, with the 3 names Qt gives
    in it.
    """

    Stopped = Kee[int](0)
    Paused = Kee[int](1)
    Running = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractAnimationJob'

  #  A C++ QAbstractAnimationJob Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractAnimationJob'

  #  The functions Qt calls itself that QAbstractAnimationJob is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'duration': (
          ('_ZNK21QAbstractAnimationJob8durationEv',
           ('int', 'number', ''),
           ()),
      ),
      'updateCurrentTime': (
          ('_ZN21QAbstractAnimationJob17updateCurrentTimeEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'updateLoopCount': (
          ('_ZN21QAbstractAnimationJob15updateLoopCountEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'updateState': (
          ('_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQml:QAbstractAnimationJob.State'),
               ('int', 'enum', 'QtQml:QAbstractAnimationJob.State'),
           )),
      ),
      'updateDirection': (
          ('_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQml:QAbstractAnimationJob.Direction'),
           )),
      ),
      'topLevelAnimationLoopChanged': (
          ('_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'debugAnimation': (
          ('_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QDebug'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def group(self) -> Optional[QAnimationGroupJob]:
    """
    Calls Qt's 'QAnimationGroupJob *QAbstractAnimationJob::group() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimationjob.html#group

    Returns
    -------

    Optional[QAnimationGroupJob]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationGroupJob *QAbstractAnimationJob::group() const
    address = self._callAs(
        'QAbstractAnimationJob', 'ritual_ZNK21QAbstractAnimationJob5groupEv',
    )
    from . import QAnimationGroupJob
    return QAnimationGroupJob._cuteAt(address)

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimationJob::loopCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#loopCount
    """
    #  int QAbstractAnimationJob::loopCount() const
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob9loopCountEv',
    )

  def totalDuration(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimationJob::totalDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#totalDuration
    """
    #  int QAbstractAnimationJob::totalDuration() const
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob13totalDurationEv',
    )

  def duration(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimationJob::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#duration
    """
    #  int QAbstractAnimationJob::duration() const
    ritual = 'ritual_ZNK21QAbstractAnimationJob8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QAbstractAnimationJob8durationEv'
    return self._callAs('QAbstractAnimationJob', ritual)

  def direction(self) -> Direction:
    """
    Calls Qt's 'QAbstractAnimationJob::Direction
    QAbstractAnimationJob::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#direction

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  QAbstractAnimationJob::Direction QAbstractAnimationJob::direction()
    #      const
    return QAbstractAnimationJob.Direction(self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob9directionEv',
    ))

  def currentTime(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimationJob::currentTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#currentTime
    """
    #  int QAbstractAnimationJob::currentTime() const
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob11currentTimeEv',
    )

  def currentLoopTime(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimationJob::currentLoopTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#currentLoopTime
    """
    #  int QAbstractAnimationJob::currentLoopTime() const
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob15currentLoopTimeEv',
    )

  def currentLoop(self) -> int:
    """
    Calls Qt's 'int QAbstractAnimationJob::currentLoop() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#currentLoop
    """
    #  int QAbstractAnimationJob::currentLoop() const
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob11currentLoopEv',
    )

  def state(self) -> State:
    """
    Calls Qt's 'QAbstractAnimationJob::State QAbstractAnimationJob::state()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimationjob.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  QAbstractAnimationJob::State QAbstractAnimationJob::state() const
    return QAbstractAnimationJob.State(self._callAs(
        'QAbstractAnimationJob', 'ritual_ZNK21QAbstractAnimationJob5stateEv',
    ))

  def userControlDisabled(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAnimationJob::userControlDisabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#userControlDisabled
    """
    #  bool QAbstractAnimationJob::userControlDisabled() const
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob19userControlDisabledEv',
    )

  def isGroup(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAnimationJob::isGroup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimationjob.html#isGroup
    """
    #  bool QAbstractAnimationJob::isGroup() const
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob7isGroupEv',
    )

  def isRenderThreadJob(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAnimationJob::isRenderThreadJob() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#isRenderThreadJob
    """
    #  bool QAbstractAnimationJob::isRenderThreadJob() const
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob17isRenderThreadJobEv',
    )

  def isRenderThreadProxy(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAnimationJob::isRenderThreadProxy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#isRenderThreadProxy
    """
    #  bool QAbstractAnimationJob::isRenderThreadProxy() const
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZNK21QAbstractAnimationJob19isRenderThreadProxyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLoopCount(self, loopCount: int) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::setLoopCount(int loopCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#setLoopCount

    Parameters
    ----------

    loopCount : int
      Passed on as it is.
    """
    #  void QAbstractAnimationJob::setLoopCount(int loopCount)
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob12setLoopCountEi',
        loopCount,
    )

  @overload(Direction)
  def setDirection(self, direction: Direction) -> None:
    """
    Calls Qt's 'void
    QAbstractAnimationJob::setDirection(QAbstractAnimationJob::Direction
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#setDirection

    Parameters
    ----------

    direction : Direction
      Passed on as its number.
    """
    #  void QAbstractAnimationJob::setDirection(QAbstractAnimationJob::
    #      Direction direction)
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob12setDirectionENS_9DirectionE',
        direction.value,
    )

  def setDisableUserControl(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::setDisableUserControl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#setDisableUserControl
    """
    #  void QAbstractAnimationJob::setDisableUserControl()
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob21setDisableUserControlEv',
    )

  def setEnableUserControl(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::setEnableUserControl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#setEnableUserControl
    """
    #  void QAbstractAnimationJob::setEnableUserControl()
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob20setEnableUserControlEv',
    )

  @overload(int)
  def setCurrentTime(self, msecs: int) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::setCurrentTime(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#setCurrentTime

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QAbstractAnimationJob::setCurrentTime(int msecs)
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob14setCurrentTimeEi',
        msecs,
    )

  @overload(State)
  def setState(self, state: State) -> None:
    """
    Calls Qt's 'void
    QAbstractAnimationJob::setState(QAbstractAnimationJob::State state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#setState

    Parameters
    ----------

    state : State
      Passed on as its number.
    """
    #  void QAbstractAnimationJob::setState(QAbstractAnimationJob::State
    #      state)
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob8setStateENS_5StateE',
        state.value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractAnimationJob::QAbstractAnimationJob()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#QAbstractAnimationJob
    """
    #  QAbstractAnimationJob::QAbstractAnimationJob()
    self._noteCreation(QAbstractAnimationJob, lambda: Rituals.call(
        'ritual_ZN21QAbstractAnimationJobC1Ev',
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

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAnimationJob::isRunning()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#isRunning
    """
    #  bool QAbstractAnimationJob::isRunning()
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob9isRunningEv',
    )

  def isStopped(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAnimationJob::isStopped()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#isStopped
    """
    #  bool QAbstractAnimationJob::isStopped()
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob9isStoppedEv',
    )

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAnimationJob::isPaused()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#isPaused
    """
    #  bool QAbstractAnimationJob::isPaused()
    return self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob8isPausedEv',
    )

  def start(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimationjob.html#start
    """
    #  void QAbstractAnimationJob::start()
    self._callAs(
        'QAbstractAnimationJob', 'ritual_ZN21QAbstractAnimationJob5startEv',
    )

  def pause(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimationjob.html#pause
    """
    #  void QAbstractAnimationJob::pause()
    self._callAs(
        'QAbstractAnimationJob', 'ritual_ZN21QAbstractAnimationJob5pauseEv',
    )

  def resume(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimationjob.html#resume
    """
    #  void QAbstractAnimationJob::resume()
    self._callAs(
        'QAbstractAnimationJob', 'ritual_ZN21QAbstractAnimationJob6resumeEv',
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimationjob.html#stop
    """
    #  void QAbstractAnimationJob::stop()
    self._callAs(
        'QAbstractAnimationJob', 'ritual_ZN21QAbstractAnimationJob4stopEv',
    )

  def complete(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::complete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#complete
    """
    #  void QAbstractAnimationJob::complete()
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob8completeEv',
    )

  @overload(QAnimationJobChangeListener, ChangeTypes)
  @overload(NoneType, ChangeTypes)
  def addAnimationChangeListener(
      self,
      listener: Optional[QAnimationJobChangeListener],
      a1: ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::addAnimationChangeListener(
    QAnimationJobChangeListener *listener, QAbstractAnimationJob::ChangeTypes
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html

    Parameters
    ----------

    listener : Optional[QAnimationJobChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : ChangeTypes
      Passed on as its number.
    """
    #  void QAbstractAnimationJob::addAnimationChangeListener(
    #      QAnimationJobChangeListener *listener,
    #      QAbstractAnimationJob::ChangeTypes a1)
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob26addAnimationChangeListenerEP27QA'
        'nimationJobChangeListener6QFlagsINS_10ChangeTypeEE',
        self._addressOf(listener, 'QAnimationJobChangeListener'), a1.value,
    )

  @overload(QAnimationJobChangeListener, ChangeTypes)
  @overload(NoneType, ChangeTypes)
  def removeAnimationChangeListener(
      self,
      listener: Optional[QAnimationJobChangeListener],
      a1: ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::removeAnimationChangeListener(
    QAnimationJobChangeListener *listener, QAbstractAnimationJob::ChangeTypes
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html

    Parameters
    ----------

    listener : Optional[QAnimationJobChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : ChangeTypes
      Passed on as its number.
    """
    #  void QAbstractAnimationJob::removeAnimationChangeListener(
    #      QAnimationJobChangeListener *listener,
    #      QAbstractAnimationJob::ChangeTypes a1)
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob29removeAnimationChangeListenerEP2'
        '7QAnimationJobChangeListener6QFlagsINS_10ChangeTypeEE',
        self._addressOf(listener, 'QAnimationJobChangeListener'), a1.value,
    )

  @overload(int)
  def updateCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::updateCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#updateCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractAnimationJob::updateCurrentTime(int a0)
    ritual = 'ritual_ZN21QAbstractAnimationJob17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAbstractAnimationJob17updateCurrentTimeEi'
    self._callAs('QAbstractAnimationJob', ritual, a0)

  @overload(int)
  def updateLoopCount(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::updateLoopCount(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#updateLoopCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractAnimationJob::updateLoopCount(int a0)
    ritual = 'ritual_ZN21QAbstractAnimationJob15updateLoopCountEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QAbstractAnimationJob15updateLoopCountEi'
    self._callAs('QAbstractAnimationJob', ritual, a0)

  @overload(State, State)
  def updateState(self, newState: State, oldState: State) -> None:
    """
    Calls Qt's 'void
    QAbstractAnimationJob::updateState(QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#updateState

    Parameters
    ----------

    newState : State
      Passed on as its number.

    oldState : State
      Passed on as its number.
    """
    #  void QAbstractAnimationJob::updateState(QAbstractAnimationJob::State
    #      newState, QAbstractAnimationJob::State oldState)
    ritual = 'ritual_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_')
    self._callAs(
        'QAbstractAnimationJob', ritual, newState.value, oldState.value,
    )

  @overload(Direction)
  def updateDirection(self, direction: Direction) -> None:
    """
    Calls Qt's 'void
    QAbstractAnimationJob::updateDirection(QAbstractAnimationJob::Direction
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#updateDirection

    Parameters
    ----------

    direction : Direction
      Passed on as its number.
    """
    #  void QAbstractAnimationJob::updateDirection(QAbstractAnimationJob::
    #      Direction direction)
    ritual = (
        'ritual_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QAbstractAnimationJob15updateDirectionENS_9Direct'
          'ionE')
    self._callAs('QAbstractAnimationJob', ritual, direction.value)

  def topLevelAnimationLoopChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::topLevelAnimationLoopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html
    """
    #  void QAbstractAnimationJob::topLevelAnimationLoopChanged()
    ritual = (
        'ritual_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QAbstractAnimationJob28topLevelAnimationLoopChang'
          'edEv')
    self._callAs('QAbstractAnimationJob', ritual)

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::debugAnimation(QDebug d) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QAbstractAnimationJob::debugAnimation(QDebug d) const
    ritual = 'ritual_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug')
    self._callAs('QAbstractAnimationJob', ritual, self._valueOf(d))

  def fireTopLevelAnimationLoopChanged(self) -> None:
    """
    Calls Qt's 'void
    QAbstractAnimationJob::fireTopLevelAnimationLoopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html
    """
    #  void QAbstractAnimationJob::fireTopLevelAnimationLoopChanged()
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob32fireTopLevelAnimationLoopChanged'
        'Ev',
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#finished
    """
    #  void QAbstractAnimationJob::finished()
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob8finishedEv',
    )

  @overload(State, State)
  def stateChanged(self, newState: State, oldState: State) -> None:
    """
    Calls Qt's 'void
    QAbstractAnimationJob::stateChanged(QAbstractAnimationJob::State
    newState, QAbstractAnimationJob::State oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#stateChanged

    Parameters
    ----------

    newState : State
      Passed on as its number.

    oldState : State
      Passed on as its number.
    """
    #  void QAbstractAnimationJob::stateChanged(QAbstractAnimationJob::State
    #      newState, QAbstractAnimationJob::State oldState)
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob12stateChangedENS_5StateES0_',
        newState.value, oldState.value,
    )

  def currentLoopChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::currentLoopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#currentLoopChanged
    """
    #  void QAbstractAnimationJob::currentLoopChanged()
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob18currentLoopChangedEv',
    )

  @overload(int)
  def currentTimeChanged(self, currentTime: int) -> None:
    """
    Calls Qt's 'void QAbstractAnimationJob::currentTimeChanged(int
    currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationjob.html#currentTimeChanged

    Parameters
    ----------

    currentTime : int
      Passed on as it is.
    """
    #  void QAbstractAnimationJob::currentTimeChanged(int currentTime)
    self._callAs(
        'QAbstractAnimationJob',
        'ritual_ZN21QAbstractAnimationJob18currentTimeChangedEi',
        currentTime,
    )

  @staticmethod
  def directionChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractAnimationJob::directionChanged(QAbstractAnimationJob::Direction
    a0)': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QAbstractAnimationJob.directionChanged' has no cute function yet. "
        "Qt's 'void "
        "QAbstractAnimationJob::directionChanged(QAbstractAnimationJob::Dire"
        "ction a0)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
