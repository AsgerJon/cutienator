"""
QModbusTcpServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qmodbustcpserver_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QModbusTcpServerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QModbusDevice, QModbusServerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QModbusRequest, QModbusResponse, QModbusTcpServer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModbusRequest = WAIT['QModbusRequest']


class QModbusTcpServerPrivate(QModbusServerPrivate):
  """
  The cute side of Qt's QModbusTcpServerPrivate: a plain Python object
  standing in front of one C++ QModbusTcpServerPrivate.

  It is built on the cute 'QModbusServerPrivate', as Qt's
  QModbusTcpServerPrivate is built on Qt's QModbusServerPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusTcpServerPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func', 'forwardProcessRequest',
  'forwardError', 'matchingServerAddress', 'setupTcpServer'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QModbusTcpServer *QModbusTcpServerPrivate::q_func() const':
    takes in Python what 'QModbusTcpServer
    *QModbusTcpServerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QModbusTcpServerPrivate is created at the first use, not by
    'QModbusTcpServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusTcpServerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusTcpServerPrivate'

  #  A C++ QModbusTcpServerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusTcpServerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def matchingServerAddress(self, unitId: int) -> bool:
    """
    Calls Qt's 'bool QModbusTcpServerPrivate::matchingServerAddress(quint8
    unitId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpserverprivate.html#matchingServerAddress

    Parameters
    ----------

    unitId : int
      Passed on as it is.
    """
    #  bool QModbusTcpServerPrivate::matchingServerAddress(quint8 unitId)
    #      const
    return self.uglySide.call(
        'ritual_ZNK23QModbusTcpServerPrivate21matchingServerAddressEh',
        unitId,
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

  def q_func(self) -> Optional[QModbusTcpServer]:
    """
    Calls Qt's 'QModbusTcpServer *QModbusTcpServerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpserverprivate.html#q_func

    Returns
    -------

    Optional[QModbusTcpServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusTcpServer *QModbusTcpServerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QModbusTcpServerPrivate6q_funcEv',
    )
    from . import QModbusTcpServer
    return QModbusTcpServer._cuteAt(address)

  @overload(QModbusRequest)
  def forwardProcessRequest(self, r: QModbusRequest) -> QModbusResponse:
    """
    Calls Qt's 'QModbusResponse
    QModbusTcpServerPrivate::forwardProcessRequest(const QModbusRequest &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpserverprivate.html#forwardProcessRequest

    Parameters
    ----------

    r : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    Returns
    -------

    QModbusResponse
      A new cute QModbusResponse around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusResponse QModbusTcpServerPrivate::forwardProcessRequest(const
    #      QModbusRequest &r)
    address = self.uglySide.call(
        'ritual_ZN23QModbusTcpServerPrivate21forwardProcessRequestERK14QMod'
        'busRequest',
        self._valueOf(r),
    )
    from . import QModbusResponse
    return QModbusResponse._cuteOwning(address)

  @overload(str, QModbusDevice.Error)
  def forwardError(self, errorText: str, error: QModbusDevice.Error) -> None:
    """
    Calls Qt's 'void QModbusTcpServerPrivate::forwardError(const QString
    &errorText, QModbusDevice::Error error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpserverprivate.html#forwardError

    Parameters
    ----------

    errorText : str
      Passed on as it is: a QString is made of it for the call.

    error : QModbusDevice.Error
      Passed on as its number.
    """
    #  void QModbusTcpServerPrivate::forwardError(const QString &errorText,
    #      QModbusDevice::Error error)
    self.uglySide.call(
        'ritual_ZN23QModbusTcpServerPrivate12forwardErrorERK7QStringN13QMod'
        'busDevice5ErrorE',
        errorText, error.value,
    )

  def setupTcpServer(self) -> None:
    """
    Calls Qt's 'void QModbusTcpServerPrivate::setupTcpServer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpserverprivate.html#setupTcpServer
    """
    #  void QModbusTcpServerPrivate::setupTcpServer()
    self.uglySide.call(
        'ritual_ZN23QModbusTcpServerPrivate14setupTcpServerEv',
    )
