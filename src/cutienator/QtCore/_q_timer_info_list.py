"""
QTimerInfoList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtimerinfo_unix_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTimerInfoList to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QObject, QTimerInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QTimerInfo = WAIT['QTimerInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTimerInfoList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTimerInfoList: a plain Python object standing in
  front of one C++ QTimerInfoList.

  C++ hands a QTimerInfoList around as a copy, so every C++ QTimerInfoList
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTimerInfoList that has a ritual and that Python can
  call so far, 8 names in all: 'timerInsert', 'unregisterTimer',
  'unregisterTimers', 'activateTimers', 'hasPendingTimers', 'clearTimers',
  'isEmpty', 'size'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::optional<Duration> QTimerInfoList::timerWait()': gives a type
    Python has no way to take yet.
  - Qt's 'Duration QTimerInfoList::remainingDuration(Qt::TimerId timerId)
    const': gives a type Python has no way to take yet.
  - Qt's 'void QTimerInfoList::registerTimer(Qt::TimerId timerId, Duration
    interval, Qt::TimerType timerType, QObject *object)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QList<TimerInfo> QTimerInfoList::registeredTimers(QObject *object)
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<QTimerInfo *>::const_iterator
    QTimerInfoList::findTimerById(Qt::TimerId timerId) const': gives a type
    Python has no way to take yet.
  - Qt's 'std::chrono::steady_clock::time_point
    QTimerInfoList::updateCurrentTime() const': gives a type Python has no
    way to take yet.
  - Qt's 'QTimerInfoList::~QTimerInfoList()': the destructor: Python removes
    its C++ QTimerInfoList by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTimerInfoList is created at the first use, not by
    'QTimerInfoList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTimerInfoList back gives a copy the ritual made for
    Python, in a new cute QTimerInfoList.
  - Each name of Qt's QTimerInfoList that has no cute function yet,
    'findTimerById', 'registerTimer', 'registeredTimers',
    'remainingDuration', 'timerWait', 'updateCurrentTime', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTimerInfoList'

  #  Qt's '~QTimerInfoList()'. Naming it makes this a value class: Python
  #  owns every C++ QTimerInfoList behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QTimerInfoListD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QTimerInfoList::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerinfolist.html#isEmpty
    """
    #  bool QTimerInfoList::isEmpty() const
    return self.uglySide.call('ritual_ZNK14QTimerInfoList7isEmptyEv')

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QTimerInfoList::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerinfolist.html#size
    """
    #  qsizetype QTimerInfoList::size() const
    return self.uglySide.call('ritual_ZNK14QTimerInfoList4sizeEv')

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTimerInfoList::QTimerInfoList()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimerinfolist.html#QTimerInfoList
    """
    #  QTimerInfoList::QTimerInfoList()
    self._noteCreation(QTimerInfoList, lambda: Rituals.call(
        'ritual_ZN14QTimerInfoListC1Ev',
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

  @overload(QTimerInfo)
  @overload(NoneType)
  def timerInsert(self, a0: Optional[QTimerInfo]) -> None:
    """
    Calls Qt's 'void QTimerInfoList::timerInsert(QTimerInfo *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerinfolist.html#timerInsert

    Parameters
    ----------

    a0 : Optional[QTimerInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTimerInfoList::timerInsert(QTimerInfo *a0)
    self.uglySide.call(
        'ritual_ZN14QTimerInfoList11timerInsertEP10QTimerInfo',
        self._addressOf(a0),
    )

  @overload(Qt.TimerId)
  def unregisterTimer(self, timerId: Qt.TimerId) -> bool:
    """
    Calls Qt's 'bool QTimerInfoList::unregisterTimer(Qt::TimerId timerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimerinfolist.html#unregisterTimer

    Parameters
    ----------

    timerId : Qt.TimerId
      Passed on as its number.
    """
    #  bool QTimerInfoList::unregisterTimer(Qt::TimerId timerId)
    return self.uglySide.call(
        'ritual_ZN14QTimerInfoList15unregisterTimerEN2Qt7TimerIdE',
        timerId.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def unregisterTimers(self, object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QTimerInfoList::unregisterTimers(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimerinfolist.html#unregisterTimers

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTimerInfoList::unregisterTimers(QObject *object)
    return self.uglySide.call(
        'ritual_ZN14QTimerInfoList16unregisterTimersEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def activateTimers(self) -> int:
    """
    Calls Qt's 'int QTimerInfoList::activateTimers()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerinfolist.html#activateTimers
    """
    #  int QTimerInfoList::activateTimers()
    return self.uglySide.call('ritual_ZN14QTimerInfoList14activateTimersEv')

  def hasPendingTimers(self) -> bool:
    """
    Calls Qt's 'bool QTimerInfoList::hasPendingTimers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimerinfolist.html#hasPendingTimers
    """
    #  bool QTimerInfoList::hasPendingTimers()
    return self.uglySide.call(
        'ritual_ZN14QTimerInfoList16hasPendingTimersEv',
    )

  def clearTimers(self) -> None:
    """
    Calls Qt's 'void QTimerInfoList::clearTimers()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerinfolist.html#clearTimers
    """
    #  void QTimerInfoList::clearTimers()
    self.uglySide.call('ritual_ZN14QTimerInfoList11clearTimersEv')

  @staticmethod
  def findTimerById(*__, **_) -> Never:
    """
    Qt's 'QList<QTimerInfo *>::const_iterator
    QTimerInfoList::findTimerById(Qt::TimerId timerId) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTimerInfoList.findTimerById' has no cute function yet. Qt's "
        "'QList<QTimerInfo *>::const_iterator "
        "QTimerInfoList::findTimerById(Qt::TimerId timerId) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def registerTimer(*__, **_) -> Never:
    """
    Qt's 'void QTimerInfoList::registerTimer(Qt::TimerId timerId, Duration
    interval, Qt::TimerType timerType, QObject *object)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTimerInfoList.registerTimer' has no cute function yet. Qt's "
        "'void QTimerInfoList::registerTimer(Qt::TimerId timerId, Duration "
        "interval, Qt::TimerType timerType, QObject *object)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def registeredTimers(*__, **_) -> Never:
    """
    Qt's 'QList<TimerInfo> QTimerInfoList::registeredTimers(QObject *object)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTimerInfoList.registeredTimers' has no cute function yet. Qt's "
        "'QList<TimerInfo> QTimerInfoList::registeredTimers(QObject "
        "*object) const': gives a type Python has no way to take yet.")

  @staticmethod
  def remainingDuration(*__, **_) -> Never:
    """
    Qt's 'Duration QTimerInfoList::remainingDuration(Qt::TimerId timerId)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTimerInfoList.remainingDuration' has no cute function yet. Qt's "
        "'Duration QTimerInfoList::remainingDuration(Qt::TimerId timerId) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def timerWait(*__, **_) -> Never:
    """
    Qt's 'std::optional<Duration> QTimerInfoList::timerWait()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTimerInfoList.timerWait' has no cute function yet. Qt's "
        "'std::optional<Duration> QTimerInfoList::timerWait()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def updateCurrentTime(*__, **_) -> Never:
    """
    Qt's 'std::chrono::steady_clock::time_point
    QTimerInfoList::updateCurrentTime() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QTimerInfoList.updateCurrentTime' has no cute function yet. Qt's "
        "'std::chrono::steady_clock::time_point "
        "QTimerInfoList::updateCurrentTime() const': gives a type Python "
        "has no way to take yet.")
