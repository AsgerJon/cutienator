"""
QRemoteObjectPendingCall binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectpendingcall.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QRemoteObjectPendingCallData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRemoteObjectPendingCallData = WAIT['QRemoteObjectPendingCallData']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectPendingCall(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRemoteObjectPendingCall: a plain Python object
  standing in front of one C++ QRemoteObjectPendingCall.

  C++ hands a QRemoteObjectPendingCall around as a copy, so every C++
  QRemoteObjectPendingCall behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRemoteObjectPendingCall that has a ritual and that
  Python can call so far, 5 names in all: 'returnValue', 'error',
  'isFinished', 'waitForFinished', 'fromCompletedCall'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRemoteObjectPendingCall::~QRemoteObjectPendingCall()': the
    destructor: Python removes its C++ QRemoteObjectPendingCall by it, and
    has no other use for it.
  - Qt's 'QRemoteObjectPendingCall &QRemoteObjectPendingCall::operator=(const
    QRemoteObjectPendingCall &other)': assignment: Python binds a name and
    has no operator for it.

  What to expect
  --------------

  - The C++ QRemoteObjectPendingCall is created at the first use, not by
    'QRemoteObjectPendingCall(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRemoteObjectPendingCall back gives a copy the ritual
    made for Python, in a new cute QRemoteObjectPendingCall.
  """

  #  The enums Qt writes inside QRemoteObjectPendingCall, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Error(CuteNum):
    """
    The enum 'QRemoteObjectPendingCall::Error' of Qt, with the 2 names Qt
    gives in it.
    """

    NoError = Kee[int](0)
    InvalidMessage = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVariant)
  def fromCompletedCall(returnValue: QVariant) -> QRemoteObjectPendingCall:
    """
    Calls Qt's 'QRemoteObjectPendingCall
    QRemoteObjectPendingCall::fromCompletedCall(const QVariant
    &returnValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcall.html#fromCompletedCall

    Parameters
    ----------

    returnValue : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QRemoteObjectPendingCall
      A new cute QRemoteObjectPendingCall around the copy Qt gave back.
      Python owns it.
    """
    #  QRemoteObjectPendingCall
    #      QRemoteObjectPendingCall::fromCompletedCall(const QVariant
    #      &returnValue)
    address = Rituals.call(
        'ritual_ZN24QRemoteObjectPendingCall17fromCompletedCallERK8QVariant',
        CuteMixin._valueOf(returnValue),
    )
    return QRemoteObjectPendingCall._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectPendingCall'

  #  Qt's '~QRemoteObjectPendingCall()'. Naming it makes this a value class:
  #  Python owns every C++ QRemoteObjectPendingCall behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QRemoteObjectPendingCallD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def returnValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QRemoteObjectPendingCall::returnValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcall.html#returnValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QRemoteObjectPendingCall::returnValue() const
    address = self._callAs(
        'QRemoteObjectPendingCall',
        'ritual_ZNK24QRemoteObjectPendingCall11returnValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def error(self) -> Error:
    """
    Calls Qt's 'QRemoteObjectPendingCall::Error
    QRemoteObjectPendingCall::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcall.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  QRemoteObjectPendingCall::Error QRemoteObjectPendingCall::error()
    #      const
    return QRemoteObjectPendingCall.Error(self._callAs(
        'QRemoteObjectPendingCall',
        'ritual_ZNK24QRemoteObjectPendingCall5errorEv',
    ))

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectPendingCall::isFinished() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcall.html#isFinished
    """
    #  bool QRemoteObjectPendingCall::isFinished() const
    return self._callAs(
        'QRemoteObjectPendingCall',
        'ritual_ZNK24QRemoteObjectPendingCall10isFinishedEv',
    )

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
    Notes what was given, for Qt's
    'QRemoteObjectPendingCall::QRemoteObjectPendingCall()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcall.html
    """
    #  QRemoteObjectPendingCall::QRemoteObjectPendingCall()
    self._noteCreation(QRemoteObjectPendingCall, lambda: Rituals.call(
        'ritual_ZN24QRemoteObjectPendingCallC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QRemoteObjectPendingCall) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectPendingCall::QRemoteObjectPendingCall(const
    QRemoteObjectPendingCall &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcall.html

    Parameters
    ----------

    other : QRemoteObjectPendingCall
      Passed on as a value: Qt reads the C++ QRemoteObjectPendingCall, which
      stays Python's own.
    """
    #  QRemoteObjectPendingCall::QRemoteObjectPendingCall(const
    #      QRemoteObjectPendingCall &other)
    self._noteCreation(QRemoteObjectPendingCall, lambda: Rituals.call(
        'ritual_ZN24QRemoteObjectPendingCallC1ERKS_',
        self._valueOf(other, 'QRemoteObjectPendingCall'),
    ))

  @overload(QRemoteObjectPendingCallData)
  @overload(NoneType)
  def __init__(self, dd: Optional[QRemoteObjectPendingCallData]) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectPendingCall::QRemoteObjectPendingCall(
    QRemoteObjectPendingCallData *dd)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcall.html

    Parameters
    ----------

    dd : Optional[QRemoteObjectPendingCallData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRemoteObjectPendingCall::QRemoteObjectPendingCall(
    #      QRemoteObjectPendingCallData *dd)
    self._noteCreation(QRemoteObjectPendingCall, lambda: Rituals.call(
        'ritual_ZN24QRemoteObjectPendingCallC1EP28QRemoteObjectPendingCallD'
        'ata',
        self._addressOf(dd),
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
  @overload(int)
  def waitForFinished(self, timeout: int = 30000) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectPendingCall::waitForFinished(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcall.html#waitForFinished

    Parameters
    ----------

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QRemoteObjectPendingCall::waitForFinished(int timeout)
    return self._callAs(
        'QRemoteObjectPendingCall',
        'ritual_ZN24QRemoteObjectPendingCall15waitForFinishedEi',
        timeout,
    )
