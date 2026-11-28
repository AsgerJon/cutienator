"""
QModbusTcpClientPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qmodbustcpclient_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QModbusTcpClientPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QModbusClientPrivate, QModbusReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice
  from . import QModbusDataUnit, QModbusRequest, QModbusTcpClient
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModbusDataUnit = WAIT['QModbusDataUnit']
  QModbusRequest = WAIT['QModbusRequest']


class QModbusTcpClientPrivate(QModbusClientPrivate):
  """
  The cute side of Qt's QModbusTcpClientPrivate: a plain Python object
  standing in front of one C++ QModbusTcpClientPrivate.

  It is built on the cute 'QModbusClientPrivate', as Qt's
  QModbusTcpClientPrivate is built on Qt's QModbusClientPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusTcpClientPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'q_func', 'setupTcpSocket',
  'enqueueRequest', 'isOpen', 'cleanupTransactionStore',
  'incrementTransactionId', 'transactionId', 'device'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QModbusTcpClient *QModbusTcpClientPrivate::q_func() const':
    takes in Python what 'QModbusTcpClient
    *QModbusTcpClientPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QModbusTcpClientPrivate is created at the first use, not by
    'QModbusTcpClientPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusTcpClientPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusTcpClientPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool QModbusTcpClientPrivate::isOpen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpclientprivate.html#isOpen
    """
    #  bool QModbusTcpClientPrivate::isOpen() const
    ritual = 'ritual_ZNK23QModbusTcpClientPrivate6isOpenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QModbusTcpClientPrivate6isOpenEv'
    return self.uglySide.call(ritual)

  def transactionId(self) -> int:
    """
    Calls Qt's 'int QModbusTcpClientPrivate::transactionId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpclientprivate.html#transactionId
    """
    #  int QModbusTcpClientPrivate::transactionId() const
    return self.uglySide.call(
        'ritual_ZNK23QModbusTcpClientPrivate13transactionIdEv',
    )

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QModbusTcpClientPrivate::device() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpclientprivate.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QModbusTcpClientPrivate::device() const
    ritual = 'ritual_ZNK23QModbusTcpClientPrivate6deviceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QModbusTcpClientPrivate6deviceEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

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

  def q_func(self) -> Optional[QModbusTcpClient]:
    """
    Calls Qt's 'QModbusTcpClient *QModbusTcpClientPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpclientprivate.html#q_func

    Returns
    -------

    Optional[QModbusTcpClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusTcpClient *QModbusTcpClientPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QModbusTcpClientPrivate6q_funcEv',
    )
    from . import QModbusTcpClient
    return QModbusTcpClient._cuteAt(address)

  def setupTcpSocket(self) -> None:
    """
    Calls Qt's 'void QModbusTcpClientPrivate::setupTcpSocket()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpclientprivate.html#setupTcpSocket
    """
    #  void QModbusTcpClientPrivate::setupTcpSocket()
    self.uglySide.call(
        'ritual_ZN23QModbusTcpClientPrivate14setupTcpSocketEv',
    )

  @overload(QModbusRequest, int, QModbusDataUnit, QModbusReply.ReplyType)
  def enqueueRequest(
      self,
      request: QModbusRequest,
      serverAddress: int,
      unit: QModbusDataUnit,
      type: QModbusReply.ReplyType,
  ) -> Optional[QModbusReply]:
    """
    Calls Qt's 'QModbusReply *QModbusTcpClientPrivate::enqueueRequest(const
    QModbusRequest &request, int serverAddress, const QModbusDataUnit &unit,
    QModbusReply::ReplyType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpclientprivate.html#enqueueRequest

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    serverAddress : int
      Passed on as it is.

    unit : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    type : QModbusReply.ReplyType
      Passed on as its number.

    Returns
    -------

    Optional[QModbusReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusReply *QModbusTcpClientPrivate::enqueueRequest(const
    #      QModbusRequest &request, int serverAddress, const QModbusDataUnit
    #      &unit, QModbusReply::ReplyType type)
    ritual = (
        'ritual_ZN23QModbusTcpClientPrivate14enqueueRequestERK14QModbusRequ'
        'estiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QModbusTcpClientPrivate14enqueueRequestERK14QModb'
          'usRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE')
    address = self.uglySide.call(
        ritual,
        self._valueOf(request), serverAddress, self._valueOf(unit),
        type.value,
    )
    return QModbusReply._cuteAt(address)

  def cleanupTransactionStore(self) -> None:
    """
    Calls Qt's 'void QModbusTcpClientPrivate::cleanupTransactionStore()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpclientprivate.html
    """
    #  void QModbusTcpClientPrivate::cleanupTransactionStore()
    self.uglySide.call(
        'ritual_ZN23QModbusTcpClientPrivate23cleanupTransactionStoreEv',
    )

  def incrementTransactionId(self) -> None:
    """
    Calls Qt's 'void QModbusTcpClientPrivate::incrementTransactionId()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpclientprivate.html
    """
    #  void QModbusTcpClientPrivate::incrementTransactionId()
    self.uglySide.call(
        'ritual_ZN23QModbusTcpClientPrivate22incrementTransactionIdEv',
    )
