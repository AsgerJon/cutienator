"""
QEventLoop binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qeventloop.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDeadlineTimer, QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEventLoop(QObject):
  """
  The cute side of Qt's QEventLoop: a plain Python object standing in front
  of one C++ QEventLoop.

  It is built on the cute 'QObject', as Qt's QEventLoop is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QEventLoop that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'processEvents', 'exec',
  'isRunning', 'wakeUp', 'event', 'exit', 'quit'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QEventLoop::~QEventLoop()': the destructor: Python never removes a
    C++ QEventLoop.

  What has no ritual
  ------------------

  6 of the 19 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QEventLoop is created at the first use, not by 'QEventLoop(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEventLoop.
  - Qt tells when it has removed the C++ QEventLoop. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QEventLoop, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ProcessEventsFlag(CuteFlags):
    """
    The flags enum 'QEventLoop::ProcessEventsFlag' of Qt, with the 8 names Qt
    gives in it. Qt names the type of its combinations
    'QEventLoop::ProcessEventsFlags'.
    """

    AllEvents = 0x0
    ExcludeUserInputEvents = 0x1
    ExcludeSocketNotifiers = 0x2
    WaitForMoreEvents = 0x4
    X11ExcludeTimers = 0x8
    EventLoopExec = 0x20
    DialogExec = 0x40
    ApplicationExec = 0x80

  ProcessEventsFlags = ProcessEventsFlag

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
    Calls Qt's 'QString QEventLoop::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#tr

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
    #  QString QEventLoop::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QEventLoop2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventLoop'

  #  A C++ QEventLoop Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QEventLoop'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QEventLoop::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QEventLoop::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QEventLoop10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QEventLoop::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#isRunning
    """
    #  bool QEventLoop::isRunning() const
    return self.uglySide.call('ritual_ZNK10QEventLoop9isRunningEv')

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
    Notes what was given, for Qt's 'QEventLoop::QEventLoop(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#QEventLoop

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QEventLoop::QEventLoop(QObject *parent)
    self._noteCreation(QEventLoop, lambda: Rituals.call(
        'ritual_ZN10QEventLoopC1EP7QObject', self._addressOf(parent),
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

  @overload()
  @overload(ProcessEventsFlags)
  def processEvents(
      self,
      flags: ProcessEventsFlags = ProcessEventsFlags.AllEvents,
  ) -> bool:
    """
    Calls Qt's 'bool QEventLoop::processEvents(ProcessEventsFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#processEvents

    Parameters
    ----------

    flags : ProcessEventsFlags
      Passed on as its number. May be left out, as in Qt: it is then
      ProcessEventsFlags.AllEvents.
    """
    #  bool QEventLoop::processEvents(ProcessEventsFlags flags)
    return self.uglySide.call(
        'ritual_ZN10QEventLoop13processEventsE6QFlagsINS_17ProcessEventsFla'
        'gEE',
        flags.value,
    )

  @overload(ProcessEventsFlags, int)
  def processEvents(
      self,
      flags: ProcessEventsFlags,
      maximumTime: int,
  ) -> None:
    """
    Calls Qt's 'void QEventLoop::processEvents(ProcessEventsFlags flags, int
    maximumTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#processEvents

    Parameters
    ----------

    flags : ProcessEventsFlags
      Passed on as its number.

    maximumTime : int
      Passed on as it is.
    """
    #  void QEventLoop::processEvents(ProcessEventsFlags flags, int
    #      maximumTime)
    self.uglySide.call(
        'ritual_ZN10QEventLoop13processEventsE6QFlagsINS_17ProcessEventsFla'
        'gEEi',
        flags.value, maximumTime,
    )

  @overload(ProcessEventsFlags, QDeadlineTimer)
  def processEvents(
      self,
      flags: ProcessEventsFlags,
      deadline: QDeadlineTimer,
  ) -> None:
    """
    Calls Qt's 'void QEventLoop::processEvents(ProcessEventsFlags flags,
    QDeadlineTimer deadline)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#processEvents

    Parameters
    ----------

    flags : ProcessEventsFlags
      Passed on as its number.

    deadline : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  void QEventLoop::processEvents(ProcessEventsFlags flags,
    #      QDeadlineTimer deadline)
    self.uglySide.call(
        'ritual_ZN10QEventLoop13processEventsE6QFlagsINS_17ProcessEventsFla'
        'gEE14QDeadlineTimer',
        flags.value, self._valueOf(deadline),
    )

  @overload()
  @overload(ProcessEventsFlags)
  def exec(
      self,
      flags: ProcessEventsFlags = ProcessEventsFlags.AllEvents,
  ) -> int:
    """
    Calls Qt's 'int QEventLoop::exec(ProcessEventsFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#exec

    Parameters
    ----------

    flags : ProcessEventsFlags
      Passed on as its number. May be left out, as in Qt: it is then
      ProcessEventsFlags.AllEvents.
    """
    #  int QEventLoop::exec(ProcessEventsFlags flags)
    return self.uglySide.call(
        'ritual_ZN10QEventLoop4execE6QFlagsINS_17ProcessEventsFlagEE',
        flags.value,
    )

  def wakeUp(self) -> None:
    """
    Calls Qt's 'void QEventLoop::wakeUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#wakeUp
    """
    #  void QEventLoop::wakeUp()
    self.uglySide.call('ritual_ZN10QEventLoop6wakeUpEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QEventLoop::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QEventLoop::event(QEvent *event)
    ritual = 'ritual_ZN10QEventLoop5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QEventLoop5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload()
  @overload(int)
  def exit(self, returnCode: int = 0) -> None:
    """
    Calls Qt's 'void QEventLoop::exit(int returnCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#exit

    Parameters
    ----------

    returnCode : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QEventLoop::exit(int returnCode)
    self.uglySide.call('ritual_ZN10QEventLoop4exitEi', returnCode)

  def quit(self) -> None:
    """
    Calls Qt's 'void QEventLoop::quit()'.

    Qt's own words: https://doc.qt.io/qt-6/qeventloop.html#quit
    """
    #  void QEventLoop::quit()
    self.uglySide.call('ritual_ZN10QEventLoop4quitEv')
