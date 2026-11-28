"""
QModbusClient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbusclient.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QModbusDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QModbusClientPrivate, QModbusDataUnit, QModbusReply
  from . import QModbusRequest, QModbusResponse
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModbusDataUnit = WAIT['QModbusDataUnit']
  QModbusRequest = WAIT['QModbusRequest']
  QModbusResponse = WAIT['QModbusResponse']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModbusClient(QModbusDevice):
  """
  The cute side of Qt's QModbusClient: a plain Python object standing in
  front of one C++ QModbusClient.

  It is built on the cute 'QModbusDevice', as Qt's QModbusClient is built on
  Qt's QModbusDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusClient that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'd_func',
  'sendReadRequest', 'sendWriteRequest', 'sendReadWriteRequest',
  'sendRawRequest', 'timeout', 'setTimeout', 'numberOfRetries',
  'setNumberOfRetries', 'timeoutChanged', 'processResponse',
  'processPrivateResponse'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QModbusClient::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QModbusClient::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QModbusClientPrivate *QModbusClient::d_func() const': takes
    in Python what 'QModbusClientPrivate *QModbusClient::d_func()' takes.
  - Qt's 'QModbusClient::~QModbusClient()': the destructor: Python never
    removes a C++ QModbusClient.
  - Qt's 'QModbusClient::QModbusClient(QModbusClientPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QModbusClient is created at the first use, not by
    'QModbusClient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusClient.
  - Qt tells when it has removed the C++ QModbusClient. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QModbusClient::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#tr

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
    #  QString QModbusClient::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QModbusClient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusClient'

  #  A C++ QModbusClient Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusClient'

  #  The functions Qt calls itself that QModbusClient is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'processResponse': (
          ('_ZN13QModbusClient15processResponseERK15QModbusResponseP15QModb'
           'usDataUnit',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtSerialBus:QModbusResponse'),
               ('address', 'address', 'QtSerialBus:QModbusDataUnit'),
           )),
      ),
      'processPrivateResponse': (
          ('_ZN13QModbusClient22processPrivateResponseERK15QModbusResponseP'
           '15QModbusDataUnit',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtSerialBus:QModbusResponse'),
               ('address', 'address', 'QtSerialBus:QModbusDataUnit'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QModbusClient::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QModbusClient::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QModbusClient10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def timeout(self) -> int:
    """
    Calls Qt's 'int QModbusClient::timeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#timeout
    """
    #  int QModbusClient::timeout() const
    return self.uglySide.call('ritual_ZNK13QModbusClient7timeoutEv')

  def numberOfRetries(self) -> int:
    """
    Calls Qt's 'int QModbusClient::numberOfRetries() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#numberOfRetries
    """
    #  int QModbusClient::numberOfRetries() const
    return self.uglySide.call('ritual_ZNK13QModbusClient15numberOfRetriesEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTimeout(self, newTimeout: int) -> None:
    """
    Calls Qt's 'void QModbusClient::setTimeout(int newTimeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#setTimeout

    Parameters
    ----------

    newTimeout : int
      Passed on as it is.
    """
    #  void QModbusClient::setTimeout(int newTimeout)
    self.uglySide.call('ritual_ZN13QModbusClient10setTimeoutEi', newTimeout)

  @overload(int)
  def setNumberOfRetries(self, number: int) -> None:
    """
    Calls Qt's 'void QModbusClient::setNumberOfRetries(int number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclient.html#setNumberOfRetries

    Parameters
    ----------

    number : int
      Passed on as it is.
    """
    #  void QModbusClient::setNumberOfRetries(int number)
    self.uglySide.call(
        'ritual_ZN13QModbusClient18setNumberOfRetriesEi', number,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QModbusClient::QModbusClient(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#QModbusClient

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QModbusClient::QModbusClient(QObject *parent)
    self._noteCreation(QModbusClient, lambda: Rituals.call(
        'ritual_ZN13QModbusClientC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QModbusClientPrivate]:
    """
    Calls Qt's 'QModbusClientPrivate *QModbusClient::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#d_func

    Returns
    -------

    Optional[QModbusClientPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusClientPrivate *QModbusClient::d_func()
    address = self.uglySide.call('ritual_ZN13QModbusClient6d_funcEv')
    from . import QModbusClientPrivate
    return QModbusClientPrivate._cuteAt(address)

  @overload(QModbusDataUnit, int)
  def sendReadRequest(
      self,
      read: QModbusDataUnit,
      serverAddress: int,
  ) -> Optional[QModbusReply]:
    """
    Calls Qt's 'QModbusReply *QModbusClient::sendReadRequest(const
    QModbusDataUnit &read, int serverAddress)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#sendReadRequest

    Parameters
    ----------

    read : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    serverAddress : int
      Passed on as it is.

    Returns
    -------

    Optional[QModbusReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusReply *QModbusClient::sendReadRequest(const QModbusDataUnit
    #      &read, int serverAddress)
    address = self.uglySide.call(
        'ritual_ZN13QModbusClient15sendReadRequestERK15QModbusDataUniti',
        self._valueOf(read), serverAddress,
    )
    from . import QModbusReply
    return QModbusReply._cuteAt(address)

  @overload(QModbusDataUnit, int)
  def sendWriteRequest(
      self,
      write: QModbusDataUnit,
      serverAddress: int,
  ) -> Optional[QModbusReply]:
    """
    Calls Qt's 'QModbusReply *QModbusClient::sendWriteRequest(const
    QModbusDataUnit &write, int serverAddress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclient.html#sendWriteRequest

    Parameters
    ----------

    write : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    serverAddress : int
      Passed on as it is.

    Returns
    -------

    Optional[QModbusReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusReply *QModbusClient::sendWriteRequest(const QModbusDataUnit
    #      &write, int serverAddress)
    address = self.uglySide.call(
        'ritual_ZN13QModbusClient16sendWriteRequestERK15QModbusDataUniti',
        self._valueOf(write), serverAddress,
    )
    from . import QModbusReply
    return QModbusReply._cuteAt(address)

  @overload(QModbusDataUnit, QModbusDataUnit, int)
  def sendReadWriteRequest(
      self,
      read: QModbusDataUnit,
      write: QModbusDataUnit,
      serverAddress: int,
  ) -> Optional[QModbusReply]:
    """
    Calls Qt's 'QModbusReply *QModbusClient::sendReadWriteRequest(const
    QModbusDataUnit &read, const QModbusDataUnit &write, int serverAddress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclient.html#sendReadWriteRequest

    Parameters
    ----------

    read : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    write : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    serverAddress : int
      Passed on as it is.

    Returns
    -------

    Optional[QModbusReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusReply *QModbusClient::sendReadWriteRequest(const
    #      QModbusDataUnit &read, const QModbusDataUnit &write, int
    #      serverAddress)
    address = self.uglySide.call(
        'ritual_ZN13QModbusClient20sendReadWriteRequestERK15QModbusDataUnit'
        'S2_i',
        self._valueOf(read), self._valueOf(write), serverAddress,
    )
    from . import QModbusReply
    return QModbusReply._cuteAt(address)

  @overload(QModbusRequest, int)
  def sendRawRequest(
      self,
      request: QModbusRequest,
      serverAddress: int,
  ) -> Optional[QModbusReply]:
    """
    Calls Qt's 'QModbusReply *QModbusClient::sendRawRequest(const
    QModbusRequest &request, int serverAddress)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#sendRawRequest

    Parameters
    ----------

    request : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    serverAddress : int
      Passed on as it is.

    Returns
    -------

    Optional[QModbusReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusReply *QModbusClient::sendRawRequest(const QModbusRequest
    #      &request, int serverAddress)
    address = self.uglySide.call(
        'ritual_ZN13QModbusClient14sendRawRequestERK14QModbusRequesti',
        self._valueOf(request), serverAddress,
    )
    from . import QModbusReply
    return QModbusReply._cuteAt(address)

  @overload(int)
  def timeoutChanged(self, newTimeout: int) -> None:
    """
    Calls Qt's 'void QModbusClient::timeoutChanged(int newTimeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#timeoutChanged

    Parameters
    ----------

    newTimeout : int
      Passed on as it is.
    """
    #  void QModbusClient::timeoutChanged(int newTimeout)
    self.uglySide.call(
        'ritual_ZN13QModbusClient14timeoutChangedEi', newTimeout,
    )

  @overload(QModbusResponse, QModbusDataUnit)
  @overload(QModbusResponse, NoneType)
  def processResponse(
      self,
      response: QModbusResponse,
      data: Optional[QModbusDataUnit],
  ) -> bool:
    """
    Calls Qt's 'bool QModbusClient::processResponse(const QModbusResponse
    &response, QModbusDataUnit *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclient.html#processResponse

    Parameters
    ----------

    response : QModbusResponse
      Passed on as a value: Qt reads the C++ QModbusResponse, which stays
      Python's own.

    data : Optional[QModbusDataUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QModbusClient::processResponse(const QModbusResponse &response,
    #      QModbusDataUnit *data)
    ritual = (
        'ritual_ZN13QModbusClient15processResponseERK15QModbusResponseP15QM'
        'odbusDataUnit')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QModbusClient15processResponseERK15QModbusRespons'
          'eP15QModbusDataUnit')
    return self.uglySide.call(
        ritual, self._valueOf(response), self._addressOf(data),
    )

  @overload(QModbusResponse, QModbusDataUnit)
  @overload(QModbusResponse, NoneType)
  def processPrivateResponse(
      self,
      response: QModbusResponse,
      data: Optional[QModbusDataUnit],
  ) -> bool:
    """
    Calls Qt's 'bool QModbusClient::processPrivateResponse(const
    QModbusResponse &response, QModbusDataUnit *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclient.html#processPrivateResponse

    Parameters
    ----------

    response : QModbusResponse
      Passed on as a value: Qt reads the C++ QModbusResponse, which stays
      Python's own.

    data : Optional[QModbusDataUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QModbusClient::processPrivateResponse(const QModbusResponse
    #      &response, QModbusDataUnit *data)
    ritual = (
        'ritual_ZN13QModbusClient22processPrivateResponseERK15QModbusRespon'
        'seP15QModbusDataUnit')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QModbusClient22processPrivateResponseERK15QModbus'
          'ResponseP15QModbusDataUnit')
    return self.uglySide.call(
        ritual, self._valueOf(response), self._addressOf(data),
    )
