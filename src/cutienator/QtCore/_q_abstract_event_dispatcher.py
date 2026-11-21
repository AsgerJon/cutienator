"""
QAbstractEventDispatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstracteventdispatcher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QEventLoop, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractNativeEventFilter, QMetaObject, QSocketNotifier
  from . import QThread
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractNativeEventFilter = WAIT['QAbstractNativeEventFilter']
  QSocketNotifier = WAIT['QSocketNotifier']
  QThread = WAIT['QThread']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractEventDispatcher(QObject):
  """
  The cute side of Qt's QAbstractEventDispatcher: a plain Python object
  standing in front of one C++ QAbstractEventDispatcher.

  It is built on the cute 'QObject', as Qt's QAbstractEventDispatcher is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractEventDispatcher that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'instance',
  'processEvents', 'registerSocketNotifier', 'unregisterSocketNotifier',
  'registerTimer', 'unregisterTimer', 'unregisterTimers', 'remainingTime',
  'wakeUp', 'interrupt', 'startingUp', 'closingDown',
  'installNativeEventFilter', 'removeNativeEventFilter'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractEventDispatcher::~QAbstractEventDispatcher()': the
    destructor: Python never removes a C++ QAbstractEventDispatcher.

  What has no ritual
  ------------------

  16 of the 35 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 3 private; 2 a signal; 1 a template; 1 the class is abstract,
  so C++ cannot make one; 1 protected.

  What to expect
  --------------

  - The C++ QAbstractEventDispatcher is created at the first use, not by
    'QAbstractEventDispatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractEventDispatcher.
  - Qt tells when it has removed the C++ QAbstractEventDispatcher. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The classes Qt writes inside QAbstractEventDispatcher, each a class in
  #  here as in C++.

  class TimerInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractEventDispatcher::TimerInfo: a plain Python
    object standing in front of one C++ QAbstractEventDispatcher::TimerInfo.

    C++ hands a QAbstractEventDispatcher::TimerInfo around as a copy, so
    every C++ QAbstractEventDispatcher::TimerInfo behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QAbstractEventDispatcher::TimerInfo yet. It can be
    made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAbstractEventDispatcher::TimerInfo::~TimerInfo()': the
      destructor: Python removes its C++ QAbstractEventDispatcher::TimerInfo
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QAbstractEventDispatcher::TimerInfo is created at the first
      use, not by 'QAbstractEventDispatcher::TimerInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAbstractEventDispatcher::TimerInfo back gives a
      copy the ritual made for Python, in a new cute
      QAbstractEventDispatcher::TimerInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractEventDispatcher::TimerInfo'

    #  Qt's '~QAbstractEventDispatcher::TimerInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QAbstractEventDispatcher::TimerInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN24QAbstractEventDispatcher9TimerInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QAbstractEventDispatcher::TimerInfo::TimerInfo()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstracteventdispatcher-timerinfo.html
      """
      #  QAbstractEventDispatcher::TimerInfo::TimerInfo()
      self._noteCreation(
          QAbstractEventDispatcher.TimerInfo, lambda: Rituals.call(
              'ritual_ZN24QAbstractEventDispatcher9TimerInfoC1Ev',
          ))

    @overload(int, int, Qt.TimerType)
    def __init__(self, id: int, i: int, t: Qt.TimerType) -> None:
      """
      Notes what was given, for Qt's
      'QAbstractEventDispatcher::TimerInfo::TimerInfo(int id, int i,
      Qt::TimerType t)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstracteventdispatcher-timerinfo.html

      Parameters
      ----------

      id : int
        Passed on as it is.

      i : int
        Passed on as it is.

      t : Qt.TimerType
        Passed on as its number.
      """
      #  QAbstractEventDispatcher::TimerInfo::TimerInfo(int id, int i,
      #      Qt::TimerType t)
      self._noteCreation(
          QAbstractEventDispatcher.TimerInfo, lambda: Rituals.call(
              'ritual_ZN24QAbstractEventDispatcher9TimerInfoC1EiiN2Qt9Timer'
              'TypeE',
              id, i, t.value,
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class TimerInfoV2(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractEventDispatcher::TimerInfoV2: a plain
    Python object standing in front of one C++
    QAbstractEventDispatcher::TimerInfoV2.

    C++ hands a QAbstractEventDispatcher::TimerInfoV2 around as a copy, so
    every C++ QAbstractEventDispatcher::TimerInfoV2 behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QAbstractEventDispatcher::TimerInfoV2 yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAbstractEventDispatcher::TimerInfoV2::~TimerInfoV2()': the
      destructor: Python removes its C++
      QAbstractEventDispatcher::TimerInfoV2 by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QAbstractEventDispatcher::TimerInfoV2 is created at the first
      use, not by 'QAbstractEventDispatcher::TimerInfoV2(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAbstractEventDispatcher::TimerInfoV2 back gives a
      copy the ritual made for Python, in a new cute
      QAbstractEventDispatcher::TimerInfoV2.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractEventDispatcher::TimerInfoV2'

    #  Qt's '~QAbstractEventDispatcher::TimerInfoV2()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QAbstractEventDispatcher::TimerInfoV2 behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN24QAbstractEventDispatcher11TimerInfoV2D1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QAbstractEventDispatcher::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracteventdispatcher.html#tr

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
    #  QString QAbstractEventDispatcher::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QAbstractEventDispatcher2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload()
  @overload(QThread)
  @overload(NoneType)
  def instance(
      thread: Optional[QThread] = None,
  ) -> Optional[QAbstractEventDispatcher]:
    """
    Calls Qt's 'QAbstractEventDispatcher
    *QAbstractEventDispatcher::instance(QThread *thread)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#instance

    Parameters
    ----------

    thread : Optional[QThread]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QAbstractEventDispatcher]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractEventDispatcher *QAbstractEventDispatcher::instance(QThread
    #      *thread)
    address = Rituals.call(
        'ritual_ZN24QAbstractEventDispatcher8instanceEP7QThread',
        CuteMixin._addressOf(thread),
    )
    return QAbstractEventDispatcher._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractEventDispatcher'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractEventDispatcher::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractEventDispatcher::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstractEventDispatcher10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QEventLoop.ProcessEventsFlags)
  def processEvents(self, flags: QEventLoop.ProcessEventsFlags) -> bool:
    """
    Calls Qt's 'bool
    QAbstractEventDispatcher::processEvents(QEventLoop::ProcessEventsFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#processEvents

    Parameters
    ----------

    flags : QEventLoop.ProcessEventsFlags
      Passed on as its number.
    """
    #  bool QAbstractEventDispatcher::processEvents(QEventLoop::
    #      ProcessEventsFlags flags)
    return self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEve'
        'ntLoop17ProcessEventsFlagEE',
        flags.value,
    )

  @overload(QSocketNotifier)
  @overload(NoneType)
  def registerSocketNotifier(
      self,
      notifier: Optional[QSocketNotifier],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractEventDispatcher::registerSocketNotifier(QSocketNotifier
    *notifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html

    Parameters
    ----------

    notifier : Optional[QSocketNotifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractEventDispatcher::registerSocketNotifier(QSocketNotifier
    #      *notifier)
    self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher22registerSocketNotifierEP15QSo'
        'cketNotifier',
        self._addressOf(notifier),
    )

  @overload(QSocketNotifier)
  @overload(NoneType)
  def unregisterSocketNotifier(
      self,
      notifier: Optional[QSocketNotifier],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractEventDispatcher::unregisterSocketNotifier(QSocketNotifier
    *notifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html

    Parameters
    ----------

    notifier : Optional[QSocketNotifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QAbstractEventDispatcher::unregisterSocketNotifier(QSocketNotifier
    #      *notifier)
    self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher24unregisterSocketNotifierEP15Q'
        'SocketNotifier',
        self._addressOf(notifier),
    )

  @overload(int, Qt.TimerType, QObject)
  @overload(int, Qt.TimerType, NoneType)
  def registerTimer(
      self,
      interval: int,
      timerType: Qt.TimerType,
      object: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'int QAbstractEventDispatcher::registerTimer(qint64 interval,
    Qt::TimerType timerType, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#registerTimer

    Parameters
    ----------

    interval : int
      Passed on as it is.

    timerType : Qt.TimerType
      Passed on as its number.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAbstractEventDispatcher::registerTimer(qint64 interval,
    #      Qt::TimerType timerType, QObject *object)
    return self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher13registerTimerExN2Qt9TimerType'
        'EP7QObject',
        interval, timerType.value, self._addressOf(object),
    )

  @overload(int, int, Qt.TimerType, QObject)
  @overload(int, int, Qt.TimerType, NoneType)
  def registerTimer(
      self,
      timerId: int,
      interval: int,
      timerType: Qt.TimerType,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QAbstractEventDispatcher::registerTimer(int timerId,
    qint64 interval, Qt::TimerType timerType, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#registerTimer

    Parameters
    ----------

    timerId : int
      Passed on as it is.

    interval : int
      Passed on as it is.

    timerType : Qt.TimerType
      Passed on as its number.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractEventDispatcher::registerTimer(int timerId, qint64
    #      interval, Qt::TimerType timerType, QObject *object)
    self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher13registerTimerEixN2Qt9TimerTyp'
        'eEP7QObject',
        timerId, interval, timerType.value, self._addressOf(object),
    )

  @overload(int)
  def unregisterTimer(self, timerId: int) -> bool:
    """
    Calls Qt's 'bool QAbstractEventDispatcher::unregisterTimer(int timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#unregisterTimer

    Parameters
    ----------

    timerId : int
      Passed on as it is.
    """
    #  bool QAbstractEventDispatcher::unregisterTimer(int timerId)
    return self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher15unregisterTimerEi', timerId,
    )

  @overload(Qt.TimerId)
  def unregisterTimer(self, timerId: Qt.TimerId) -> bool:
    """
    Calls Qt's 'bool QAbstractEventDispatcher::unregisterTimer(Qt::TimerId
    timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#unregisterTimer

    Parameters
    ----------

    timerId : Qt.TimerId
      Passed on as its number.
    """
    #  bool QAbstractEventDispatcher::unregisterTimer(Qt::TimerId timerId)
    return self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher15unregisterTimerEN2Qt7TimerIdE',
        timerId.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def unregisterTimers(self, object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QAbstractEventDispatcher::unregisterTimers(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#unregisterTimers

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractEventDispatcher::unregisterTimers(QObject *object)
    return self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher16unregisterTimersEP7QObject',
        self._addressOf(object),
    )

  @overload(int)
  def remainingTime(self, timerId: int) -> int:
    """
    Calls Qt's 'int QAbstractEventDispatcher::remainingTime(int timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#remainingTime

    Parameters
    ----------

    timerId : int
      Passed on as it is.
    """
    #  int QAbstractEventDispatcher::remainingTime(int timerId)
    return self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher13remainingTimeEi', timerId,
    )

  def wakeUp(self) -> None:
    """
    Calls Qt's 'void QAbstractEventDispatcher::wakeUp()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#wakeUp
    """
    #  void QAbstractEventDispatcher::wakeUp()
    self.uglySide.call('ritual_ZN24QAbstractEventDispatcher6wakeUpEv')

  def interrupt(self) -> None:
    """
    Calls Qt's 'void QAbstractEventDispatcher::interrupt()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#interrupt
    """
    #  void QAbstractEventDispatcher::interrupt()
    self.uglySide.call('ritual_ZN24QAbstractEventDispatcher9interruptEv')

  def startingUp(self) -> None:
    """
    Calls Qt's 'void QAbstractEventDispatcher::startingUp()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#startingUp
    """
    #  void QAbstractEventDispatcher::startingUp()
    self.uglySide.call('ritual_ZN24QAbstractEventDispatcher10startingUpEv')

  def closingDown(self) -> None:
    """
    Calls Qt's 'void QAbstractEventDispatcher::closingDown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html#closingDown
    """
    #  void QAbstractEventDispatcher::closingDown()
    self.uglySide.call('ritual_ZN24QAbstractEventDispatcher11closingDownEv')

  @overload(QAbstractNativeEventFilter)
  @overload(NoneType)
  def installNativeEventFilter(
      self,
      filterObj: Optional[QAbstractNativeEventFilter],
  ) -> None:
    """
    Calls Qt's 'void QAbstractEventDispatcher::installNativeEventFilter(
    QAbstractNativeEventFilter *filterObj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html

    Parameters
    ----------

    filterObj : Optional[QAbstractNativeEventFilter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractEventDispatcher::installNativeEventFilter(
    #      QAbstractNativeEventFilter *filterObj)
    self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher24installNativeEventFilterEP26Q'
        'AbstractNativeEventFilter',
        self._addressOf(filterObj),
    )

  @overload(QAbstractNativeEventFilter)
  @overload(NoneType)
  def removeNativeEventFilter(
      self,
      filterObj: Optional[QAbstractNativeEventFilter],
  ) -> None:
    """
    Calls Qt's 'void QAbstractEventDispatcher::removeNativeEventFilter(
    QAbstractNativeEventFilter *filterObj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracteventdispatcher.html

    Parameters
    ----------

    filterObj : Optional[QAbstractNativeEventFilter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractEventDispatcher::removeNativeEventFilter(
    #      QAbstractNativeEventFilter *filterObj)
    self.uglySide.call(
        'ritual_ZN24QAbstractEventDispatcher23removeNativeEventFilterEP26QA'
        'bstractNativeEventFilter',
        self._addressOf(filterObj),
    )
